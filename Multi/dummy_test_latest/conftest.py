

import pytest, os

from mypack.deploy_call import ReturnIDStatus
def pytest_addoption(parser):
    print('adoption is called------------------>')
    parser.addoption('--env',required = True, action='store', help='Do foo')
    parser.addoption('--project',required=True, action='store', help='Do not do bar')
    parser.addoption('--uid',required=True, action='store', help='Do not do bar')


def pytest_configure(config):
    os.environ['report_identifier'] = config.getoption('--uid')

class MyGlobal:
    def __init__(self, file_path, env, project, input_dict):
        self.input_dict = input_dict
        self.file_path = file_path
        self.env = env
        self.project = project

    def do_this(self):
        depl_status = ReturnIDStatus(self.file_path,
                                self.env,
                                self.project,
                                self.input_dict).return_id_status()
        print("In do this---------------->")
        print(depl_status)
        return depl_status

@pytest.fixture(autouse=False, scope='class')
def input_value(request):
    print('fixture is called------------------>')
    env = request.config.getoption("--env")
    project = request.config.getoption("--project")
    print("00000000000000000000000000000000000000")
    print(request.param)
    return "fixture"


