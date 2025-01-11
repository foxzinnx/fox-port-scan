import socket
from colorama import Fore, Style, init
import argparse

init(autoreset=True)

def main_menu():
    banner = f"""{Fore.RED}
 _____ _____  __  ____   ___  ____ _____   ____   ____    _    _   _ 
|  ___/ _ \ \/ / |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | |
| |_ | | | \  /  | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |
|  _|| |_| /  \  |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  |
|_|   \___/_/\_\ |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|
                
                    {Fore.CYAN}github.com/foxzinnx                           """
    print(banner)


def scan(ip, output_file=None):
    results = []
    print(f"\n{Fore.CYAN}Scanning target: {ip}")
    for ports in range(1, 65):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            connect = s.connect_ex((ip, ports))
            if connect == 0:
                msg = f"Port: {ports} State: Open"
                print(f"{Fore.YELLOW}Port: {Fore.LIGHTMAGENTA_EX}{ports} {Fore.YELLOW}State: {Fore.GREEN}Open")
                results.append(msg)
            s.close()
        except Exception as e:
            print(f"{Fore.RED}Error scanning port {ports}: {e}")

    if results:
        print(f"\n{Fore.GREEN}Scan complete. Open ports found:")
        for r in results:
            print(f" - {r}")
    else:
        print(f"\n{Fore.RED}No open ports found on {ip} in the specified range.")

    if output_file:
        with open(output_file, "w") as f:
            f.write(f"Scan results for {ip}:\n")
            f.write("\n".join(results))
        print(f"\n{Fore.GREEN}Results saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description=f"{Fore.RED}FOX - PORT SCAN")
    parser.add_argument("-i", "--ip", required=True, help=f"{Style.BRIGHT}IP Target")
    parser.add_argument("-o", "--output", required=False, help=f"{Style.BRIGHT}Save results to a file")

    args = parser.parse_args()
    ip = args.ip
    output_file = args.output

    main_menu()
    scan(ip, output_file)


if __name__ == "__main__":
    main()
