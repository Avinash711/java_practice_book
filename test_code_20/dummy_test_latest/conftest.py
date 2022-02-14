

import pytest, json

from mypack.deploy_call import ReturnIDStatus
def pytest_addoption(parser):
    print('adoption is called------------------>')
    parser.addoption('--env',required = True, action='store', help='Do foo')
    parser.addoption('--project',required=True, action='store', help='Do not do bar')
    parser.addoption('--source',required=True, action='store', help='Do not do bar')


@pytest.fixture(autouse=True, scope='class')
def ret_report(request):
    print('I m here----------------->')
    source = request.config.getoption("--source")
    print("source is -------------->", source)
    file_name = f"./files/new_test_{source}.json"
    print("file looking for, is -------------->", file_name)
    json_reports = {}
    with open(file_name) as data:
        json_reports = json.load(data)
    return json_reports['new_reports']

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
    source = request.config.getoption("--source")
    print("source is -------------->", source)

    return MyGlobal('abc/report.json',env, project, request.param).do_this()


