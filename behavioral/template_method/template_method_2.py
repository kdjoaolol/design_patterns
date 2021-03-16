"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.
Também é possível definir hooks para que as subclasses
utilizem caso necessário.
The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod



class Pizza(ABC):


      def prepare(self) -> None:
            # ----> TEMPLATE METHOD <----#
            self.hook_before_add_ingretients()
            self.add_ingretients() # Abstract
            self.hook_after_add_ingretients()
            self.cook()            # Abstract
            self.cut()             # Concreto
            self.serve()           # Concreto
            print()

      def hook_before_add_ingretients(self)-> None: pass

      def hook_after_add_ingretients(self)-> None: pass

      def cut(self)-> None:
            print(f'{self.__class__.__name__}: Cortando pizza')

      def serve(self)-> None:
            print(f'{self.__class__.__name__}: Servindo pizza')

      @abstractmethod
      def add_ingretients(self)-> None: pass

      @abstractmethod
      def cook(self)-> None: pass


class AModa(Pizza):
      def add_ingretients(self)-> None:
            print(f'AModa - adicionando ingredientes: presunto, queijo, abacaxi')

      def cook(self)-> None:
            print(f'AModa - cozinhando por 40min no forno a lenha')

class Veg(Pizza):
      def hook_before_add_ingretients(self)-> None:
            print('Veg - Lavando ingredientes')

      def add_ingretients(self)-> None:
            print(f'Vegana - adicionando ingredientes: milho, ervilha, palmito e champion')

      def cook(self)-> None:
            print(f'Vegana - cozinhando por 25min no forno a lenha')


if __name__ == "__main__":
      a_moda = AModa()
      a_moda.prepare()

      p_veg = Veg()
      p_veg.prepare()