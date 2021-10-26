import datetime
import time


def get_time(time_type, layout, unit="0,0,0,0,0"):
    tim = datetime.datetime.now()
    if time_type != "now":
        lag = unit.split(",")
        try:
            tim = tim + datetime.timedelta(seconds=int(lag[0]), minutes=int(lag[1]),
                                           hours=int(lag[2]), days=int(lag[3]), weeks=int(lag[4]))
        except ValueError:
            raise Exception("time err type:%s" % unit)
    # get 10 time stamp 
    if layout == "10timestamp":
        tim = tim.strftime('%Y-%m-%d %H:%M:%S')
        tim = int(time.mktime(time.strptime(tim, "%Y-%m-%d %H:%M:%S")))
        return tim
    # get 13 time stamp 
    elif layout == "13timestamp":
        tim = tim.strftime('%Y-%m-%d %H:%M:%S')
        tim = int(time.mktime(time.strptime(tim, "%Y-%m-%d %H:%M:%S")))
        tim = int(round(tim * 1000))
        return tim
    # format time
    else:
        tim = tim.strftime(layout)
        return tim


if __name__ == "__main__":
    print(get_time("else_time", "%Y-%m-%d %H:%M:%S", "5,5,5,5,5"))
    print(get_time("now", "%Y-%m-%d %H:%M:%S", "5,5,5,5,5"))

