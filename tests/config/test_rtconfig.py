import imp
import pytest
import os
from tests.test_rt_cli import set_up
from rt_cli.config.rtconfig import init_rtconfig

def test_init_rtconfig(set_up):

    rtconfig = init_rtconfig()
