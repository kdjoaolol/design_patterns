"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""
class StringReprMixin:
      def __str__(self):
            params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
            return f'{self.__class__.__name__}({params})'

      def __repr__(self):
            return self.__str__()

class MonoStateSimple(StringReprMixin):
      _state: dict = {}
      
      def __init__(self, nome=None, sobrenome=None):
            self.__dict__ = self._state # por exemplo list1 = list as mudanças no list mudam no list1
            if nome is not None:        # logo __dict__ é uma referencia de state, como state esta sendo
                  self.nome = nome      # carregado como constante, os atts nunca mudam ja que estao carregados em self._state
            if sobrenome is not None:
                  self.sobrenome = sobrenome
            print(self.__dict__, self._state)


if __name__ == "__main__":
      m1 = MonoStateSimple(nome='Joao')
      m2 = MonoStateSimple(sobrenome='Victor')
      print(m2.sobrenome)
 #     print(m1)
 #     print(m2)
