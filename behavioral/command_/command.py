"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

class Ligth:
      # ----> RECEIVER - LUZ INTELIGENTE <---- #
      def __init__(self, name: str, room_name: str) -> None:
            self.name = name
            self.room_name = room_name
            self.collor = 'Default color'

      def on(self) -> None:
            print(f'Light {self.name} in {self.room_name} is now ON')
      
      def off(self) -> None:
            print(f'Light {self.name} in {self.room_name} is now OFF')

      def change_color(self, color: str) -> None:
            self.color = color
            print(f'Light {self.name} in {self.room_name} is now {self.color}')

class ICommand(ABC):
      # ----> INTERFACE DE COMANDO <---- #
      @abstractmethod
      def execute(self) -> None: pass

      @abstractmethod
      def undo(self) -> None: pass

class LigthOnCommand(ICommand):
      # ----> COMANDO CONCRETO <---- #
      def __init__(self, light: Ligth) -> None:
            self.light = light

      def execute(self) -> None:
            self.light.on()

      def undo(self) -> None:
            self.ligth.off()

class RemoteController:
      # ----> INVOKER <---- #
      def __init__(self) -> None:
            self._buttons: Dict[str, ICommand] = {}
      
      def button_add_command(self, name: str, command: ICommand) -> None:
            self._buttons[name] = command