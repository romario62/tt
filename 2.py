

def color(inp):
    if "готов" in inp:
        color = {"backgroundColor": {"red": 0, "green": 1} }
    else:
        color = {"backgroundColor": {"red": 1, "green": 0} }
    return color
inp = input()
print(color(inp))
