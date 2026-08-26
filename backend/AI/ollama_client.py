import json
import httpx

from ollama import chat


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"


def ask_ollama(message: str):
    response = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
            "stream": False
        },
        timeout=120.0
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]


def run_tool_chat(message: str, tool_registry: dict):
    messages = [
        {
            "role": "system",
            "content": (
                "Si Restaurant Assistant systému Smart Restaurant AI. "
                "Na získanie údajov používaj dostupné nástroje. "
                "Nevymýšľaj si údaje, ktoré nástroje neposkytli. "
                "Odpovedaj používateľovi po slovensky."
            )
        },
        {
            "role": "user",
            "content": message
        }
    ]

    tools = list(tool_registry.values())

    for _ in range(5):
        response = chat(
            model=MODEL,
            messages=messages,
            tools=tools
        )

        messages.append(response.message)

        if not response.message.tool_calls:
            return (
                response.message.content
                or "Nepodarilo sa vytvoriť odpoveď."
            )

        for tool_call in response.message.tool_calls:
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            function_to_call = tool_registry.get(tool_name)

            if function_to_call is None:
                result = {
                    "error": f"Nástroj {tool_name} neexistuje."
                }
            else:
                try:
                    result = function_to_call(**arguments)
                except Exception as error:
                    result = {
                        "error": str(error)
                    }

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": json.dumps(
                        result,
                        ensure_ascii=False,
                        default=str
                    )
                }
            )

    return "Požiadavku sa nepodarilo dokončiť."