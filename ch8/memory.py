MEMORY_SIZE = 4096
PROGRAM_BEGIN = 0x200
INTERPRETER_END = 0x1FFF
INTERPRETER_BEGIN = 0x000

class Memory:
    def __init__(self):
        self.memory = [0 for _ in range(MEMORY_SIZE)]
        self.program_space = self.memory[PROGRAM_BEGIN]
        self.allocate_interpreter()
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
    def allocate_interpreter(self):
        chip8_fontset = [
            0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
            0x20, 0x60, 0x20, 0x20, 0x70,  # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
            0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
            0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
            0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
            0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
            0xF0, 0x80, 0xF0, 0x80, 0x80   # F
        ]
        for i in range(len(chip8_fontset)):
            self.memory[INTERPRETER_BEGIN + i] = chip8_fontset[i]
        
