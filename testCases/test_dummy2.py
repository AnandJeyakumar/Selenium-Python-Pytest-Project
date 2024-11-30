import pytest


def test_firstProgram():
    msg = "Hello"
    assert msg=="Hai","Test failed because of Strings does not match"
    print("Om Namashivaya")
@pytest.mark.framework
def testsecondProgramCredit():
    a=4
    b=6
    assert a+2 ==6 ,"Addition do not match"