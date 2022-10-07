#!/usr/bin/env python3
from pwn import *

{bindings}

context.binary = {bin_name}


def conn():
    if args.REMOTE:
        r = remote('127.0.0.1', 1337)
    else:
        r = process({proc_args})
        if args.DEBUG:
            gdb.attach(r)
    return r


def main():
    io = conn()
    # good luck pwning :)

    io.interactive()


if __name__ == "__main__":
    main()