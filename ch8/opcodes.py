NNN_MASK = 0x0FFF
def get_low_nibble(instruction:int) -> int:
    return instruction & 0x000F
def get_high_nibble(instruction:int) -> int:
    return instruction & 0xF000
def handle_opcode(cpu:object,instruction:int):
    y_instruction = (instruction & 0x00F0) >> 4
    x_instruction = (instruction & 0x0F00) >> 8
    kk = instruction & 0x00FF
    opcode_id = get_high_nibble(instruction)
    if opcode_id == 0x1000:
        cpu.pc = instruction & NNN_MASK
    if opcode_id == 0x2000:
        cpu.mem_stack[cpu.sp] = cpu.pc
        cpu.sp += 1
        cpu.pc = instruction & NNN_MASK
        cpu.skip_next_instruction()
    if opcode_id == 0x3000: # 3xkk, vx == kk
        register = x_instruction
        if cpu.data_registers[register] == kk:
            cpu.skip_next_instruction()
        else:
            cpu.goto_next_instruction()
    if opcode_id == 0x4000: # 4xkk, 4x != kk
        register = x_instruction
        if cpu.data_registers[register] != kk:
            cpu.skip_next_instruction()
        else:
            cpu.goto_next_instruction()
    if opcode_id == 0x5000: # 5xy0, x == y
        x_register = x_instruction
        y_register = y_instruction
        if cpu.data_registers[x_register] == cpu.data_registers[y_register]:
            cpu.skip_next_instruction()
        else:
            cpu.goto_next_instruction()
    if opcode_id == 0x6000: # 6xkk, Vx = kk
        cpu.data_registers[x_instruction] = kk
        cpu.goto_next_instruction()
    if opcode_id == 0x7000:
        cpu.data_registers[x_instruction] += kk
        cpu.goto_next_instruction()
    if opcode_id == 0x8000:
        nibble = get_low_nibble(instruction)
        x_register = x_instruction
        y_register = y_instruction
        if nibble == 0:
            cpu.data_registers[x_register] = cpu.data_registers[y_register]
            cpu.goto_next_instruction()
        if nibble == 1:
            cpu.data_registers[x_register] = cpu.data_registers[x_register] | cpu.data_registers[y_register]
            cpu.goto_next_instruction()
        if nibble == 2:
            cpu.data_registers[x_register] = cpu.data_registers[x_register] & cpu.data_registers[y_register]
            cpu.goto_next_instruction()
        if nibble == 3:
            cpu.data_registers[x_register] = cpu.data_registers[x_register] ^ cpu.data_registers[y_register]
            cpu.goto_next_instruction()
        if nibble == 4:
            result = cpu.data_registers[x_register] + cpu.data_registers[y_register]
            cpu.data_registers[0xF] = 1 if result > 0xFF else 0
            cpu.data_registers[x_register] = (result & 0xFF)
            cpu.goto_next_instruction()
        if nibble == 5:
            cpu.data_registers[0xF] = 1 if cpu.data_registers[x_register] >= cpu.data_registers[y_register] else 0
            cpu.data_registers[x_register] -= cpu.data_registers[y_register]
            cpu.goto_next_instruction()
        if nibble == 6:
            cpu.data_registers[0xF] = 1 if (get_low_nibble(cpu.data_registers[x_register]) & 0b0001) == 1 else 0
            cpu.data_registers[x_register] >>= 1
            cpu.goto_next_instruction()
        if nibble == 7:
            cpu.data_registers[0xF] = 1 if cpu.data_registers[y_register] > cpu.data_registers[x_register] else 0
            cpu.data_registers[x_register] = cpu.data_registers[y_register] - cpu.data_registers[x_register]
            cpu.goto_next_instruction()
        if nibble == 0xE:
            cpu.data_registers[0xF] = 1 if (get_high_nibble(cpu.data_registers[x_register]) & 0b1000) == 1 else 0
            cpu.data_registers[x_register] <<= 1
            cpu.goto_next_instruction()
    if opcode_id == 0x9000:
        nibble = get_low_nibble(instruction)
        x_register = x_instruction
        y_register = y_instruction
        if nibble == 0x0:
            if cpu.data_registers[x_register] != cpu.data_register[y_register]:
                cpu.skip_next_instruction()
            else:
                cpu.goto_next_instruction()
    if opcode_id == 0xA000:
        cpu.I = instruction & NNN_MASK
        cpu.goto_next_instruction()
    if opcode_id == 0xB000:
        cpu.pc = (instruction & NNN_MASK) + cpu.data_registers[0x0]

def op_0NNN(cpu,address_nnn:int) -> None:
    return
def op_00E0(cpu):
    return
def op_00EE(cpu):
    cpu.sp -= 1
    cpu.pc = cpu.mem_stack[cpu.sp]
    return
def op_1NNN(cpu,address_nnn:int) -> None:
    return
def op_2NNN(cpu,address_nnn:int) -> None:
    return
def op_3XNN(cpu,nn_value:int) -> None:
    return
def op_4XNN(cpu,nn_value:int) -> None:
    return
