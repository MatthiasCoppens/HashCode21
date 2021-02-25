file_in = open('input_F', 'r')
file_out = open('output_F', 'w')

inp = file_in.read().splitlines()
l = int(inp[0].split()[0])
lines = [l.split() for l in inp[1:l+1]]

db = {}

for line in lines:
    db[line[1]] = db.get(line[1], [])
    db[line[1]].append(line[2])

print(len(db), file=file_out)
for intersection, streets in db.items():
    print(intersection, file=file_out)
    print(len(streets), file=file_out)
    for street in streets:
        print(f'{street} 1', file=file_out)
