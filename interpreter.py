import sys

args = sys.argv

with open(args[1], "r") as f:
    code = f.read().split()

memory = [0 for i in range(1024)]
ptr = 0
rdr = 0

while rdr < len(code):
    if code[rdr] == "てもて":
        ptr += 1

    if code[rdr] == "てもてっ":
        ptr -= 1

    if code[rdr] == "てもて〜":
        memory[ptr] += 1

    if code[rdr] == "てもてー":
        memory[ptr] -= 1

    if code[rdr] == "てもて！":
        print(chr(memory[ptr]), end="")

    if code[rdr] == "てもて？":
        memory[ptr] = int(input())

    if code[rdr] == "あっぷっ":
        if memory[ptr] == 0:
            nest = 0
            while True:
                rdr += 1
                if code[rdr] == "あっぷっ":
                    nest += 1
                if code[rdr] == "ぷぇ！" and nest == 0:
                    break
                if code[rdr] == "ぷぇ！":
                    nest -= 1

    if code[rdr] == "ぷぇ！":
        if memory[ptr] != 0:
            nest = 0
            while True:
                rdr -= 1
                if code[rdr] == "ぷぇ！":
                    nest += 1
                if code[rdr] == "あっぷっ" and nest == 0:
                    break
                if code[rdr] == "あっぷっ":
                    nest -= 1

    rdr += 1
