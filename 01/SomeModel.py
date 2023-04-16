import random


class SomeModel:
    @staticmethod
    def predict(message):
        if type(message) == str:
            num = round(random.random(), 2)
            return num
        else:
            return f"Type is not str"


def predict_message_mood(message,
                         bad_thresholds: float = 0.3, good_thresholds: float = 0.8):
    if type(message) == str:
        score = SomeModel.predict(message)
        if score < bad_thresholds:
            return f"неуд, {score = }"
        elif score > good_thresholds:
            return f"oтл, {score = }"
        else:
            return f"норм, {score = }"
    else:
        pass


if __name__ == "__main__":
    print("First homework")
