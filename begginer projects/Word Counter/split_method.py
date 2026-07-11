def read_input_file(filename):
    try:
        file = open(filename, 'r')
        return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""


# Write the code below to solve the problem
def count_words_split(text):
    words=text.split()
    # Split the text into words
    total_words=len(words)
    return total_words
    # Count and return the total number of words

    

if __name__ == "__main__":
    filename = "/home/chef/workspace/input.txt"
    text = read_input_file(filename)

    if text:
        total_words = count_words_split(text)
        print(total_words)