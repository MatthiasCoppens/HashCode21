def read_sim_data(filename):
    """
    input:
        name of file

    output:
        - tuple with simulation data
        - dictionary with street data
        - dictionary with intersection data
        - list with vehicle routes
    """
    
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

    """
    list of vehicle paths
    """
    vehicles = []
    
    with open(filename) as file:
        # read in simulation data
        d,i,s,v,f = [int(i) for i in file.readline().rstrip().split(" ")]
        
        # read in street and intersection data
        for _ in range(s):
            line = file.readline().rstrip().split(" ")
    
            streets[line[2]] = [int(line[0]), int(line[1]), int(line[3]), 0]
            
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
            for street in vehicles[-1][:-1]:
                streets[street][-1]+=1
                intersections[streets[street][1]][-1]+=1

    return (d,i,s,v,f), streets, intersections, vehicles

print(read_sim_data("./problem/input_A"))
