# test_parameterized_fixture.py
import pytest, os
from looup import ReturnEntry

# category 1 reports
input_dictionary = ReturnEntry(os.environ['report_identifier']).ret_data()
print("Avinashshshsh=================")
print(input_dictionary)
@pytest.mark.parametrize('input_value', [input_dictionary], indirect=['input_value'], 
                         ids=[input_dictionary['report_name']])
class TestDeploy(object):
    def test_status(self, input_value):
        assert True
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
    
