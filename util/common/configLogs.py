import logging
import time

from util.common.mkDir import mk_dir


class LogConfig:
    def __init__(self, path):
        runtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # Log level
        # all logs
        mk_dir(path+"\logs\\")
        logfile = path + "\logs\\" + runtime + '.log'
        fh = logging.FileHandler(logfile, mode='w+')
        fh.setLevel(logging.DEBUG)  # Log level
        # error logs
        logfile_error = path + "\logs\\" + runtime + '_error.log'
        fh_error = logging.FileHandler(logfile_error, mode='w+')
        fh_error.setLevel(logging.ERROR)  # log level
        # console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # level
        # output format
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        fh_error.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add logs
        logger.addHandler(fh)
        logger.addHandler(fh_error)
        logger.addHandler(ch)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=logfile,
                            filemode='w')
        logging.basicConfig(level=logging.ERROR,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=fh_error,
                            filemode='w')

