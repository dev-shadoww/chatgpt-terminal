import openai
import requests
from rich.prompt import Prompt as rich_input
from rich import print as rich_print
from rich.panel import Panel

from rich.prompt import Prompt

rich_print(Panel.fit("ChatGPT, On Terminal", title_align="center"))

rich_print("Enter your query below, to quit enter [red]\"exit\",")

openai.api_key = "OPENAI_API_KEY"
open_ai_api_url = "https://api.openai.com/v1/chat/completions"
open_ai_headers_object = {"Authorization": f"Bearer {openai.api_key}"}

while True:
    user_query = rich_input.ask("[bold green]User   [/bold green]")
    if (user_query.lower() == "exit"):
        break
    open_ai_request_object = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{user_query}"}]
    }
    open_ai_response = requests.post(
        open_ai_api_url, json=open_ai_request_object, headers=open_ai_headers_object)
    open_ai_response_object = open_ai_response.text
    rich_print("[bold blue]ChatGPT[/bold blue]: ", end='')
    rich_print(open_ai_response_object["choices"][0]["message"]["content"])
    rich_print()
