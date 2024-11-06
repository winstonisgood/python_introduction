# Prompt user to enter the file name they want to combine
def get_file():
    filename = input("Please enter the file name you want to combine (exclude '-A.txt'): ")
    return filename.replace("-A.txt", "").replace("-B.txt", "")

#Read the content of the file and return a list of lines
def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            return [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Insert the lines from two files to combined_lines list
def insert_lines(lines_a, lines_b):
    # Ensure the function covers all lines from both files
    max_length = max(len(lines_a), len(lines_b))
    # Initialize the combined_lines list
    combined_lines = []
    for i in range(max_length):
        if i < len(lines_a):
            combined_lines.append(lines_a[i])
        if i < len(lines_b):
            combined_lines.append(lines_b[i])

    final_combined_lines = []
    for i in range(len(combined_lines)):
        if i % 2 == 0 and i // 2 < len(lines_a):
            final_combined_lines.append(lines_a[i // 2])
        elif i % 2 == 1 and i // 2 < len(lines_b):
            final_combined_lines.append(lines_b[i // 2])

    return '\n'.join(final_combined_lines)


#Write the combined content to the output file
def write_output(filename, lines):
    with open(filename, 'w') as file:
        file.write(lines)
    print(lines)

# Main function
def combine_files():
    filename_base = get_file()
    file_a = f"{filename_base}-A.txt"
    file_b = f"{filename_base}-B.txt"
    output_file = f"{filename_base}-out.txt"

    lines_a = read_file_lines(file_a)
    lines_b = read_file_lines(file_b)

    # Combine lines
    combined_lines = insert_lines(lines_a, lines_b)

    # Write combined content to the output file
    write_output(output_file, combined_lines)

combine_files()
