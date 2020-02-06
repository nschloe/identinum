import identinum


def test_cli():
    identinum.cli.main(["{:f}".format(3.0 / 7.0)])
