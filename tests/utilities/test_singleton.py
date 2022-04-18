from pytest import raises
from pytest import fixture
from rt_cli.utilities.singleton import Singleton

class Test_singleton(object, metaclass=Singleton):
    pass
    
@fixture
def instantiate1():
    return Test_singleton()

@fixture
def instantiate2():
    return Test_singleton()

def test_singleton(instantiate1, instantiate2):
    assert instantiate1 is instantiate2