from memory import Memory as mem
from opcodes import OpCodes as opcodes 

REGISTER_COUNT = 16

class CPU:
    def __int__(self):
        self.mem_stack = [0] * 12
        self.memory = mem()
        self.data_registers = [0] * REGISTER_COUNT
        self.index_register = 0
        self.sp = 0
        self.pc = 0x200
        return
    
