import pytest

@pytest.mark.cat_1
class TestData:
    @pytest.mark.c
    def test_good_data(self):
        assert True
    
    @pytest.mark.a
    def test_good_data_2(self):
        assert True