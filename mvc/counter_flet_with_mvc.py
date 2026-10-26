import flet as ft

from model import Model
from view  import View
from controller import Controller

def main(page : ft.Page):

    model = Model()
    view = View(page)

    controller = Controller(model, view)

    view.imposta_controller(controller)



ft.run(main)



