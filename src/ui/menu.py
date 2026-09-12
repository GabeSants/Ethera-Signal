from ui.colors import *
from ui.art import ETHERA_ART
from utils.helpers import clear_screen

def draw_header():
    clear_screen()
    print(RED + ETHERA_ART + RESET)
    print(f"{CYAN}{BOLD}============================================================================================={RESET}")
    print(f"{YELLOW}{BOLD}                                       Developed by zxgabr {RESET}")
    print(f"{CYAN}{BOLD}============================================================================================={RESET}\n")

def show_menu():
    draw_header()

    print(" [1] TShark - Packet Capture")
    print(" [2] Nmap - Network Scan")
    print(" [3] Kismet - Wireless Analysis")
    print(" [4] Capture History")
    print(" [0] Exit\n")