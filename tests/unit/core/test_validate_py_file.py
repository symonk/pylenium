from pylenium import is_py_file
from pytest import raises
from pytest import UsageError


def test_invalid_file_without_py():
    with raises(UsageError) as ex:
        assert is_py_file("notapyfile")
    assert ex.value.args[0] == "File path provided: notapyfile was not a .py file"


def test_invalid_file():
    with raises(UsageError) as ex:
        assert is_py_file("isapyfilebutnotreal.py")
    assert (
        ex.value.args[0]
        == "Pylenium was unable to find the file provided at: isapyfilebutnotreal.py"
    )
