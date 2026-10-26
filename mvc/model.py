
# Nel pattern MVC il ruolo del model è quello di
# memorizzare i dati (e, essendo una classe, mettere
# a disposizione i metodi per operare su quei dati)
class Model():
    def __init__(self):
        self._valore = 0

    @property
    def valore(self):
        return self._valore
    @valore.setter
    def valore(self, v):
        self._valore = v