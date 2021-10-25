import os


def mk_dir(path):
    # head space
    path = path.strip()
    # end \
    path = path.rstrip("\\")

    # path exist
    is_exists = os.path.exists(path)
    if not is_exists:
        try:
            os.makedirs(path)
        except Exception as e:
            print(e)
    else:
        pass


if __name__ == "__main__":
    mk_dir("./log")
