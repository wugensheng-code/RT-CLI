from typing import Dict
from tomlkit.toml_file import TOMLFile
from ..utilities.singleton import Singleton

TOOLS = ['CC', 'AS', 'AR', 'CXX', 'LINK', 'SIZE', 'OBJDUMP', 'OBJCPY']

        
def init_rtconfig() -> Dict:
    
    f = TOMLFile('rtthread.toml')
    rtconfig = f.read().value
    return rtconfig






