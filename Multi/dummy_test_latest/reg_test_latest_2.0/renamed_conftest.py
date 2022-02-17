import pytest

from mypack.deploy_call import ReturnIDStatus
def pytest_addoption(parser):
    print('adoption is called------------------>')
    parser.addoption('--env',required = True, action='store', help='Do foo')
    parser.addoption('--project',required=True, action='store', help='Do not do bar')



class MyTester:
    def __init__(self, x):
        self.x = x

    def dothis(self):
        assert self.x

@pytest.fixture(autouse=False, scope='class')
def tester(request):
    """Create tester object"""
    print('fixture is called------------------>')
    env = request.config.getoption("--env")
    project = request.config.getoption("--project")
    print('env: --->', env)
    print('project: --->', project)
    print('request param:--->', request.param)
    return MyTester(request.param).dothis()

