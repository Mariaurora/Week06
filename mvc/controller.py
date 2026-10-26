from mvc.model import Model
import flet as ft


class Controller():
    def __init__(self, model : Model, view : ft.View):
        self._model = model
        self._view = view

    def handler_minus(self, e):
        print("-")
        #v = int(myText.value)
        #v = v-1
        #myText.value = v
        #myText.update()
        self._model.valore = self._model.valore - 1 # -=1
        # Dovrei dire alla view/page di aggiornarsi
        self._view.aggiorna_GUI(self._model.valore)

    def handler_plus(self, e):
        print("+")
        #v = int(myText.value)
        #v = v+1
        #myText.value = v
        #myText.update()
        self._model.valore +=1
        # Dovrei dire alla view/page di aggiornarsi
        self._view.aggiorna_GUI(self._model.valore)
