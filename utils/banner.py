from colorama import Fore
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("Cyber Toolkit")
    print(Fore.GREEN + banner)
