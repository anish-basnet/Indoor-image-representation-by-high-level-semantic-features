
import json


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})):
    pass


class Config:
    __instance = None
    __is_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.name = 'Config Singleton'
        return cls.__instance

    def __init__(self, filename=None):
        if not self.__is_init:
            self.__build(filename)
            self.__is_init = True

    def __build(self, filename=None):
        try:
            with open(filename or 'settings.json') as fp:
                self.__config = json.load(fp)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_instance():
        return Config().__config
