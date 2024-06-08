def file_instructions(file: str):

    instructions = []

    instruction = ""

    with open(file, "r") as file_to_read:
        for x in file_to_read.readlines():
            for y in x:
                if y in [" ","\n"]:
                    instructions.append(instruction)
                    instruction = ""
                    continue
                instruction += y
    for x in instructions:
        if x == "":
            instructions.pop(instructions.index(x))
    return instructions
