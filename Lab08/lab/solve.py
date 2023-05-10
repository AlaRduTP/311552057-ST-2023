import sys

import angr
import claripy

main_addr = 0x4011a9
find_addr = 0x401371
avoid_addr = 0x40134d

def handle_fgets_real_input(raw_input):
    idx = 0
    for c in raw_input:
        if c == ord('\n') or c == ord('\0'):
            break
        idx += 1
    return raw_input[:idx]

proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})

class MyScanf(angr.SimProcedure):
    def run(self, fmt, x):
        xparam = claripy.BVS('xparam', 32)
        self.state.memory.store(x, xparam, endness=proj.arch.memory_endness)
        if not self.state.globals.get('xs'):
            self.state.globals['xs'] = []
        self.state.globals['xs'].append(xparam)

proj.hook_symbol('__isoc99_scanf', MyScanf())

state = proj.factory.blank_state(addr=main_addr)

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=find_addr, avoid=avoid_addr)
if simgr.found:
    sol = simgr.found[0]
    xs = '\n'.join(map(str, map(sol.solver.eval, sol.globals['xs'])))
    print(xs, file=open('solve_input', 'w'))
    print('Success')
else:
    print('Failed')
