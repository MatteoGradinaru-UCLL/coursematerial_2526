def rpg2(n_sides, goal):
    count = 0
    total = n_sides * n_sides
    for i in range(1, n_sides + 1):
        for y in range(1, n_sides + 1):
            if i + y >= goal:
                count += 1
    return (count / total) * 100


def rpg3(n_sides, goal):
    count = 0
    total = n_sides * n_sides * n_sides
    for i in range(1, n_sides + 1):
        for y in range(1, n_sides + 1):
            for k in range(1, n_sides + 1):
                if i + y + k >= goal:
                    count += 1
    return (count / total) * 100