from SomeModel import *
from Generator_of_lines import *
import unittest


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


class TestMessageMoodAndGeneratorOfLines(unittest.TestCase):

    def test_predict_type_errors(self):
        self.assertRaises(ValueError, SomeModel.predict, int)
        self.assertRaises(ValueError, SomeModel.predict, float)
        self.assertRaises(ValueError, SomeModel.predict, bool)
        self.assertRaises(ValueError, SomeModel.predict, complex)
        self.assertRaises(ValueError, SomeModel.predict, list)
        self.assertRaises(ValueError, SomeModel.predict, tuple)
        self.assertRaises(ValueError, SomeModel.predict, set)
        self.assertRaises(ValueError, SomeModel.predict, dict)
        self.assertRaises(ValueError, SomeModel.predict, frozenset)

    def test_custom_end_cases(self):

        def custom_predict_message_mood(score, bad_thresholds, good_thresholds):
            if score < bad_thresholds:
                return f"неуд {score}"
            elif score == bad_thresholds:
                return f"норм, вы указали пограничный случай для нормальных показателей"
            elif score > good_thresholds:
                return f"отл {score}"
            elif score == good_thresholds:
                return f"отл, вы указали пограничный случай для отличных показателей"
            else:
                return f"норм {score}"

        custom_predict_message_mood(0.4, 0.4, 0.6)

        self.assertEqual(custom_predict_message_mood(0.4, 0.4, 0.6).__str__(), "норм, вы указали пограничный случай для нормальных показателей")
        self.assertEqual(custom_predict_message_mood(0.4, 0.5, 0.6).__str__(), "неуд 0.4")
        self.assertEqual(custom_predict_message_mood(0.4, 0.1, 0.4).__str__(), "отл, вы указали пограничный случай для отличных показателей")
        self.assertEqual(custom_predict_message_mood(0.4, 0.3, 0.6).__str__(), "норм 0.4")
        self.assertEqual(custom_predict_message_mood(0.99, 0.8, 0.9).__str__(), "отл 0.99")

    def test_end_cases(self):

        def custom_predict_message_mood(score, bad_thresholds: float = 0.3, good_thresholds: float = 0.8):
            if score < bad_thresholds:
                return f"неуд {score}"
            elif score == bad_thresholds:
                return f"норм, вы указали пограничный случай для нормальных показателей"
            elif score > good_thresholds:
                return f"отл {score}"
            elif score == good_thresholds:
                return f"отл, вы указали пограничный случай для отличных показателей"
            else:
                return f"норм {score}"

        self.assertEqual(custom_predict_message_mood(0.3).__str__(), "норм, вы указали пограничный случай для нормальных показателей")
        self.assertEqual(custom_predict_message_mood(0.8).__str__(), "отл, вы указали пограничный случай для отличных показателей")

    def test_generator(self):
        s1 = generator_of_lines("Homework1Vk.txt", "в")
        res = next(s1)
        s2 = generator_of_lines("Homework1Vk.txt", "файла")
        res2 = next(s2)
        s3 = generator_of_lines("Homework1Vk.txt", "файла", "не")
        res3 = next(s3)
        self.assertEqual(res, "Есть текстовый файл который может не помещаться в память")
        self.assertEqual(res2, "Написать генератор filter_file для чтения и фильтрации файла")
        self.assertEqual(res3, "Написать генератор filter_file для чтения и фильтрации файла")


if __name__ == "__main__":
    unittest.main()

