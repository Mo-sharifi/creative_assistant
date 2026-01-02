from openai import APIConnectionError, APIError, RateLimitError

from app.config import MODEL_NAME, client

SYSTEM_PROMPT = """You are a professional text summarizer.
Your task is to rewrite the input text in a concise, accurate, and fluent manner.
Preserve key points and remove unnecessary information.
The summary should be clear and easy to understand."""


def summarize(text: str) -> str:
    """Summarize the input text"""

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Summarize this text:\n\n{text}"},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content  # type: ignore


if __name__ == "__main__":
    # Example usage
    sample_text = """
SArtificial intelligence is revolutionizing healthcare.
From diagnostic tools to personalized treatment plans,
AI is helping doctors make better decisions.
Machine learning algorithms can analyze medical images faster than humans.
This technology is expected to save millions of lives in the coming years."""
    try:
        print("=" * 50)
        print("TEXT SUMMARIZATION EXAMPLE")
        print("=" * 50)
        print(f"\nOriginal Text ({len(sample_text)} characters):")
        print(sample_text)
        print("\n" + "-" * 50)

        result = summarize(sample_text)

        print(f"\nSummary ({len(result)} characters):")
        print(result)
        print("\n" + "=" * 50)

    except ValueError as e:
        print(f"Validation Error: {e}")
    except RateLimitError:
        print("Rate Limit Error: Too many requests. Please try again later.")
    except APIConnectionError:
        print(
            "Connection Error: Failed to connect to API. Check your internet connection."
        )
    except APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
