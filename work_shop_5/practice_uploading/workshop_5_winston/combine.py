file = input('Enter the name of the file you want to combine: ')
file_base = ''
if 'puzzle2' in file:
    file_base = 'puzzle2'
elif 'puzzle1' in file:
    file_base = 'puzzle1'
else:
    print('Invalid file name')
    exit()
file_a = open(file_base + '-A.txt','r')
file_b = open(file_base + '-B.txt','r')
file_b = open("puzzle2-B.txt","r")
file_out = open("puzzle2-out.txt","w")
file_a_lines = file_a.readlines()
file_b_lines = file_b.readlines()

max_lines = max(len(file_a_lines), len(file_b_lines))

for i in range(max_lines):
    if i < len(file_a_lines):
        file_out.write(file_a_lines[i])
    if i < len(file_b_lines):
        file_out.write(file_b_lines[i])