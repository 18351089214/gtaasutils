"""
------------------------------------
@Time : 2019/11/13 10:00
@Auth : wangfei
@File : logfile.py
@IDE : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import logging
import os
import platform
from os import path


class Log(object):
    def __init__(self, name=__name__, path='{}.log'.format(os.path.split(__file__)[-1].split(".")[0]), level='ERROR'):
        print(path)
        self.__name = name
        self.__path = path
        if platform.system() == 'Windows':
            log_path = '\\'.join(path.split('\\')[0:-1])
        else:
            log_path = '/'.join(path.split('/')[0:-1])
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(filename)s] [line:%(lineno)d]'
                                      '[%(levelname)s]: %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回looger"""
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger


if __name__ == '__main__':
    log_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep), 'log')
    log = Log(path=log_path + '/log' + '/' + os.path.split(__file__)[-1].split(".")[0] + r".log")
    logger = log.Logger
    logger.debug('I am a debug message')
    logger.info('I am a info message')
    logger.warning('I am a warning message')
    logger.error('I am a error message')
    logger.critical('I am a critical message')
