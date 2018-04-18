from argparse import ArgumentDefaultsHelpFormatter
import random

PW_LEN = 64
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def gen_parser(sub):
    d = 'Generate a password suitable for use by a sbws scanner for '\
        'authenticating to an sbws server.'
    p = sub.add_parser('pwgen', formatter_class=ArgumentDefaultsHelpFormatter,
                       description=d)
    p.add_argument('--output', type=str, help='Where to write the password')


def rand_char():
    return rng.choice(ALPHABET)


def rand_str():
    s = ''
    while len(s) < PW_LEN:
        s += rand_char()
    assert len(s) == PW_LEN
    return s


def main(args, conf):
    global rng
    rng = random.SystemRandom()
    if args.output:
        with open(args.output, 'wt') as fd:
            fd.write(rand_str() + '\n')
    else:
        print(rand_str())