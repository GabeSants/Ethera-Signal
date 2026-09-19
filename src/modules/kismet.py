import platform
import subprocess

from modules.history import save_history


def run_kismet():
    system = platform.system()

    interface = input("Interface wireless: ").strip()

    if not interface:
        print("Erro: nenhuma interface wireless foi informada.")
        return
    
    save_history("Kismet", f"Interface {interface}")

    try:
        if system == "Linux":
            subprocess.run(
                ["kismet", "-c", interface],
                check=True
            )

        elif system == "Windows":
            subprocess.run(
                ["wsl", "-d", "kali-linux", "kismet", "-c", interface],
                check=True
            )

        else:
            print(f"Sistema operacional não suportado: {system}")
            return

        input("\nPress Enter to return to the menu...")

    except FileNotFoundError:
        print("Erro: Kismet ou WSL não está disponível.")

    except KeyboardInterrupt:
        print("\nKismet interrompido.")

    except subprocess.CalledProcessError:
        print(
            f"Erro: não foi possível iniciar o Kismet "
            f"com a interface '{interface}'."
        )