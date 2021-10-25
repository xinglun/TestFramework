import hashlib
import re


def md5_data(data):
    m1 = hashlib.md5()
    m1.update(data.encode("utf-8"))
    data = m1.hexdigest()
    return data


def re_md5(data):
    test = re.findall("\$MD5\(((?!.*\$MD5\().*?)\)MD5\$", data)
    if not len(test):
        pass
    else:
        for i in test:
            k = md5_data(i)
            i = i.replace("(", "\(").replace(")", "\)")
            pattern = re.compile('\$MD5\(' + i + '\)MD5\$')  # 初始化正则匹配
            data = re.sub(pattern, k, data, count=1)
            # print(data)
            data = re_md5(data)
    return data


if __name__ == "__main__":
    print(md5_data("123456"))
