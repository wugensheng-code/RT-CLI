import pytest
import os
from tests.test_rt_cli import set_up
# from rt_cli.builder.builder import RTenv
from rt_cli.builder.builder import init_construct_env

def test_added_method(set_up):
    env = init_construct_env()
    src = None
    env.DefineGroup('Finsh', src, depend = ['RT_USING_FINSH'])
    pass