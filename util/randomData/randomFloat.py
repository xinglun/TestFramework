import random



def random_float(data):
    try:
        start_num, end_num, accuracy = data.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
        accuracy = int(accuracy)
    except ValueError:
        raise Exception("range or acc err！\n acc %s" % data)
    if start_num <= end_num:
        num = random.uniform(start_num, end_num)
    else:
        num = random.uniform(end_num, start_num)
    num = round(num, accuracy)
    return num


if __name__ == "__main__":
    print(random_float("200, 100, 5"))
