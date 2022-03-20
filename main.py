import argparse
import socket
import sys
import os
from win32com.client import Dispatch

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_version():
    parser = Dispatch("Scripting.FileSystemObject")
    version = parser.GetFileVersion(sys.argv[0])
    return version

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='hntoip', usage='%(prog)s [options]', description='Show IP of website (URL)')

    parser.add_argument('-V', '--version', action='version', version=f'IP From Website {get_version()}-beta.2')
    parser.add_argument('-m', '--module', action='store_true', help='\
        use as a helper program to pipe output to another program. \
        PowerShell syntax: \
        \'echo [yourdomain.net] | hntoip | [your program that waits for input]\'\
    ')
    parser.add_argument('-C', '--clear', action='store_true', help='\
        clear terminal before launch\
    ')

    return parser

def get_ip_by_hostname(hostname: str) -> str:
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as error:
        return f'{bcolors.FAIL}[!] Invalid Hostname - {error}{bcolors.ENDC}'
    except socket.timeout as error:
        return f'{bcolors.FAIL}[!] Invalid Hostname - {error}{bcolors.ENDC}'

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.module:
        print( get_ip_by_hostname( input() ) )
    else:
        if namespace.clear:
            os.system('cls' if os.name in ('nt', 'dos') else '')
        
        hostname = input(f'{bcolors.BOLD}{bcolors.HEADER}Enter your website address (URL): {bcolors.ENDC}')
        print(f'{bcolors.OKCYAN}{hostname}{bcolors.ENDC}: {bcolors.OKGREEN}{bcolors.BOLD}{get_ip_by_hostname(hostname)}{bcolors.ENDC}')

if __name__ == "__main__":
    main()
