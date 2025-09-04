from prompts import FALLBACK_PROMPT

def handle_fallback(message: str) -> str:
    """
    Provide a helpful fallback message while staying on-task (collecting info / generating questions).
    """
    return FALLBACK_PROMPT
