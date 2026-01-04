# Creative Assistant

An AI-powered text processing tool that provides text summarization, title generation, and intelligent question-answering capabilities.

## Features

- **Text Summarization**: Generate concise summaries while preserving key information
- **Title Generation**: Create 5 catchy and relevant titles for any topic
- **Q&A Assistant**: Interactive chat with conversation memory and optional context support

## Tech Stack

- Python 3.11+
- OpenAI SDK
- OpenRouter API (Gemini 2.0 Flash)
- Pytest for testing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mo-sharifi/creative_assistant.git
cd creative_assistant
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory:
```env
API_KEY=your_openrouter_api_key_here
```
## Usage
```bash
python run.py
```
### Use individual modules
#### Summarize text :
```python
from app.summarizer import summarize

text = "Your long text here..."
summary = summarize(text)
print(summary)
```
#### Generate titles :
```python
from app.title_generator import generate_title

titles = generate_title("AI in healthcare")
print(titles)
```
#### Q&A with memory :
```python
from app.qa_assistant import QAAssistant

assistant = QAAssistant()
answer1 = assistant.ask("What is Python?")
answer2 = assistant.ask("What are its main features?")
```
## Project Structure
```text
creative_assistant/
├── app/
│   ├── __init__.py
│   ├── config.py           # API configuration
│   ├── summarizer.py       # Text summarization
│   ├── title_generator.py  # Title generation
│   ├── qa_assistant.py     # Q&A with memory
│   └── main.py             # CLI interface
├── tests/
│   ├── __init__.py
│   ├── test_summarizer.py
│   ├── test_title_generator.py
│   └── test_qa_assistant.py
├── .env                    # API key (not in repo)
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```
## Testing
### Run tests
```bash
pytest tests/ -v
```
## License
MIT license - see [LICENSE](./LICENSE) file for details
## Author
- Mohammadreza Sharifi
## Acknowledgments
- Uses OpenRouter API for LLM access
