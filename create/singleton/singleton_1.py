"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.
When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""

class AppSettings:
      _instance = None # executando quando as1.qualquernome, se na foi digitado
                       # se ja foi digitado sobrescreve e todos sao a mesma sobrescrita 
      
      def __new__(cls, *args, **kwargs):
            if not cls._instance:
                  cls._instance = super().__new__(cls, *args, **kwargs)
                  print('passou pelo if not')
            return cls._instance

# problema nesse singleton é o init iniciado varias vezes

      def __init__(self): 
            self.tema = "o tema escuro" #comentar init pra ser singleton
            self.font = '19px'
            print('passou pelo init')


if __name__ == "__main__":
      as1 = AppSettings()
      as1.tema = 'o tema claro'
      print(as1.tema)
      as2 = AppSettings()
      as2.tema = 'o tema escuro'
      print(as2.tema)
      as3 = AppSettings()
      as1.data = '25/05'
      print(as1.data)
