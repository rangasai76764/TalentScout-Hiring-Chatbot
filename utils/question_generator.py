"""
Generates 4–5 unique technical questions per declared tech stack item.
Ensures no duplicates are returned.
"""

from typing import List, Dict
import random

# Seed for predictability in tests
random.seed(42)

# Small knowledge base of sample questions per tech
_QBANK = {
    "python": [
        "Explain list comprehensions and give an example.",
        "What is the GIL in Python and how does it affect concurrency?",
        "How would you profile and optimize a slow Python function?",
        "What are Python decorators and when would you use them?",
        "Explain the difference between shallow and deep copy in Python."
    ],
    "django": [
        "Explain the Django request/response lifecycle.",
        "What is Django ORM and how do you write migrations?",
        "How would you create a custom middleware in Django?",
        "What are Django signals and when to use them?",
        "How does Django handle static and media files?"
    ],
    "flask": [
        "Describe how routing works in Flask.",
        "How do you manage configuration and environment variables in Flask apps?",
        "How would you structure a medium-sized Flask application?",
        "What are Flask Blueprints and why are they useful?",
        "Explain how Flask handles sessions."
    ],
    "javascript": [
        "Explain event loop and microtasks vs macrotasks in JavaScript.",
        "What's the difference between var, let and const?",
        "How do closures work in JavaScript?",
        "Explain promises and async/await with an example.",
        "What is hoisting in JavaScript?"
    ],
    "react": [
        "Explain the virtual DOM and why React uses it.",
        "When would you use useEffect and how to avoid infinite loops?",
        "Describe the difference between controlled and uncontrolled components.",
        "What is React context and when would you use it?",
        "Explain React reconciliation."
    ],
    "sql": [
        "What is an index and how does it improve query performance?",
        "Explain the difference between INNER JOIN and LEFT JOIN.",
        "How do you approach query optimization for large tables?",
        "What is a primary key vs a foreign key?",
        "Explain normalization and denormalization."
    ],
    "postgresql": [
        "How do you perform full-text search in PostgreSQL?",
        "Explain VACUUM and why it's necessary in PostgreSQL.",
        "How would you set up replication for a Postgres database?",
        "What are materialized views and when to use them?",
        "Explain PostgreSQL transactions and isolation levels."
    ],
    "aws": [
        "Explain the difference between EC2 and Lambda and when to use each.",
        "How do you secure an S3 bucket and make static websites available?",
        "What is IAM and how do you design least-privilege policies?",
        "What is CloudFormation and how is it used?",
        "Explain VPC and subnets in AWS."
    ],
    "linux": [
        "How do you troubleshoot high CPU usage on a Linux server?",
        "Explain file permissions and how to use chmod/chown.",
        "How would you set up a scheduled task using cron?",
        "What are systemd services?",
        "Explain how to check open ports on a Linux system."
    ],
    "docker": [
        "What is the difference between a Docker image and a container?",
        "How do you create a multistage Dockerfile for a Python app?",
        "How do you persist data in Docker containers?",
        "What is Docker Compose and how is it useful?",
        "Explain the concept of Docker networking."
    ],
}

def generate_questions(tech_stack: List[str], min_q=4, max_q=5) -> Dict[str, List[str]]:
    """
    For each declared tech, sample unique questions from _QBANK.
    Ensures 4–5 questions PER tech stack item.
    Returns a dict {tech: [questions]}.
    """
    techs = [t.strip().lower() for t in tech_stack if t and t.strip()]
    if not techs:
        return {"general": ["Please specify some technologies to generate questions for."]}

    results = {}
    for tech in techs:
        bank = _QBANK.get(tech)
        if bank:
            # Ensure min 4 questions and max 5, even if bank has exactly 5
            num_questions = random.randint(min_q, min(max_q, len(bank)))
            # If bank has fewer than min_q, repeat random questions to reach min_q
            if len(bank) < min_q:
                extended_bank = bank * ((min_q // len(bank)) + 1)
                results[tech] = [f"[{tech}] {q}" for q in random.sample(extended_bank, min_q)]
            else:
                results[tech] = [f"[{tech}] {q}" for q in random.sample(bank, num_questions)]
        else:
            # Generic fallback for unknown tech
            generic_qs = [
                f"[{tech}] Describe core concepts and common pitfalls when working with {tech}.",
                f"[{tech}] What are best practices when using {tech} in production?",
                f"[{tech}] How would you troubleshoot performance issues in {tech}?",
                f"[{tech}] How do you handle scaling and optimization in {tech}?",
                f"[{tech}] Explain debugging and monitoring techniques for {tech}."
            ]
            num_questions = random.randint(min_q, max_q)
            results[tech] = random.sample(generic_qs, num_questions)

    return results
