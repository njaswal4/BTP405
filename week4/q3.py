def wordCount(file_path):
    word_dict = {}

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()

            for word in words:
                clean_word = word.strip('.,?!:;').lower()

                if clean_word not in word_dict:
                    word_dict[clean_word] = [line_number]
                else:
                    word_dict[clean_word].append(line_number)

    return word_dict

# Example ->
file_path = r'Text.txt'  
result = wordCount(file_path)
print(result)
