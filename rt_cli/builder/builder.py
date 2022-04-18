from SCons.Environment import Environment
from SCons.Defaults import DefaultEnvironment
from .interface import generate
from ..config.rtconfig import RTconfig


def init_construct_env():
    rtconfig = RTconfig().config
    tools = rtconfig.get('toolchain')
    env = DefaultEnvironment(**tools)
    generate(env)
    return env








