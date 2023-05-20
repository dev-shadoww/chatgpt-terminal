import os
import openai
import requests
import json
from dotenv import load_dotenv

from rich.console import Console
from rich.panel import Panel

load_dotenv()

console = Console(record=True)
openai.api_key = os.getenv("OPEN_AI_API_KEY")
api_url = "https://api.openai.com/v1/chat/completions"
api_headers = {"Authorization": f"Bearer {openai.api_key}"}

console.print(
    Panel.fit("[bold red]ChatGPT, On Terminal[/bold red]", title_align="center"))
console.print("Enter your query below, to quit enter [red]\"exit\",")

while True:
    user_query = console.input("[bold green]User   [/bold green]: ")
    if (user_query.lower() == "exit"):
        break

    request_object = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{user_query}"}]
    }

    response = requests.post(
        api_url, json=request_object, headers=api_headers)
    response_object = json.loads(response.text)
    console.print("[bold blue]ChatGPT[/bold blue]: ", end='')
    console.print(response_object["choices"][0]
                  ["message"]["content"], soft_wrap=True)
    console.print()

export_text_file = console.input(
    "Do you want to export your conversation into a file? [bold green](Y or N)[/bold green]: ")
if (export_text_file.lower() == 'y'):
    with open("conversation.txt", 'w') as file:
        file.write(console.export_text(clear=True))
