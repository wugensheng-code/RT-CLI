from SCons.Environment import Environment
from SCons.Defaults import DefaultEnvironment
from .interface import generate
from ..config.rtconfig import init_rtconfig


def init_construct_env():
    rtconfig = init_rtconfig()
    tools = rtconfig.get('toolchain')
    env = DefaultEnvironment(**tools)
    generate(env)
    return env








