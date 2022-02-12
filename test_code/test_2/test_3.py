


import unittest
import pytest
from time import sleep
from time import gmtime, strftime



'''
to reduce number of threads using -n 
added the nested mehtods for status, gcs, bq, adls validation in one mehtod
'''
class TestCategoryOne(unittest.TestCase):

    @classmethod
    def setUp(cls):
        delay = 5
        sleep(delay)
        cls.result = {
            "status": ['Success'],
            "status_code":[200],
            "gcs":['pass'],
            "BQ": ["pass"]
        }
        
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
       

    def test_report_abc(self):
        def status_validation():
            status = self.result['status'][0]
            print(f"status is {status}")
            sleep(2)
            assert status == 'Success'

        def status_code_validation():
            status_code = self.result['status_code'][0]
            print(f"status is {status_code}")
            sleep(2)
            assert status_code == 200
        
        def gcs_validation():
            gcs = self.result['gcs'][0]
            sleep(2)
            assert gcs == 'pass'

        
        def bq_validation():
            bq = self.result['BQ'][0]
            print(f"status is {bq}")
            sleep(2)
            assert bq == 'pass'
        
        status_validation()
        status_code_validation()
        gcs_validation()
        bq_validation()


class TestCategoryTwo(unittest.TestCase):

    @classmethod
    def setUp(cls):
        delay = 5
        sleep(delay)
        cls.result = {
            "status": ['Success'],
            "status_code":[200],
            "gcs":['pass'],
            "BQ": ["pass"]
        }
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    def test_report_xyz(self):
        def status_validation():
            status = self.result['status'][0]
            print(f"status is {status}")
            sleep(2)
            assert status == 'Success'

        def status_code_validation():
            status_code = self.result['status_code'][0]
            print(f"status is {status_code}")
            sleep(2)
            assert status_code == 200
        
        def gcs_validation():
            gcs = self.result['gcs'][0]
            sleep(2)
            assert gcs == 'pass'

        
        def bq_validation():
            bq = self.result['BQ'][0]
            print(f"status is {bq}")
            sleep(2)
            assert bq == 'pass'
        
        status_validation()
        status_code_validation()
        gcs_validation()
        bq_validation()