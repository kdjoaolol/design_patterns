'''
class Meta(type):
      def __call__(cls, *args, **kwargs):
            print('CALL')
            return super().__call__(*args, **kwargs)

class Pessoa(metaclass=Meta):
      def __new__(cls, *args, **kwargs):
            print('NEW')
            return super().__new__(cls)

      def __init__(self, nome):
            print('INIT')
            self.nome = nome

      def __call__(self, x, y):
            print('Call chamado', self.nome, x+y)

p1 = Pessoa('LUIZ')
print(p1.nome)
'''
from typing import Dict

class Singleton(type):
      _instances: Dict = {}
      
      def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                  cls._instances[cls] = super().__call__(*args, **kwargs)
                  print('passou pelo if not ')
            print(cls._instances[cls])
            print(cls)
            return cls._instances[cls]

class AppSettings(metaclass=Singleton):
      def __init__(self):
            self.tema = "o tema escuro"
            self.font = '19px'

class Test(metaclass=Singleton):
      pass


if __name__ == "__main__":
      as1 = AppSettings()
      as1.tema = "quakquer coisa"
      as2 = AppSettings()
      as3 = AppSettings()

      print(as3.tema)
      print(as1 == as2)
      print(as2 == as3)

      t1 = Test()

      