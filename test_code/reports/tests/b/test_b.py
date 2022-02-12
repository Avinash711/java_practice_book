import pytest

@pytest.mark.cat_2
class TestXyz:
    @pytest.mark.a
    def test_b(self):
        assert True