

import unittest
import pytest
from time import sleep
from time import gmtime, strftime

class TestCategoryOne(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.result = {
            "status": ['Success'],
            "status_code":[200],
            "BQ": ["pass"]
        }
        delay = 20
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(delay)

    def test_a(self):
        
        status = self.result['status'][0]
        print(f"status is {status}")
        assert status == 'Success'
    
    def test_b(self):
        status_code = self.result['status_code'][0]
        print(f"status is {status_code}")
        assert status_code == 200
    
    def test_c(self):
        bq = self.result['BQ'][0]
        print(f"status is {bq}")
        assert bq == 'pass'


class TestCategoryTwo(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.result = {
            "status": ['Success'],
            "status_code":[200],
            "BQ": ["pass"]
        }
        delay = 30
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(delay)

    def test_a_2(self):
        
        status = self.result['status'][0]
        print(f"status is {status}")
        assert status == 'Success'
    
    def test_b_2(self):
        status_code = self.result['status_code'][0]
        print(f"status is {status_code}")
        assert status_code == 200
    
    def test_c_2(self):
        bq = self.result['BQ'][0]
        print(f"status is {bq}")
        assert bq == 'pass'


