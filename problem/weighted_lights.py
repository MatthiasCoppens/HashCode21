from copy import deepcopy

for c in 'ABCDEF':

    filename = f'input_{c}'
    """
    drukte initieel
    key: streetname
    data: number of cars initially on it
    """
    initial_queues = {}

    """
    key: streetname
    data:
        - start intersection
        - stop intersection
        - time to travel
        - amount of passing cars
    """
    streets = {}

    """
    key: intersection ID
    data:
        - incomming streets
        - outgoing streets
        - amount of passing cars
    """
    intersections = {}
    vehicles = []

    with open(filename) as file:
        # read in simulation data
        d, i, s, v, f = [int(i) for i in file.readline().rstrip().split(" ")]

        # read in street and intersection data
        for _ in range(s):
            line = file.readline().rstrip().split(" ")

            streets[line[2]] = [int(line[0]), int(line[1]), int(line[3]), 0]
            initial_queues[line[2]] = 0

            if int(line[0]) not in intersections:
                intersections[int(line[0])] = [[], [line[2]], 0]
            else:
                intersections[int(line[0])][1].append(line[2])

            if int(line[1]) not in intersections:
                intersections[int(line[1])] = [[line[2]], [], 0]
            else:
                intersections[int(line[1])][0].append(line[2])

        # read in vehicles
        for _ in range(v):
            line = file.readline().rstrip().split(" ")
            vehicles.append(line[1:])

            initial_queues[line[1]] += 1
            if len(line) > 2:
                initial_queues[line[2]] += 0.5
            for street in vehicles[-1][:-1]:
                streets[street][-1] += 1
                intersections[streets[street][1]][-1] += 1

    file_out = open(f'output_{c}', 'w')

    #print(len(intersections), file=file_out)
    total_string = ""
    intersections_useful = 0
    for intersection, inter_data in intersections.items():
        #print(len(inter_data[0]), file=file_out)
        #norm_factor = 5
        #normalisation = d // (len(inter_data[0]) * norm_factor)


        sorted_streets = sorted(inter_data[0], key=lambda s: -initial_queues.get(s, 0))
        inter_data[0] = sorted_streets

        count_rules = 0
        lijnadd = ""
        for street in sorted_streets:
            if streets[street][3] == 0:
                time = 0
            elif streets[street][3] < len(inter_data[0]):
                time = 1
            else:
                time = streets[street][3] // len(inter_data[0])

            if (time != 0):
                count_rules += 1
                lijnadd += f'{street} {time}\n'
                #print(f'{street} {time}', file=file_out)

        if count_rules != 0:
            intersections_useful += 1
            total_string += f"{intersection}\n{count_rules}\n{lijnadd}"

    print(intersections_useful, file=file_out)
    print(total_string[:-1], file=file_out)

        # get corresponding intersection

        # set schedule for the intersection as to
