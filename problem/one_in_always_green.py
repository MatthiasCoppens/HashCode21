intersections = {0: [["straat_1"], ["straat_2"]]}
f = open("output_file", "w")
for intersection in intersections.keys():
    if len(intersections[intersection][0]) == 1:
        print(intersection, file=f)
        print(1, file=f)
        print(intersections[intersection][0][0], 1, file=f)
f.close()