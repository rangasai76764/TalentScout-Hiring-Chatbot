"""
Core chatbot logic: greeting, info collection, tech stack handling,
question generation, fallback, exit handling,
plus sentiment analysis, multilingual support, and personalization.
"""

import re
import logging
from typing import Optional
from textblob import TextBlob
from googletrans import Translator

from prompts import GREETING_PROMPT, EXIT_KEYWORDS, FALLBACK_PROMPT, THANK_YOU_PROMPT
from utils.question_generator import generate_questions
from utils.fallback import handle_fallback
from utils.validators import validate_email, sanitize_tech_stack

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class HiringAssistantChatbot:
    def __init__(self):
        # candidate_info keeps progressive fields as they are provided
        self.candidate_info = {}
        self.stage = "greeting"  # start directly at greeting
        self.translator = Translator()
        self.user_lang = "en"  # default language English

        # Define the required fields in order
        self.fields = [
            ("full_name", "Full Name"),
            ("email", "Email"),
            ("phone", "Phone Number"),
            ("years_experience", "Years of Experience"),
            ("desired_position", "Desired Position(s)"),
            ("current_location", "Current Location"),
        ]
        self.current_field_index = 0

    def _translate_to_en(self, text: str) -> str:
        """Translate user input to English for processing."""
        detected = self.translator.detect(text)
        self.user_lang = detected.lang
        if detected.lang != "en":
            return self.translator.translate(text, src=detected.lang, dest="en").text
        return text

    def _translate_back(self, text: str) -> str:
        """Translate response back to user’s language if not English."""
        if self.user_lang != "en":
            return self.translator.translate(text, src="en", dest=self.user_lang).text
        return text

    def _analyze_sentiment(self, text: str) -> str:
        """Return sentiment category: positive, neutral, or negative."""
        analysis = TextBlob(text).sentiment.polarity
        if analysis > 0.2:
            return "positive"
        elif analysis < -0.2:
            return "negative"
        else:
            return "neutral"

    def process_message(self, message: str, context, data_handler) -> str:
        # Handle multilingual translation
        original_msg = message.strip()
        message = self._translate_to_en(original_msg)
        logger.info("Processing message in stage '%s': %s", self.stage, message)

        # Exit check
        if any(token.lower() == message.lower() or token.lower() in message.lower() for token in EXIT_KEYWORDS):
            if self.candidate_info:
                data_handler.save(self.candidate_info)
            return self._translate_back(THANK_YOU_PROMPT)

        # -------- GREETING --------
        if self.stage == "greeting":
            if message.lower() == "hi":
                self.stage = "collect"  # move to collect after hi
                return self._translate_back(
                    f"{GREETING_PROMPT}\nPlease provide your {self.fields[self.current_field_index][1]}."
                )
            else:
                return self._translate_back("Please type 'hi' to begin.")

        # -------- COLLECT INFO --------
        if self.stage == "collect":
            return self._translate_back(self._collect_info(message, data_handler))

        # -------- TECH STACK --------
        if self.stage == "tech_stack":
            techs = sanitize_tech_stack(message)
            if not techs:
                return self._translate_back(
                    "I couldn't parse your tech stack. Please provide comma-separated technologies (e.g. Python, Django, PostgreSQL)."
                )
            self.candidate_info["tech_stack"] = techs
            questions_by_tech = generate_questions(techs)
            data_handler.save(self.candidate_info)
            self.stage = "questions"

            # Personalized response
            name = self.candidate_info.get("full_name", "Candidate")
            lines = [f"Thank you {name} — based on your tech stack, here are tailored technical questions:\n"]
            for tech, qs in questions_by_tech.items():
                lines.append(f"--- {tech.upper()} ---")
                for i, q in enumerate(qs, 1):
                    lines.append(f"{i}. {q}")
                lines.append("")
            lines.append("When you're done, say 'exit' or 'bye' to finish.")
            return self._translate_back("\n".join(lines))

        # -------- QUESTIONS --------
        if self.stage == "questions":
            sentiment = self._analyze_sentiment(message)
            if sentiment == "negative":
                return self._translate_back(
                    "I sense some hesitation. Don’t worry, take your time — you’re doing great! "
                    "If you want more questions, say 'more'. Otherwise, say 'exit' to finish."
                )
            elif sentiment == "positive":
                return self._translate_back(
                    "Glad to hear your enthusiasm! 🎉 If you want more questions, say 'more'. Otherwise, say 'exit' to finish."
                )
            else:
                return self._translate_back(
                    "If you want more questions, say 'more'. Otherwise, say 'exit' to finish. "
                    "You can also provide a new tech stack for fresh questions."
                )

        # -------- FALLBACK --------
        return self._translate_back(handle_fallback(message))

    def _collect_info(self, message: str, data_handler) -> str:
        """
        Sequentially collect fields from the user with validation.
        """
        key, human = self.fields[self.current_field_index]

        # Validation
        if key == "full_name":
            if not re.match(r"^[A-Za-z ]{2,50}$", message):
                return "Please enter a valid name (only letters and spaces, 2–50 characters)."
        if key == "email":
            if not validate_email(message):
                return "That doesn't look like a valid email. Please enter a valid email address (e.g. name@example.com)."
        if key == "phone":
            # ✅ Accept only global phone numbers with country code (+XX ...), allow spaces
            if not re.match(r"^\+\d{1,3}[\s]?\d{6,14}$", message.replace(" ", "")):
                return "That doesn't look like a valid phone number. Please include country code (e.g. +91 9876543210)."
        if key == "years_experience":
            if not message.isdigit() or int(message) < 0:
                return "Please enter a valid number for Years of Experience (0 or more)."
        if key == "current_location":
            if not re.match(r"^[A-Za-z ]{2,50}$", message):
                return "Please enter a valid location (only letters and spaces, 2–50 characters)."

        # Save field
        self.candidate_info[key] = message
        self.current_field_index += 1

        # Check if all fields collected
        if self.current_field_index >= len(self.fields):
            self.stage = "tech_stack"
            return "✅ All set. Please now provide your Tech Stack (comma-separated): languages, frameworks, databases, tools."

        # Otherwise ask next field
        next_key, next_human = self.fields[self.current_field_index]
        return f"✅ {human} recorded. Please provide your {next_human}."

    @property
    def state(self):
        """
        Expose candidate_info as 'state' for compatibility with Streamlit session_state usage.
        """
        return self.candidate_info
