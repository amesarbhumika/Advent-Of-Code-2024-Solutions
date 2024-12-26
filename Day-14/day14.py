from collections import Counter

with open('input14.txt', 'r') as f:
    lines = f.read().splitlines()

robots = []
for line in lines:
    position, velocity = line.split()
    position = position.split('=')[1].split(',')
    velocity = velocity.split('=')[1].split(',')
    px, py = int(position[0]), int(position[1])
    vx, vy = int(velocity[0]), int(velocity[1])
    robots.append((px, py, vx, vy))

width = 101
height = 103

def get_position_after_time(robot, t):
    px, py, vx, vy = robot
    return ((px + vx * t) % width, (py + vy * t) % height)

def get_quadrant(position):
    px, py = position
    if px == width // 2 or py == height // 2:
        return None
    return (px < width // 2, py < height // 2)

quadrants = Counter()
for robot in robots:
    new_position = get_position_after_time(robot, 100)
    quadrant = get_quadrant(new_position)
    if quadrant is not None:
        quadrants[quadrant] += 1

safety_factor = 1
for v in quadrants.values():
    safety_factor *= v

print("Part 1:", safety_factor)

def count_horizontal_adjacencies(positions):
    adjacencies = 0
    pos_set = set(positions)
    for y in range(height):
        for x in range(width - 1):
            if (x, y) in pos_set and (x + 1, y) in pos_set:
                adjacencies += 1
    return adjacencies

for t in range(10000):
    positions = [get_position_after_time(robot, t) for robot in robots]
    adjacencies = count_horizontal_adjacencies(positions)
    if adjacencies > 200:
        print("Part 2:", t)
        break