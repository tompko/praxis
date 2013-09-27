def brainfuck(program):
    program = "".join([x for x in list(program) if x in "<>+-,.[]"])
    data = [0] * 30000
    data_pointer = 0
    program_pointer = 0
    program_length = len(program)
    jump_stack = []
    
    while program_pointer < program_length:
        curr_inst = program[program_pointer]
        curr_data = data[data_pointer]
        if program[program_pointer] == "<":
            data_pointer -= 1
        elif program[program_pointer] == ">":
            data_pointer += 1
        elif program[program_pointer] == "+":
            data[data_pointer] += 1
        elif program[program_pointer] == "-":
            data[data_pointer] -= 1
        elif program[program_pointer] == ".":
            print chr(data[data_pointer]),
        elif program[program_pointer] == ",":
            data[data_pointer] = ord(raw_input())
        elif program[program_pointer] == "[":
            if data[data_pointer] == 0:
                inside = 0
                program_pointer += 1
                while program[program_pointer] != "]" or inside != 0:
                    if program[program_pointer] == "[":
                        inside += 1
                    if program[program_pointer] == "]":
                        inside -= 1
                    program_pointer += 1
            else:
                jump_stack.append(program_pointer)
        elif program[program_pointer] == "]":
            program_pointer = jump_stack.pop() - 1
        program_pointer += 1
