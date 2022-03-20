import argparse
import socket
import sys
import os

VERSION = 1, '1.0dev0.1'

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


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='hntoip', usage='%(prog)s [options]', description='Show IP of website (URL)')

    parser.add_argument('-V', '--version', action='version', version=f'IP From Website {VERSION[1]}')
    parser.add_argument('-m', '--module', action='store_true', help='\
        use as a helper program to pipe output to another program. \
        PowerShell syntax: \
        \'echo [your hostname (google.com)] | hntoip | [your program that waits for input]\'\
    ')
    parser.add_argument('-C', '--clear', action='store_true', help='\
        clear terminal before launch\
    ')

    return parser

def get_ip_by_hostname(hostname: str) -> str:
    return socket.gethostbyname(hostname)

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