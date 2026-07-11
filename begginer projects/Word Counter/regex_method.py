import re

def read_input_file(filename):
    try:
        file = open(filename, 'r')
        return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

# Write the code below
def count_words_regex(text):  
    # Use regex to extract words while ignoring punctuation  
    words=re.findall(r'\b\w+\b',text)
    return len(words)
    
    # Count and return the total number of words  
    
    

if __name__ == "__main__":
    filename = "/home/chef/workspace/input.txt"
    text = read_input_file(filename)

    if text:
        total_words = count_words_regex(text)
        print(total_words)