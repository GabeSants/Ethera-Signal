import sys

from ui.menu import show_menu
from modules.tshark import run_tshark
from modules.nmap import run_nmap
from modules.kismet import run_kismet
from modules.history import show_history


def main():
    while True:
        show_menu()
        choice = input("ethera-signal > ").strip()

        if choice == "1":
            run_tshark()

        elif choice == "2":
            run_nmap()

        elif choice == "3":
            run_kismet()
        
        elif choice == "4":
            show_history()

        elif choice == "0":
            print("Encerrando Ethera Signal...")
            sys.exit(0)

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()