
file_a = open("puzzle1-A.txt","r")
file_b = open("puzzle1-B.txt","r")
file_out = open("puzzle1-out.txt","a")
file_a_lines = file_a.readlines()
file_b_lines = file_b.readlines()


max_lines = max(len(file_a_lines), len(file_b_lines))


for i in range(max_lines):
    if i < len(file_a_lines):  
        file_out.write(file_a_lines[i])
    if i < len(file_b_lines):  
        file_out.write(file_b_lines[i])

