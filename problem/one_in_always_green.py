# for putting the intersections with one street incoming in a dict
intersections = {0: [["straat_1"], ["straat_2"]]}
traffic_lights = {}
for intersection in intersections:
    if len(intersections[intersection][0]) == 1:
        # traffic_lights[intersection] = list of tuples with street names and time per cycle
        traffic_lights[intersection] = [(intersections[intersection][0][0], 1)]

# for printing the traffic light from the format above
f = open("output_file", "w")
for intersection in traffic_lights:
    print(intersection, file=f)
    print(len(traffic_lights[intersection]), file=f)
    for streetname, time in traffic_lights[intersection]:
        print(streetname, time, file=f)
f.close()