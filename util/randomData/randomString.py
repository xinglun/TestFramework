import random
import string
def random_string(num_length):
    try:
        num_length = int(num_length)
    except ValueError:
        raise Exception("length err %s" % num_length)
    num = ''.join(random.sample(string.ascii_letters + string.digits, num_length))
    return num


if __name__ == "__main__":
    print(random_string(5))
