import platform
import subprocess


def run_kismet():
    system = platform.system()

    try:
        if system == "Linux":
            subprocess.run(
                ["kismet"],
                check=True
            )

        elif system == "Windows":
            subprocess.run(
                ["wsl", "-d", "kali-linux", "kismet"],
                check=True
            )

        else:
            print(f"Sistema operacional não suportado: {system}")
            return

        input("\nPress Enter to return to the menu...")

    except FileNotFoundError:
        print("Error: Kismet ou WSL não está disponível.")

    except KeyboardInterrupt:
        print("\nKismet interrupted.")

    except subprocess.CalledProcessError as error:
        print(f"Error executing Kismet: {error}")