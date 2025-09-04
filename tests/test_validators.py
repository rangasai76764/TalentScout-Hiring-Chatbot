from utils.validators import validate_email, validate_phone, sanitize_tech_stack

def test_email():
    assert validate_email("x@y.com")
    assert not validate_email("notanemail")

def test_phone():
    assert validate_phone("+1234567890")
    assert validate_phone("0123456789")
    assert not validate_phone("abcd")

def test_sanitize_stack():
    l = sanitize_tech_stack("Python, Django , Postgres")
    assert "Python" in [x.capitalize() for x in l] or "python" in l
