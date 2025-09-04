from utils.question_generator import generate_questions

def test_generate_for_known_tech():
    q = generate_questions(["python", "django"])
    assert len(q) >= 3
    assert any("python" in s.lower() for s in q)

def test_generate_for_unknown_tech():
    q = generate_questions(["someobscuretech"])
    assert any("someobscuretech" in s.lower() for s in q)
