def singleton(the_class):
      instances = {}

      def get_class(*args, **kwargs):
            if the_class not in instances:
                  instances[the_class] = the_class(*args, **kwargs)
                  print('passou pelo get_class if not')
            return instances[the_class]

      return get_class

@singleton
class AppSettings:
      def __init__(self):
            self.tema = "o tema escuro"
            self.font = '19px'


@singleton
class Teste:
      def __init__(self):
            pass


if __name__ == "__main__":
      as1 = AppSettings()
      as1.tema = 'o tema claro'
      print(as1.tema)
      as2 = AppSettings()
      as2.tema = 'o tema escuro'
      print(as1.tema)
      
      t1 = Teste()
      t2 = Teste()


