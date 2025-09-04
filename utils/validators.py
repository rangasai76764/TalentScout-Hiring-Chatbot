# utils/validators.py
import re

def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email or "") is not None

def validate_phone(value: str) -> bool:
    """
    Validate international phone numbers.
    Format: +<country_code> <number>
    - Country code: 1–3 digits
    - Number: 6–14 digits
    - Spaces allowed between groups
    Examples:
        +1 202 555 0147
        +91 98765 43210
        +44 20 7946 0958
    """
    pattern = r"^\+\d{1,3}(?:\s?\d){6,14}$"
    return re.match(pattern, value or "") is not None

def sanitize_tech_stack(stack: str):
    if not stack:
        return []
    return [tech.strip().lower() for tech in stack.split(",") if tech.strip()]

def validate_name(name: str) -> bool:
    return bool(re.match(r"^[A-Za-z\s]{2,50}$", name or ""))

def validate_location(location: str) -> bool:
    return bool(re.match(r"^[A-Za-z\s]{2,50}$", location or ""))
