import random

# Define the CFG
grammar = {
    "<song>": [["<alap>", "<bandish>", "<taal_pattern>"]],
    "<alap>": [["<phrase>", "<alap>"], ["<phrase>"]],
    "<bandish>": [["<line>", "<bandish>"], ["<line>"]],
    "<taal_pattern>": [["<taal>", "<taal_pattern>"], ["<taal>"]],
    "<phrase>": [["<note>", "<ornament>"], ["<note>"]],
    "<line>": [["<phrase>", "<phrase>", "<phrase>"]],
    "<taal>": ["Dha", "Dhin", "Na", "Tin", "Ke", "Te", "Ta"],
    "<note>": ["Sa", "Re", "Ga", "Ma", "Pa", "Dha", "Ni"],
    "<ornament>": ["Gamaka", "Meend", "Murki"]
}

def generate(grammar, symbol):
    if symbol not in grammar:
        return symbol
    rule = random.choice(grammar[symbol])
    return "".join(generate(grammar, s) for s in rule)

# Generate a song
song = generate(grammar, "<song>")
print("Randomly Generated Indian Music notes:",song)
