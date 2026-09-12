import subprocess


def run_nmap():
    target = input("Target: ").strip()

    if not target:
        print("No target specified.")
        return

    print(f"\nStarting Nmap scan against {target}...\n")

    try:
        subprocess.run(
            ["nmap", target],
            check=True
        )

        input("\nPress Enter to return to the menu...")

    except FileNotFoundError:
        print("Error: Nmap is not installed or not available in PATH.")

    except KeyboardInterrupt:
        print("\nScan interrupted.")

    except subprocess.CalledProcessError as error:
        print(f"Error executing Nmap: {error}")