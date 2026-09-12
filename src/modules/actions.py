import subprocess


def run_tshark():
    capture_file = input("Arquivo de captura (.pcap/.pcapng): ").strip()

    if not capture_file:
        print("Nenhum arquivo informado.")
        return

    try:
        subprocess.run(
            ["tshark", "-r", capture_file],
            check=True
        )

    except FileNotFoundError:
        print("Erro: TShark não está instalado ou não está no PATH.")

    except subprocess.CalledProcessError as error:
        print(f"Erro ao executar o TShark: {error}")