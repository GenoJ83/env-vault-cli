from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['init'])
    assert args.command == 'init'
