import pytest

from app.qa_assistant import QAAssistant


def test_qa_assistant_initialization():
    """Test QA assistant initialization"""
    assistant = QAAssistant()
    assert assistant.get_message_count() == 0
    assert len(assistant.get_history()) == 1  # Only system prompt


def test_ask_empty_question():
    """Test with empty question - should raise error"""
    assistant = QAAssistant()
    with pytest.raises(ValueError):
        assistant.ask("")


def test_ask_whitespace_question():
    """Test with whitespace only"""
    assistant = QAAssistant()
    with pytest.raises(ValueError):
        assistant.ask("   ")


def test_clear_history():
    """Test clearing conversation history"""
    assistant = QAAssistant()

    # Add some mock messages manually
    assistant.messages.append({"role": "user", "content": "test"})
    assistant.messages.append({"role": "assistant", "content": "response"})

    assert assistant.get_message_count() == 2

    # Clear history
    assistant.clear_history()

    assert assistant.get_message_count() == 0
    assert len(assistant.get_history()) == 1  # Only system prompt


def test_get_history():
    """Test getting history returns a copy"""
    assistant = QAAssistant()

    history1 = assistant.get_history()
    assistant.messages.append({"role": "user", "content": "test"})
    history2 = assistant.get_history()

    # History should be different (copy, not reference)
    assert len(history1) != len(history2)


# def test_ask_basic():
#     """Basic Q&A test - temporarily disabled due to rate limit"""
#     assistant = QAAssistant()
#     answer = assistant.ask("What is 2+2?")
#     assert isinstance(answer, str)
#     assert len(answer) > 0
#     assert assistant.get_message_count() == 2  # user + assistant


# def test_ask_with_context():
#     """Test Q&A with context - temporarily disabled due to rate limit"""
#     assistant = QAAssistant()
#     context = "The sky is blue because of light scattering."
#     answer = assistant.ask("Why is the sky blue?", context=context)
#     assert isinstance(answer, str)
#     assert len(answer) > 0


# def test_conversation_memory():
#     """Test conversation memory - temporarily disabled due to rate limit"""
#     assistant = QAAssistant()
#
#     assistant.ask("My name is John")
#     answer = assistant.ask("What is my name?")
#
#     assert "john" in answer.lower()
#     assert assistant.get_message_count() == 4  # 2 user + 2 assistant
