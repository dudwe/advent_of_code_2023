

def parse_seeds(seeds_line):

    seeds = [int(seed) for seed in seeds_line[1:]]
    return seeds


def parse_seeds_as_range(seeds_line):
    seeds_line = parse_seeds(seeds_line)
    seeds = []
    for x in range(0, len(seeds_line), 2):
        seed = [seeds_line[x],seeds_line[x]+seeds_line[x+1]]
        print(seed)
        seeds.append(seed)

    return seeds


def parse_maps(file_data):
    maps = list(filter(lambda x: x != '', file_data))
    idx = 0
    output_maps = []
    while idx < len(maps):
        cur = []
        if "map" in maps[idx]:
            idx += 1
            while idx < len(maps) and "map" not in maps[idx]:
                cur.append([int(x) for x in maps[idx].split()])
                idx += 1
        output_maps.append(cur)
    return output_maps


def parse_maps_alt(file_data):
    maps = list(filter(lambda x: x != '', file_data))
    idx = 0
    output_maps = []
    while idx < len(maps):
        cur = []
        if "map" in maps[idx]:
            map_name = maps[idx][:-5]
            idx += 1
            while idx < len(maps) and "map" not in maps[idx]:
                cur.append([int(x) for x in maps[idx].split()])
                idx += 1
            data = {map_name:cur}
        output_maps.append(data)
    return output_maps


def parse_file(path):

    with open(path) as f:
        lines = f.read().splitlines()
        # print(lines)
        seeds_line = lines[0].split()
        seeds = parse_seeds(seeds_line)

        output_maps = parse_maps(lines[2:])

    # print(f"{seeds=} {output_maps=}")
    return seeds, output_maps


def parse_file_part_2(path):
    with open(path) as f:
        lines = f.read().splitlines()
        seeds_line = lines[0].split()
        seeds = parse_seeds_as_range(seeds_line)

        output_maps = parse_maps_alt(lines[2:])

    print(f"{seeds=} {output_maps=}")
    return seeds, output_maps


def part_1():
    seeds, maps = parse_file("input.txt")
    final_maps = []
    for seed in seeds:
        prev = seed
        current_val = seed

        for map in maps:

            for map_row in map:
                # Compute if we need ot update the seed
                # print(map_row)1
                dest, source, spread = map_row[0], map_row[1], map_row[2]
                if source <= current_val < source+spread:
                    current_val = current_val + (dest-source)
                    break
                # If so update it
            print(f"{prev} -> {current_val}")
            prev = current_val

        final_maps.append(current_val)
    print(final_maps)
    return min(final_maps)

# print(part_1())

def part_2():
    seeds, maps = parse_file_part_2("input.txt")
    print(seeds, maps)

    #Extra Process the maps
    post_maps = []

    for farm_map in maps:

        for name,mappings in  farm_map.items():
            mapping_ranges = dict()
            for mp in mappings:
                dest, source, spread = mp[0], mp[1], mp[2]
                delta =  dest-source
                mapping_ranges[(source,source+spread-1)] = (dest,dest+spread-1)

            #print(name,sorted(mapping_ranges))        
            post_maps.append({name:mapping_ranges})
    print(post_maps)


    #Look at each seed range, compute the range

    min_vals = []
    for seed in seeds:
        print("Process ",seed)

        seed_mappings = {(seed[0],seed[1])}    
        stack = [(seed[0],seed[1])]
        
        for farm in post_maps:
            
            for name,mappings in farm.items():
                #print(f"Filter through {name} {stack=}")
                output = []
                while stack:
                    current_seed = stack.pop()
                    l,r = current_seed[0],current_seed[1]
                    found = False
                    for mapping_func in sorted(mappings):
                        mapping_l,mapping_r = mapping_func[0],mapping_func[1]
                        delta = mappings[mapping_func][1] - mapping_r
                        print(f"Check {current_seed} in {mapping_func}:{mappings[mapping_func]} {delta=}")
                        if  r < mapping_l or   l > mapping_r :
                            #No overlap so we ignore this
                            continue
                        elif l >=mapping_l and r<=mapping_r:
                            new_seed = (l+delta,r+delta)
                            output.append(new_seed)
                            found = True
                            print(f"Nested {current_seed} -> {new_seed}")
                            break
                        elif l <mapping_l and r>mapping_r:
                            left = (l,mapping_l-1)
                            right = (mapping_r+1,r)
                            stack.append(left)
                            stack.append(right)
                            new_seed = (mapping_l+delta,mapping_r+delta)
                            output.append(new_seed)
                            print(f"Inner func split {mapping_func}  {current_seed} -> {left=} {new_seed=} {right=}")
                            #Nested inner
                            '''
                            e.g
                            [81,95]
                            [83,94]

                            [81,82] [83,94] [95,95]
                            
                            '''

                        else:

                            '''
                            Overlap
                            e.g. 
                            [81,95] [18,94]

                            => [81,94] [95,95]


                            74,87 77,99
                            
                            => 74,77 87,99
                            '''

                            if r > mapping_r:

                                right_tuple = (mapping_r+1,r)
                                #Map left only 
                                mapped_left = (l+delta,mapping_r+delta)
                                stack.append(right_tuple)
                                output.append(mapped_left)
                                print(f"Overlap R {mapping_func} {current_seed} -> {right_tuple=}, {mapped_left=} ")
                            elif l <= mapping_l:
                                left_tuple = (l,mapping_l-1)
                                # Map right only
                                mapped_right = (mapping_l+delta,r+delta)
                                stack.append(left_tuple)
                                output.append(mapped_right)
                                print(f"Overlap L {current_seed} -> {left_tuple=}  , {mapped_right=}")
                            else:
                                print("ERRRORORO")
                            found = True
                    if not found:
                        print(f"Failed to get match for {current_seed} in {name}")
                        output.append(current_seed)
                    else:
                        print(f"Got match for {current_seed} in {name} {output=},{stack=}")
                

                stack = output
            print(f"Result for  {name} is {output} ")
        print(f"final for {seed} is {output}")
        min_val = min(output)[0]
        min_vals.append(min_val)
        break

    print(min_vals,min(min_vals))
    return min_vals




