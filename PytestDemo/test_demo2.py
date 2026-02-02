import pytest


@pytest.mark.smoke
def test_thirdProgram(dataLoad):
    msgw = "Hello 2nd program"
    print(dataLoad)
    assert msgw == "Hello 2nd program", "test case failed"

def test_CreditProgram(setup):
    a=4
    b=10
    assert a*2.5 == b,  "test case failed"


