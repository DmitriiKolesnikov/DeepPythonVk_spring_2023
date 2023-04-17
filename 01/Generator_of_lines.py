def generator_of_lines(file_name_or_file, *finding_words):
    words = []
    global word
    for word in finding_words:
        word = str(word)
        words.append(word.lower())
    if isinstance(file_name_or_file, str):
        with open(file_name_or_file, "r") as file:
            for line in file:
                if word.lower() in line.lower():
                    yield line.strip()
    else:
        file = file_name_or_file
        for line in file:
            if word.lower() in line.lower():
                yield line.strip()


if __name__ == "__main__":
    pass
