def generator_of_lines(file_name_or_file, *finding_words):
    words = []
    global word
    for word in finding_words:
        word = str(word)
        words.append(word.lower())
    if isinstance(file_name_or_file, str):
        with open(file_name_or_file, "r") as file:
            print(type(file), type(words))
            for line in file:
                yield line.strip()
                if word.lower() in line.lower():
                    print(line)
                else:
                    print("|||||| There is no such word as", "'", word, "'", 'in this line' "||||||")

        file = file_name_or_file
        for line in file:
            yield line.strip()
            if word.lower() in line.lower():
                print(line)
            else:
                print("|||||| There is no such word as", "'", word, "'", 'in this line' "||||||")
