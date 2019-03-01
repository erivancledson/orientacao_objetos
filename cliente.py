class Cliente:

   def __init__(self, nome):
       self.__nome = nome
   'quando colocar o @property para chamar o get é cliente.nome'
   @property
   def nome(self):
       return self.__nome.title()

   'set desse jeito dessa meneira cliente.nome = "Erivan Costa"'
   @nome.setter
   def nome(self, nome):
       self.__nome = nome