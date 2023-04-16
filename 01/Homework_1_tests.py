from SomeModel import *
from Generator_of_lines import *

def what_is_in_the_predict(message):
    res = type(message)
    if res == int:
        return f"Message type is int, it's the wrong type you need str"
    elif res == float:
        return f"Message type is float, it's the wrong type you need str"
    elif res == str:
        return f"Message type is str"
    elif res == bool:
        return f"Message type is bool, it's the wrong type you need str"
    elif res == complex:
        return f"Message type is complex, it's the wrong type you need str"
    elif res == list:
        return f"Message type is list, it's the wrong type you need str"
    elif res == tuple:
        return f"Message type is tuple, it's the wrong type you need str"
    elif res == set:
        return f"Message type is set, it's the wrong type you need str"
    elif res == dict:
        return f"Message type is dict, it's the wrong type you need str"
    elif res ==frozenset:
        return f"Message type is frozenset, it's the wrong type you need str"
    else:
        return f"it's the wrong type you need str"


def check_end_cases(bad_thresholds: float = 0.3, good_thresholds: float = 0.8):

    def custom_predict_message_mood(score):
        if score < bad_thresholds:
            print("неуд", score)
        elif score == bad_thresholds:
            print("норм, вы указали пограничный случай для нормальных показателей")
        elif score > good_thresholds:
            print("отл", score)
        elif score == good_thresholds:
            print("отл, вы указали пограничный случай для отличных показателей")
        else:
            print("норм", score)

    assert custom_predict_message_mood(0.3) == "норм, вы указали пограничный случай для нормальных показателей", False
    assert custom_predict_message_mood(0.8) == "отл, вы указали пограничный случай для отличных показателей", False


def check_custom_end_cases():

    def custom_predict_message_mood(score, bad_thresholds, good_thresholds):
        if score < bad_thresholds:
            print("неуд", score)
        elif score == bad_thresholds:
            print("норм, вы указали пограничный случай для нормальных показателей")
        elif score > good_thresholds:
            print("отл", score)
        elif score == good_thresholds:
            print("отл, вы указали пограничный случай для отличных показателей")
        else:
            print("норм", score)

    assert custom_predict_message_mood(0.4, 0.4, 0.6) == "норм, вы указали пограничный случай для нормальных показателей", False
    assert custom_predict_message_mood(0.4, 0.5, 0.6) == "неуд 0.4", False
    assert custom_predict_message_mood(0.4, 0.1, 0.4) == "отл, вы указали пограничный случай для отличных показателей", False
    assert custom_predict_message_mood(0.4, 0.3, 0.6) == "норм 0.4", False
    assert custom_predict_message_mood(0.99, 0.8, 0.9) == "отл 0.99", False


def test_second_task():
    s1 = generator_of_lines("Homework1Vk.txt", 1)
    res = next(s1)
    s2 = generator_of_lines("Homework1Vk.txt", "файла")
    res2 = next(s2)
    s3 = generator_of_lines("Homework1Vk.txt", "файла", "не")
    res3 = next(s3)
    assert res is None, False
    assert res2 == "написать генератор filter_file для чтения и фильтрации файла", False
    assert res3 == "написать генератор filter_file для чтения и фильтрации файла", False


if __name__ == "__main__":
    print("First homework")