def par231t_2():
    '''
    Compute the seed min and max  for each seed range 
    We need to track the ranges as we go along

    If the map range is bigger than the range we are looking at,
        We update the range boundaries by SHIFT
    If the map range is smaller than the range we are lookign at
        We need to update our ranges
    '''
    seeds, maps = parse_file_part_2("input.txt")
    print(seeds, maps)

    for seed_range in seeds:
        print("Track for ",seed_range)
        current_ranges = [[seed_range[0],seed_range[1]]]
        for cidx, mp in enumerate(maps):
            c_map = []
            print(f"{current_ranges=}")
            





            for map_row in mp:
                dest, source, spread = map_row[0], map_row[1], map_row[2]


                delta =  dest-source
                source_l,source_r = source , source+spread-1

                #Is in range
                new_range = []
                untouched = [True for x in current_ranges]
                for idx,rg in enumerate(current_ranges):
                    l,r = rg[0],rg[1]
                    #print(f"Compare {l},{r} original range to mapping range {source_l},{source_r}, {delta=}")
                    
                    #No overlap
                    if r < source_l or   l > source_r :
                        #print("No Map")
                        continue
                    #Nested map
                    elif l >=source_l and r<=source_r:
                        #print(f"{cidx=} inner map")
                        #Replace our current_map with a new one
                        new_range.append([rg[0] + delta,rg[1] + delta])
                        untouched[idx] = False
                        break
                    else:
                        #Overlap
                        #print(f"{cidx=} overlap")
                        
                        #Need to create new tuples 
                        '''
                        e.g. 
                        [81,95] [18,94]

                        => [81,94] [95,95]


                        74,87 77,99
                        
                        => 74,77 87,99
                        '''

                        if r >= source_r:
                            left_tuple = [l,source_r]
                            right_tuple = [source_r+1,r]
                            #Map left only 
                            mapped_left = [l+delta,source_r+delta]
                            new_range.append(mapped_left)
                            new_range.append(right_tuple)
                            untouched[idx] = False    
                        elif l <= source_l:
                            left_tuple = [l,source_l-1]
                            right_tuple = [source_l,r]
                            # Map right only
                            mapped_right = [source_l+delta,r+delta]
                            new_range.append(left_tuple)
                            new_range.append(mapped_right)

                            untouched[idx] = False
                        else:
                            print("ERROR SHOULDNEVER SEE THIS")

                if new_range:
                    print(f"{cidx=} {new_range=}")
                    rem_ranges =  []
                    for idx,utc in enumerate(untouched):
                        if utc:
                            rem_ranges.append(current_ranges[idx])
                    
                    new_map = new_range + rem_ranges
                    print(f"{current_ranges} => {new_map}")
                    current_ranges = new_map
                    current_ranges.sort()
        break
    

part_2()
100053687
100165128