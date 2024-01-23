import json

def readFromJSON1():
    with open('info_commands.json') as f:
        info_commands = json.load(f)
    return info_commands

def readFromJSON2():
    with open('game_commands.json') as f:
        game_commands = json.load(f)
    return game_commands

