# test_parameterized_fixture.py
import pytest

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

@pytest.mark.parametrize('tester', input_dictionary, indirect=['tester'])
class TestIt:
    def test_tc1(self, tester):
       tester
       assert False
    
    def test_tc2(self, tester):
       tester
       assert False
    
    def test_tc3(self, tester):
       tester
       assert False
    
    def test_tc4(self, tester):
       tester
       assert False