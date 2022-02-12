import pytest
from time import sleep
from time import gmtime, strftime




class TestParallelism:
    def test_a(self):
        delay = 10
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(delay)
        assert True
    
    def test_b(self):
        delay = 20
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    
    def test_c(self):
        delay = 20
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

class TestParallelism2:
    def test_a2(self):
        delay = 10
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(delay)
        assert True
    
    def test_b2(self):
        delay = 20
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    
    def test_c2(self):
        delay = 20
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


