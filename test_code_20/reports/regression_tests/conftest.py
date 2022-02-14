

import pytest




def pytest_addoption(parser):
    print('adoption is called------------------>')
    parser.addoption('--foo', action='store_true', help='Do foo')
    parser.addoption('--bar', action='store_false', help='Do not do bar')

@pytest.fixture(autouse=False)
def input_value():
    print('fixture is called------------------>')
    input = 39
    return input
