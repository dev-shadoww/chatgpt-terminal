# By Suraj Kareppagol
# GitHub : https://github.com/dev-shadoww

# Use your own API key to use this program.
# Other packages used are, openai, rich (for styling the terminal), json

import openai
import requests
from rich.prompt import Prompt as rich_input
from rich import print as rich_print
from rich.panel import Panel
import json

from rich.prompt import Prompt

rich_print(Panel.fit("ChatGPT, On Terminal", title_align="center"))

rich_print("Enter your query below, to quit enter [red]\"exit\",")

openai.api_key = "OPEN_AI_KEY"
api_url = "https://api.openai.com/v1/chat/completions"
headers_object = {"Authorization": f"Bearer {openai.api_key}"}

while True:
    user_query = rich_input.ask("[bold green]User   [/bold green]")
    if (user_query.lower() == "exit"):
        break

    request_object = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{user_query}"}]
    }

    response = requests.post(
        api_url, json=request_object, headers=headers_object)
    response_object = json.loads(response.text)
    rich_print("[bold blue]ChatGPT[/bold blue]: ", end='')
    rich_print(response_object["choices"][0]["message"]["content"])
    rich_print()
