map_file = 'pg2701.txt.map'
sorted_map_file = 'pg2701.txt.map.sorted'

def build_index(filename):
    index = []
    f = open(filename)
    while True:
        offset = f.tell()
        line = f.readline()
        if not line:
            break
        length = len(line)
        col = line.split('\t')[0].strip()
        index.append((col, offset, length))
    f.close()
    index.sort()
    return index

try:
    index = build_index(map_file)
    in_file = open(map_file, 'r')
    out_file = open(sorted_map_file, 'w')
    for col, offset, length in index:
        in_file.seek(offset)
        out_file.write(in_file.read(length))
    in_file.close()
    out_file.close()
except IOError:
    print("error performing file operation")
