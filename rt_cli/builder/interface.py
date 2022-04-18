from SCons.Environment import Environment
def DefineGroup(env, name, src, depend, **parameters):
    print(f'Group name: {name}')

def generate(env:Environment):
    env.AddMethod(DefineGroup)
    