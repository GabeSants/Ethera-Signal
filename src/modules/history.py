import json
import os
from datetime import datetime


HISTORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "captures",
    "history.json"
)


def save_history(tool, target):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    history = []

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)
        except (json.JSONDecodeError, OSError):
            history = []

    history.append({
        "tool": tool,
        "target": target,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("\nNenhum histórico encontrado.")
        input("\nPressione Enter para voltar...")
        return

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("\nNão foi possível ler o histórico.")
        input("\nPressione Enter para voltar...")
        return

    if not history:
        print("\nNenhum histórico encontrado.")
        input("\nPressione Enter para voltar...")
        return

    print("\n=== Capture History ===\n")

    for index, entry in enumerate(history, start=1):
        print(f"{index}. {entry['tool']}")
        print(f"   Alvo: {entry['target']}")
        print(f"   Data: {entry['date']}")
        print()

    input("Pressione Enter para voltar...")