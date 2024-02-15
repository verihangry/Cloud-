import os
import collections
import socket

# Update these paths according to your local setup
DATA_DIR = "/home/data"
OUTPUT_DIR = "/home/output"

def read_file(file_path):
    """Read a text file and return its content as a list of words."""
    with open(file_path, 'r') as file:
        content = file.read()
    words = content.split()
    return words

def count_words(words):
    """Count the total number of words and return a Counter object for frequencies."""
    return len(words), collections.Counter(words)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure the output directory exists

    # a. List name of all the text files at location
    text_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]
    print(f"Text files: {text_files}")

    grand_total_words = 0
    word_counts = {}

    # b. and c. Read the two text files and count total number of words in each
    for filename in text_files:
        path = os.path.join(DATA_DIR, filename)
        words = read_file(path)
        total_words, word_freq = count_words(words)
        word_counts[filename] = total_words
        grand_total_words += total_words

    # d. List the top 3 words with maximum number of counts in IF.txt
    if 'IF.txt' in text_files:
        _, if_word_freq = count_words(read_file(os.path.join(DATA_DIR, 'IF.txt')))
        top_3_words = if_word_freq.most_common(3)
    else:
        top_3_words = []

    # e. Find the IP address of the machine
    ip_address = socket.gethostbyname(socket.gethostname())

    # f. Write all the output to a text file
    output_path = os.path.join(OUTPUT_DIR, 'result.txt')
    with open(output_path, 'w') as output_file:
        output_file.write(f"List of text files: {', '.join(text_files)}\n")
        for filename, total_words in word_counts.items():
            output_file.write(f"Total words in {filename}: {total_words}\n")
        output_file.write(f"Grand total of words in all files: {grand_total_words}\n")
        output_file.write("Top 3 words in IF.txt:\n")
        for word, count in top_3_words:
            output_file.write(f"{word}: {count}\n")
        output_file.write(f"IP Address: {ip_address}\n")

    # g. Print the information on console
    with open(output_path, 'r') as result_file:
        print(result_file.read())

if __name__ == "__main__":
    main()
