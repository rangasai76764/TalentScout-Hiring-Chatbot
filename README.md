🧑‍💼 TalentScout – AI Hiring Assistant Chatbot

A simple AI-powered hiring assistant chatbot built with Python + Streamlit.
It simulates an HR recruiter by greeting candidates, collecting essential details, generating tailored technical interview questions, and gracefully ending the conversation.

✨ Features

✅ Friendly greeting to candidates
✅ Collects essential candidate details:

Full Name

Email

Phone

Years of Experience

Desired Position(s)

Current Location

Tech Stack (languages, frameworks, databases, tools)

✅ Generates 3–5 tailored technical questions per declared tech stack item
✅ Maintains context throughout the conversation for coherent flow
✅ Handles exit keywords (bye, quit, exit) gracefully
✅ Includes fallback responses for unexpected or unclear inputs
✅ Clean, stage-based conversation flow
✅ Built with Streamlit for a modern, user-friendly UI

📂 Project Structure
TalentScout-Hiring-Assistant/
│── app.py               # Streamlit app (UI + chatbot loop)
│── chatbot.py           # Core chatbot logic (stages, state, flow)
│── prompts.py           # Centralized prompts & sample tech questions
│── data_handler.py      # Candidate data storage with anonymization
│── requirements.txt     # Dependencies
│── README.md            # Documentation (this file)

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/TalentScout-Hiring-Assistant.git
cd TalentScout-Hiring-Assistant


Create a virtual environment:

python -m venv venv


Activate the environment:

Windows (PowerShell):

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

▶️ Running the App

From the project root folder:

streamlit run app.py


Open your browser → http://localhost:8501

🧠 How It Works
1️⃣ Greeting Stage

Welcomes the candidate and introduces the chatbot.

2️⃣ Information Gathering Stage

Collects candidate details step by step (name, email, phone, experience, position, location, tech stack).

3️⃣ Tech Stack Stage

Candidate declares technologies they are proficient in (e.g., Python, Django, React).

4️⃣ Technical Question Generation Stage

Generates 3–5 relevant questions per technology to assess candidate proficiency.

Example for Python/Django:

[python] Explain list comprehensions and give an example.
[python] What is the GIL in Python and how does it affect concurrency?
[django] Explain the Django request/response lifecycle.
[django] How would you create a custom middleware in Django?

5️⃣ Context Handling & Fallback

Maintains conversation context for follow-ups.

Provides fallback responses for unclear or unexpected inputs.

6️⃣ Exit Stage

Ends conversation gracefully on keywords like bye, quit, or exit.

Thanks the candidate and informs them about next steps.

🏗️ Architecture

Streamlit UI → User-friendly web interface

State Machine Logic → Stage-based conversation handling

Prompt Engineering → Centralized in prompts.py for info collection and question generation

Question Bank → Predefined technical questions per technology

Data Handling → Temporary, anonymized storage in data_handler.py to ensure privacy compliance

📝 Data Handling & Privacy

Candidate data is simulated and anonymized.

Sensitive information is not stored in plain text.

Complies with general data privacy best practices (e.g., GDPR-style handling).

📜 Example Conversation
👋 Hello! I’m the Hiring Assistant. 
Please enter your full name:
> John Doe

Got it. Please enter your email:
> john@example.com

Now enter your phone number:
> 9876543210

How many years of experience do you have?
> 3

What positions are you applying for?
> Python Developer

Where are you located?
> Bengaluru

Please now provide your Tech Stack (comma-separated).
> Python, Django

Great! Here are some tailored questions for you:
[python] Explain list comprehensions and give an example.
[python] What is the GIL in Python and how does it affect concurrency?
[django] Explain the Django request/response lifecycle.
[django] How would you create a custom middleware in Django?

✅ Thank you for your time. We'll review your submission and contact you with next steps.

🧩 Dependencies

Python 3.8+

Streamlit

Typing (standard library)

🚀 Future Improvements

Save candidate data to a secure database

Add support for resume parsing

Deploy to Streamlit Cloud / Heroku / AWS

Expand technical question bank

Integrate LLM models (e.g., GPT, LLaMA) for dynamic question generation

📌 Challenges Faced

Designing a stage-based conversation flow without external frameworks

Ensuring 3–5 technical questions per tech stack item

Handling exit keywords and fallback responses gracefully

Keeping the code modular, readable, and extendable

📝 License

This project is open-source and available under the MIT License.

🧠 Prompt Design

The chatbot uses a stage-based prompt design stored in `prompts.py`.

- **Greeting Prompt** → Welcomes the candidate and sets a friendly tone.  
- **Information Prompts** → Sequential prompts for name, email, phone, experience, role, and location.  
- **Tech Stack Prompt** → Asks the candidate to list their technologies in a comma-separated format.  
- **Question Bank Prompts** → Each technology has a predefined list of 3–5 questions (stored in dictionaries).  
- **Fallback Prompts** → Used when the candidate provides unclear or unexpected input.  
- **Exit Prompts** → Recognizes `bye`, `quit`, or `exit` and closes the conversation gracefully.  

This structured prompt design ensures a smooth, predictable, and modular conversation flow.

🎥 Demo Video
Watch the live demo here: [Loom Link](https://loom.com/your-video-link)

📂 Repository
Source code available here: [GitHub Repo](https://github.com/your-username/TalentScout-Hiring-Assistant)

