import pytest
from time import sleep
from time import gmtime, strftime



@pytest.mark.parametrize('count', [1,2])
class TestParallelism():
    @pytest.mark.order(1)
    def test_a(self, count):
        delay = 3
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(delay)
        assert True
    @pytest.mark.order(2)
    def test_b(self, count):
        delay = 3
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    @pytest.mark.order(3)
    def test_c(self, count):
        delay = 5
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''
class TestParallelism2:
    def test_a2(self):
        delay = 2
        print(f"\nstarted-waiting for {delay} seconds-->")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        sleep(delay)
        assert True
    
    def test_b2(self):
        delay = 4
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    
    def test_c2(self):
        delay = 5
        print(f"\nstarted-waiting for {delay} seconds-->")
        sleep(delay)
        assert True
        print("Ended at: ")
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''
