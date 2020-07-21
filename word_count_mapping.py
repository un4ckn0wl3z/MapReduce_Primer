import re

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))
    
input_file = 'pg2701.txt'
map_file = 'pg2701.txt.map'

# Implement our mapping function
# import re
sums = {}
try:
    in_file = open(input_file, 'r')
    out_file = open(map_file, 'w')

    for line in in_file:
        for word in splitter(line):
            out_file.write(word.lower() + "\t1\n") # Separate key and value with 'tab'
            
    in_file.close()
    out_file.close()

except IOError:
    print("error performing file operation")
