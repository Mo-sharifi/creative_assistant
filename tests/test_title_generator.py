import pytest

from app.title_generator import generate_title


def test_generate_title_empty():
    """Test with empty topic - should raise error"""
    with pytest.raises(ValueError):
        generate_title("")


def test_generate_title_whitespace():
    """Test with whitespace only"""
    with pytest.raises(ValueError):
        generate_title("   ")


# def test_generate_title_basic():
#     """Basic title generation test - temporarily disabled due to rate limit"""
#     topic = "Machine learning in education"
#     result = generate_title(topic)
#     assert isinstance(result, str)
#     assert len(result) > 0
#     assert "1." in result  # Check for numbered format
