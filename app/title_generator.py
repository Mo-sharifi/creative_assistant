from openai import APIConnectionError, APIError, RateLimitError

from app.config import MODEL_NAME, client

SYSTEM_PROMPT = """You are a creative and professional title generator.
Your task is to create catchy, concise, and relevant titles for given topics.
Titles should be attention-grabbing yet accurate.
Use strong keywords and make it engaging.
Always provide exactly 5 title options in a numbered list format (1. 2. 3. 4. 5.)"""


def generate_title(topic: str) -> str:
    """Generate an engaging title for a given topic"""

    if not topic or not topic.strip():
        raise ValueError("Topic cannot be empty")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Create a catchy title for this topic :\n\n{topic}",
            },
        ],
        temperature=0.9,
    )

    return response.choices[0].message.content  # type: ignore


if __name__ == "__main__":
    example_topic = "AI in healthcare"

    try:
        print("=" * 50)
        print("TITLE GENERATION EXAMPLE")
        print("=" * 50)
        print(f"Topic: {example_topic}")
        print("-" * 50)

        result = generate_title(example_topic)

        print("\nGenerated Titles:")
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
