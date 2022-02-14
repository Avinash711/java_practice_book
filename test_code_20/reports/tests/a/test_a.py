import pytest

@pytest.mark.cat_1
class TestAbcd:
    @pytest.mark.a
    def test_a(self):
        assert True
