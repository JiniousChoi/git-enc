#!/usr/bin/env python3
## author: jinchoiseoul@gmail.com
## usage: use this tool to easily encrypt/decrypt credential files for github repository or any kind of public storage.


import yaml
import os, sys, argparse
from getpass import getpass
from subprocess import run


GITENCRYPT = ".gitencrypt"
GITENCPASSWORD = "GITENCPASSWORD"


def main():
    args = parse_args()
    if not args.cmd:
        print("usage: {} -h".format(sys.args[0]))
        return 1

    ydict = yaml.load(open(GITENCRYPT))

    if args.cmd == 'encrypt':
        cmd_encrypt(ydict, args.password, args.paths)
    elif args.cmd == 'decrypt':
        cmd_decrypt(ydict, args.password, args.paths)
    else:
        assert("cannot reach here")


def parse_args():
    usage = "usage: %prog [options] arg1 arg2"
    parser = argparse.ArgumentParser(\
             description='a utility tool for encrypting/decrypting confidential files.')
    subparsers = parser.add_subparsers(title='available commands', dest='cmd')
    add_encrypt_parser(subparsers)
    add_decrypt_parser(subparsers)
    # TODO
    # addListParser(subparsers)     
    # addVerifyParser(subparsers)
    return parser.parse_args()


def cmd_encrypt(ydict, password, paths):
    password = get_password(password)
    for path in paths:
        for s,d in find_kvs_at(ydict, path):
            run(['openssl', 'aes-256-cbc', '-k', password, '-in', s, '-out', d])


def cmd_decrypt(ydict, password, paths):
    password = get_password(password)
    for path in paths:
        for s,d in find_kvs_at(ydict, path):
            run(['openssl', 'aes-256-cbc', '-d', '-k', password, '-in', d, '-out', s])


def add_encrypt_parser(subparsers):
    cmd = subparsers.add_parser('encrypt', help='encrypt files')
    cmd.add_argument('-k', '--password', help='password for encrypt files')
    cmd.add_argument('paths', nargs='*', help='a list of targeting groups to encrypt.')


def add_decrypt_parser(subparsers):
    cmd = subparsers.add_parser('decrypt', help='decrypt files')
    cmd.add_argument('-k', '--password', help='password for decrypt files')
    cmd.add_argument('paths', nargs='*', help='a list of targeting groups to decrypt.')


def get_password(password):
    if password:
        return password
    if GITENCPASSWORD in os.environ:
        return os.environ[GITENCPASSWORD]
    return getpass("type password: ")


def find_kvs_at(ydict, path):
    def find_kvs(k, v):
        if type(v) is str:
            yield (k, v)
            return
        for k2, v2 in v.items():
            yield from find_kvs(k2, v2)
    sep = '.'
    ks = path.split(sep)
    it = ydict
    for k in ks:
        it = it[k]
    return find_kvs(k, it)


if __name__ == "__main__":
    main()
