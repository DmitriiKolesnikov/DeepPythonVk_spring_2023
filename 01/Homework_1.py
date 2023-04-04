import random


class SomeModel:
    def predict(self, message):
        if type(message) == str:
            num = round(random.random(), 2)
            return num
        else:
            return f"Type is not str"


def predict_message_mood(message, class_example,
                         bad_thresholds: float = 0.3, good_thresholds: float = 0.8):
    if type(message) == str \
            and isinstance(class_example, (SomeModel, float)) == True:
        if class_example < bad_thresholds:
            return f"неуд"
        elif class_example > good_thresholds:
            return f"oтл"
        else:
            return f"норм"
    else:
        pass


def file_filter(file_name, *args):
    list_of_finding_words = []
    base_line = []
    for i in args:
        list_of_finding_words.append(i)
    with open(file_name, "r") as file:
        final_line_list = []
        for line in file:
            line_list = line.split()
            base_line.append(line_list)
            line_lower = [words.lower() for words in line_list]
            final_line_list.append(line_lower)
        for index in range(len(final_line_list)):
            yield final_line_list[index]
            for finding_word in list_of_finding_words:
                if finding_word in final_line_list[index]:
                    print(" ".join(base_line[index]), "|||||| Finding word is", "'", finding_word, "'", "||||||")
                else:
                    pass


if __name__ == "__main__":
    example = SomeModel().predict("njknfb")
    print(example)
    print(predict_message_mood("njknfb", example))

    def boo(n, l=list()):
        l.append(n)
        return l

    print([boo(3) for n in range(0,3)])



