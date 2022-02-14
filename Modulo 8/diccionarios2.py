planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

total = 0
for moon in planet_moons.values():
    total += moon

print(f'hay { total } de lunas')
print(f'el promedio es de { total / 7 } lunas')
