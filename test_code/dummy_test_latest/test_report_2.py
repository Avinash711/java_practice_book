# test_parameterized_fixture.py
import pytest


# category 2 reports
input_dictionary = [
    {
        "report_name": "SAP",
        "version": "3.0.0"
    },
    {
        "report_name": "SAP",
        "version": "3.0.0"

    }
]

@pytest.mark.parametrize('input_value', input_dictionary, indirect=['input_value'])
class TestDeploy2(object):
    def test_stat2(self, input_value):
        depl_status = input_value
        print('\n')
        print('*'*10)
        print(depl_status)
        assert False
    def test_id2(self, input_value):
        depl_status = input_value
        print('\n')
        print('*'*10)
        print(depl_status)
        assert False
