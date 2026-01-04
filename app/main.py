from openai import APIConnectionError, APIError, RateLimitError

from app.qa_assistant import QAAssistant
from app.summarizer import summarize
from app.title_generator import generate_title


def print_header():
    """Print application header"""
    print("\n" + "=" * 50)
    print("   CREATIVE ASSISTANT".center(50))
    print("=" * 50)


def print_menu():
    """Print main menu"""
    print("\n--- Main Menu ---")
    print("1. Summarize Text")
    print("2. Generate Titles")
    print("3. Q&A Assistant")
    print("4. Exit")


def summarize_mode():
    """Interactive text summarization"""
    print("\n" + "=" * 50)
    print("TEXT SUMMARIZER")
    print("=" * 50)
    print("Enter your text (press Enter twice to finish):\n")

    lines = []
    while True:
        line = input()
        if line == "":
            if lines and lines[-1] == "":
                break
            lines.append(line)
        else:
            lines.append(line)

    text = "\n".join(lines).strip()

    if not text:
        print("No text provided.")
        return

    try:
        print("\nGenerating summary...\n")
        result = summarize(text)
        print("-" * 50)
        print("Summary:")
        print(result)
        print("-" * 50)
    except Exception as e:
        handle_error(e)


def title_mode():
    """Interactive title generation"""
    print("\n" + "=" * 50)
    print("TITLE GENERATOR")
    print("=" * 50)

    topic = input("Enter your topic: ").strip()

    if not topic:
        print("No topic provided.")
        return

    try:
        print("\nGenerating titles...\n")
        result = generate_title(topic)
        print("-" * 50)
        print(result)
        print("-" * 50)
    except Exception as e:
        handle_error(e)


def qa_mode():
    """Interactive Q&A assistant"""
    print("\n" + "=" * 50)
    print("Q&A ASSISTANT")
    print("=" * 50)
    print("Type 'exit' to return to main menu")
    print("Type 'clear' to clear conversation history")
    print("Type 'context' to add context for your question")
    print("-" * 50)

    assistant = QAAssistant()

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            break
        elif question.lower() == "clear":
            assistant.clear_history()
            print("Conversation history cleared.")
            continue
        elif question.lower() == "context":
            print("\nEnter context (press Enter twice to finish):")
            context_lines = []
            while True:
                line = input()
                if line == "":
                    if context_lines and context_lines[-1] == "":
                        break
                    context_lines.append(line)
                else:
                    context_lines.append(line)

            context = "\n".join(context_lines).strip()
            question = input("\nYour question: ").strip()

            if not question:
                print("No question provided.")
                continue

            try:
                print("\nThinking...\n")
                answer = assistant.ask(question, context=context)
                print(f"Assistant: {answer}")
            except Exception as e:
                handle_error(e)
            continue

        if not question:
            continue

        try:
            print("\nThinking...\n")
            answer = assistant.ask(question)
            print(f"Assistant: {answer}")
        except Exception as e:
            handle_error(e)


def handle_error(e: Exception):
    """Handle different types of errors"""
    if isinstance(e, ValueError):
        print(f"Validation Error: {e}")
    elif isinstance(e, RateLimitError):
        print("Rate Limit: Too many requests. Please try again later.")
    elif isinstance(e, APIConnectionError):
        print("Connection Error: Failed to connect to API.")
    elif isinstance(e, APIError):
        print(f"API Error: {e}")
    else:
        print(f"Unexpected Error: {e}")


def main():
    """Main application loop"""
    print_header()

    while True:
        print_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            summarize_mode()
        elif choice == "2":
            title_mode()
        elif choice == "3":
            qa_mode()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
