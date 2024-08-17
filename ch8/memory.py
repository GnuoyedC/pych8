MEMORY_SIZE = 4096
PROGRAM_BEGIN = 0x200
INTERPRETER_END = 0x1FFF
INTERPRETER_BEGIN = 0x000

class Memory:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.program_space = self.memory[PROGRAM_BEGIN]

    def valid_mem_addr(self,address):
        return 0 <= address < MEMORY_SIZE

    def load_program(self,program:list) -> None:
        if program is not None:
            for i in range(len(program)):
                self.memory[PROGRAM_BEGIN + i] = program[i]
    
    def write_bytes(self,address,value):
        if self.valid_mem_addr(address):
            self.memory[address] = value

    def read_bytes(self,address):
        if self.valid_mem_addr(address):
            return self.memory[address]
