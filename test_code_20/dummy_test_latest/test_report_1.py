# test_parameterized_fixture.py
import pytest
from pytest_lazyfixture import lazy_fixture
from read_json_content import ReadJson

json_reports = ReadJson().ret_report()

@pytest.mark.parametrize('input_value', json_reports, indirect=['input_value'],
                        ids=[i['report_name']+"_"+i['source'] for i in json_reports])
class TestDeploy(object):
    def test_stat(self, input_value):
        depl_status = input_value
        print('\n')
        print('*'*10)
        print(depl_status)
        assert True
    def test_id(self, input_value):
        depl_status = input_value
        print('\n')
        print('*'*10)
        print(depl_status)
        assert True
