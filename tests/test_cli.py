import cli


def test_cli_exists():
    assert hasattr(cli, "main_loop")