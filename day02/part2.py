import re
import operator
from functools import reduce


input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

# with open('input') as file:
#     input = file.read()


MAX_COLOR = {
    'red': 12,
    'green': 13,
    'blue': 14
}

games = {}
games_possible = []
power = 0

for game in input.split('\n'):
    row = game.split(': ')
    match = re.match('Game (\\d+)', row[0])
    if not match:
        continue
    game_nr = int(match.group(1))
    games[game_nr] = {}
    is_possible = True
    round_nr = 0
    min_cubes = {}
    for round in row[1].split('; '):
        round_nr += 1
        games[game_nr][round_nr] = {}
        for info in round.split(', '):
            match = re.match('(\\d+) ([a-zA-Z]+)', info)
            count = int(match.group(1))
            color = match.group(2)
            games[game_nr][round_nr][color] = count
            if count > MAX_COLOR[color]:
                is_possible = False
                # print('Game %d: Too many %s cubes.' % (game_nr, color))
            if color not in min_cubes or min_cubes[color] < count:
                min_cubes[color] = count
    if is_possible:
        games_possible.append(game_nr)
    power += reduce(operator.mul, min_cubes.values())


print(power)
