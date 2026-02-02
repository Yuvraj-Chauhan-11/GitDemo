import pytest

@pytest.mark.usefixtures("setup")
class TestExample:


    def test_fixtureDemo1(self):
        print("I ll be executing in fixture demo method 1")

    def test_fixtureDemo2(self):
        print("I ll be executing in fixture demo method 2")

    def test_fixtureDemo3(self):
        print("I ll be executing in fixture demo method 3")

    def test_fixtureDemo4(self):
        print("I ll be executing in fixture demo method 4")