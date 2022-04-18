from pytest import fixture
import os
from rt_cli import __version__


def test_version():
    assert __version__ == '0.1.0'

@fixture(scope='module', autouse=True)
def set_up():
    print(f'Start testing the module Builder ------------------->')

    os.chdir(r'C:\\Users\\Wcy34\\Documents\\Github\\RT-CLI\\tests\\RT-Thread\\stm32h750-artpi-h750\\')