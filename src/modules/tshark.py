import subprocess

from modules.history import save_history


def run_tshark():
    try:
        result = subprocess.run(
            ["tshark", "-D"],
            capture_output=True,
            text=True,
            check=True
        )

        print("\nInterfaces disponíveis:\n")
        print(result.stdout)

        interface = input("Selecione o número da interface: ").strip()

        if not interface:
            print("Nenhuma interface selecionada.")
            return
         
        save_history("TShark", f"Interface {interface}")

        print(f"\nIniciando captura na interface {interface}...")
        print("Pressione Ctrl+C para interromper.\n")

        subprocess.run(
            ["tshark", "-i", interface],
            check=True
        )

    except FileNotFoundError:
        print("Erro: TShark não está instalado ou não está no PATH.")

    except KeyboardInterrupt:
        print("\nCaptura interrompida.")

    except subprocess.CalledProcessError as error:
        print(f"Erro ao executar o TShark: {error}")