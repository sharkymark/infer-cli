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

## API keys as environment variables
The following environment variables are required to be set in the user's environment:
- `GROQ_API_KEY`
- `HF_API_KEY`
- `OPENROUTER_API_KEY`
- `GEMINI_API_KEY`

## Installation

To install Infer CLI, clone the repository, create a virtual Python environment, and install the dependencies:

```bash
git clone https://github.com/yourusername/infer-cli.git
cd infer-cli
python -m venv venv_infer-cli
source venv_infer_cli/bin/activate
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

## egress api 

This project is experimenting with https://lunar.dev, an egress api server to manage and monitor API calls made from the CLI.

To remove the egress api, remove the following code:

`infer_cli.py`:
```python
import lunar_interceptor
```
`requirements.txt`:
```python
lunar-interceptor==0.1.0
```
`devcontainer.json`:
```json
"LUNAR_PROXY_HOST": "${localEnv:LUNAR_PROXY_HOST}"
```

## devcontainer

This project includes a `devcontainer.json` file for use with Visual Studio Code's Remote - Containers extension. To use this feature, install the extension, open the command palette, and select "Remote-Containers: Reopen in Container".

A Docker host must be running on the local machine for this feature to work.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.