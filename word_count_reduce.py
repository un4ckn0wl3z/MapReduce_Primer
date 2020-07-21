

sorted_map_file = 'pg2701.txt.map.sorted'

previous = None
M = [None, 0]

def checkmax(key, sum):
    global m, M
    if M[1] < sum:
        M[1] = sum
        M[0] = key

try:
    in_file = open(sorted_map_file, 'r')
    for line in in_file:
        key, value = line.split('\t')
        
        if key != previous:
            if previous is not None:
                checkmax(previous, sum)
            previous = key
            sum = 0
            
        sum += int(value)
        
    checkmax(previous, sum)
    in_file.close()
except IOError:
    print("error performing file operation")
    
print("max: %s = %d" % (M[0], M[1]))
