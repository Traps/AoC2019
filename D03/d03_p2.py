input_file = open('D03/.input', 'r')

path_strings = input_file.read()

input_file.close()

paths = [ps.split(',') for ps in path_strings.splitlines()]

paths_list = list()

for path in paths:
    x_pos = 0
    y_pos = 0

    path_list= []

    for step in path:
        x_dist = 0
        y_dist = 0

        x_step_list = [x_pos]
        y_step_list = [y_pos]

        dist = int(step[1:])

        if 'U' in step:
            y_step_list = range(y_pos, y_pos + dist)
            y_pos += dist
        
        elif 'D' in step:
            y_step_list = range(y_pos, y_pos - dist, -1)
            y_pos -= dist

        elif 'R' in step:
            x_step_list = range(x_pos, x_pos + dist)
            x_pos += dist
        
        else:
            x_step_list = range(x_pos, x_pos - dist, -1)
            x_pos -= dist

        step_list = [(x, y) for x in x_step_list for y in y_step_list]
        
        path_list.extend(step_list)

    paths_list.append(path_list)

intersect_points = set(paths_list[0]).intersection(set(paths_list[1]))

intersect_dist = [abs(x)+abs(y) for (x,y) in intersect_points if (x,y) != (0,0)]

print('Distance to closest intersection:', min(intersect_dist))

intersect_time = [sum([path.index(point) for path in paths_list]) for point in intersect_points if point != (0,0)]

print("First intersection after:", min(intersect_time))


