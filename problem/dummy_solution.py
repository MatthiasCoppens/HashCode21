for c in 'BCDEF':

    file_in = open(f'input_{c}', 'r')
    file_out = open(f'output_{c}', 'w')

    inp = file_in.read().splitlines()
    lines = [l.split() for l in inp]
    
    cycle = int(lines[0][0]) // 5
    nstreets = int(lines[0][2])

    db = {}
    for line in lines[1:nstreets+1]:
        db[line[1]] = db.get(line[1], [])
        db[line[1]].append(line[2])

    cars_per_street = {}
    for line in lines[nstreets+1:]:
        cars = int(line[0])
        for street in line[1:]:
            cars_per_street[street] = cars_per_street.get(street, 0) + cars

    db2 = {}
    for intersection, streets in db.items():
        total_cars = sum(cars_per_street.get(street, 1) for street in streets)
        schedule = {}
        for street in streets:
            t = (cycle * cars_per_street.get(street, 0)) // total_cars
            if t:
                schedule[street] = t
        if schedule:
            db2[intersection] = schedule

    print(len(db2), file=file_out)
    for intersection, streets in db2.items():
        print(intersection, file=file_out)
        print(len(streets), file=file_out)
        for street, t in streets.items():
            print(f'{street} {t}', file=file_out)
