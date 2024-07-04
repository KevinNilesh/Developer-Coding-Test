def count_words_in_file(filename: str) -> int:
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print(f"The file sample.txt was not found.")
        return 0

print(count_words_in_file('sample.txt'))
