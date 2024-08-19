from memory import Memory as mem
import opcodes as op

REGISTER_COUNT = 16

class CPU:
    def __int__(self):
        self.mem_stack = [0] * 16
        self.memory = mem()
        self.data_registers = [0] * REGISTER_COUNT
        self.I = 0
        self.sp = 0
        self.pc = 0x200
        return
    def read_instruction(self,address:int):
        return
    def goto_next_instruction(self):
        self.pc += 2
    def skip_next_instruction(self):
        self.pc += 4
