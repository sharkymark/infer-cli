# Infer CLI

Infer CLI is a command-line tool that lets the user choose a large language model and ask it questions using Python. 

## Features

- **Model Agnostic**: Use any large language model (e.g., GPT-4o, Meta Llama, etc).
- **Leverage AI routers**: Use cloud-based AI routers to access the models.
- **Python CLIs**: Use Python packages from LLM providers to access the models.
- **AI routers supported**: Using AI routers like Groq, Hugging Face, OpenRouter
- **Native LLM support**: Use native LLMs like Google Gemini

## User flow
- User runs the CLI
- User selects the AI router
- User selects the model e.g., OpenAI GPT-4o
- User asks a question
- The CLI sends the question to the AI router
- The AI router sends the question to the model
- The model generates an answer
- The answer is displayed to the user

## Installation

To install Infer CLI, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/infer-cli.git
cd infer-cli
pip install -r requirements.txt
```

## Usage

To use Infer CLI, run the following command:

```bash
python infer_cli.py 
```
### Examples

Infer data from a JSON file:

```bash
python infer_cli.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.