import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='env-vault')
    sub = p.add_subparsers(dest='command')
    sub.add_parser('init')
    sub.add_parser('encrypt')
    sub.add_parser('decrypt')
    return p
