import random
def choice_data(data):
    _list = data.split(",")
    num = random.choice(_list)
    return num


if __name__ == "__main__":
    print(choice_data("200, 100, 5"))
