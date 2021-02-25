intersections = {0: [[], []]}
f = open("output_file", "w")
for intersection in intersections.keys():
    if len(intersections[intersection][0]) == 1:
        f.write(intersection)
        f.write(1)
        f.write(intersections[intersection][0][0], 1)
