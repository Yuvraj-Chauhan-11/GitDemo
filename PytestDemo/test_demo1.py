# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any Code should be wrapped in method only
# -k stands for method names exceution.
# -s means logs in output
# -v means more info or verbose or metadata.
# -m means mark the test case and can use to run only the marked test case.
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# @pytest.mark.skip --> to skip a test
# @pytest.mark.xfail --> if we want to run test cases(as it may be prerequsite to other test cases) but skip in report.
# fixtures are used as setup and tear down methods for test cases
# conftest file to genralise the fixture and mention the fixture to this file and give fixture method name as parameter to other test cases def function in all the file of the package whoever you want to apply fixture.
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it ll be run once before class is initiated and at the end
# pytest -xdist is the plug in i need to run the tests in parallel mode (pytest -n 4) --> means 4 workers will executes the tcs in 4 parallel mode

from selenium import webdriver
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_CreditTwoProgram(setup):
    print("Hello 2nd program")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])