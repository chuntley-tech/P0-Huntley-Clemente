from mcoc.cli import main


def test_main_ok(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert "funcionando" in captured.out


def test_main_help(capsys):
    assert main(["--help"]) == 0
    captured = capsys.readouterr()
    assert "Uso" in captured.out
