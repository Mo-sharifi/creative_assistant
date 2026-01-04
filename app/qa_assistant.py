from openai import APIConnectionError, APIError, RateLimitError

from app.config import MODEL_NAME, client

SYSTEM_PROMPT = """You are a helpful and knowledgeable AI assistant.
Your task is to answer questions accurately and clearly.
If context is provided, base your answer on that context.
If you reference previous messages, do so naturally.
Keep answers concise but informative."""


class QAAssistant:
    def __init__(self) -> None:
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def ask(self, question: str, context: str = ""):
        if not question or not question.strip():
            raise ValueError("Question cannot be empty")
        if context:
            prompt = f"Context:\n{context}\n\nQuestion:\n{question}"
        else:
            prompt = context

        self.messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=MODEL_NAME, messages=self.messages, temperature=0.5
        )

        answer = response.choices[0].message.content

        self.messages.append({"role": "assistant", "content": answer})

        return answer

    def clear_history(self):
        self.messages = [self.messages[0]]

    def get_history(self):
        return self.messages.copy()

    def get_message_count(self):
        return len(self.messages) - 1


if __name__ == "__main__":
    assistant = QAAssistant()

    try:
        print("=" * 60)
        print("QA ASSISTANT - CONVERSATION EXAMPLE")
        print("=" * 60)

        # Example 1: Simple conversation with memory
        print("\n--- Example 1: Conversation Memory ---\n")

        q1 = "What is the capital of France?"
        print(f"Q: {q1}")
        a1 = assistant.ask(q1)
        print(f"A: {a1}\n")

        q2 = "What is its population?"
        print(f"Q: {q2}")
        a2 = assistant.ask(q2)
        print(f"A: {a2}\n")

        # Example 2: With context
        print("--- Example 2: Question with Context ---\n")

        context = """
        Company XYZ was founded in 2020 and specializes in AI solutions.
        The company has 150 employees and offices in 5 countries.
        Their main product is an AI-powered chatbot for customer service.
        """

        q3 = "How many employees does this company have?"
        print(f"Context: {context.strip()}\n")
        print(f"Q: {q3}")
        a3 = assistant.ask(q3, context=context)
        print(f"A: {a3}\n")

        print(f"Total messages in history: {assistant.get_message_count()}")
        print("=" * 60)

    except ValueError as e:
        print(f"Validation Error: {e}")
    except RateLimitError:
        print("Rate Limit Error: Too many requests. Please try again later.")
    except APIConnectionError:
        print("Connection Error: Failed to connect to API.")
    except APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
