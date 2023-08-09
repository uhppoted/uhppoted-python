#!python3

import argparse
import sys
import traceback

from trace import Trace
from commands import commands
from commands import exec


def main():
    if len(sys.argv) < 2:
        usage()
        return -1

    parser = argparse.ArgumentParser(description='uhppoted-codegen example')

    parser.add_argument('command', type=str, help='command')

    parser.add_argument('--bind',
                        type=str,
                        default='0.0.0.0',
                        help='UDP IPv4 bind address. Defaults to 0.0.0.0:0')

    parser.add_argument(
        '--broadcast',
        type=str,
        default='255.255.255.255:60000',
        help='UDP IPv4 broadcast address. Defaults to 255.255.255.255:60000')

    parser.add_argument(
        '--listen',
        type=str,
        default='0.0.0.0:60001',
        help='UDP IPv4 event listener bind address. Defaults to 0.0.0.0:60001')

    parser.add_argument('--debug',
                        action=argparse.BooleanOptionalAction,
                        default=False,
                        help='displays sent and received UDP packets')

    args = parser.parse_args()
    cmd = args.command
    bind = args.bind
    broadcast = args.broadcast
    listen = args.listen
    debug = args.debug

    if cmd == 'all':
        for c, fn in commands().items():
            if c != 'listen':
                try:
                    exec(fn, bind, broadcast, listen, debug)
                except Exception as x:
                    print()
                    print(f'*** ERROR  {cmd}: {x}')
                    print()
    elif cmd in commands():
        try:
            exec(commands()[cmd], bind, broadcast, listen, debug)
        except Exception as x:
            print()
            print(f'*** ERROR  {cmd}: {x}')
            print()
            if debug:
                print(traceback.format_exc())

            sys.exit(1)
    else:
        print()
        print(f'  ERROR: invalid command ({cmd})')
        print()


def usage():
    print()
    print('  Usage: python3 main.py <command>')
    print()
    print('  Supported commands:')

    for cmd, _ in commands().items():
        print(f'    {cmd}')

    print()


if __name__ == '__main__':
    main()
