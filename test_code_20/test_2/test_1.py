import pytest
example_params = [1, 2, 3]

@pytest.fixture(params=example_params)
def param_loop(request):
    return request.param

class TestClass:
    def test_something1(self, param_loop):
        print(param_loop)
    def test_something2(self, param_loop):
        print(param_loop)