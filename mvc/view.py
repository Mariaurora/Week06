import flet as ft

class View():

    def __init__(self, page : ft.Page):
        self._page = page
        self._controller = None # Dichiaro la variabile di istanza


    def imposta_controller(self, controller):
        self._controller = controller # La inizializzo qui con la funzione impostaController
        self.inizializza_GUI() # Dopo aver impostato il controller

    def inizializza_GUI(self):
        self._page.window.width = 420
        self._page.window.height = 300
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER

        myBtnMinus = ft.IconButton(icon=ft.Icons.REMOVE,
                                   icon_size=50,
                                   on_click=self._controller.handler_minus)

        myBtnPlus = ft.IconButton(icon=ft.Icons.ADD,
                                  icon_size=50,
                                  on_click=self._controller.handler_plus)

        self._myText = ft.TextField(value=0,
                              disabled=True,
                              width=130,
                              text_size=50,
                              text_align=ft.TextAlign.CENTER
                              )

        # Riga per organizzare i contenuti, allinearli, ...
        myRow = ft.Row([myBtnMinus, self._myText, myBtnPlus],
                       alignment=ft.MainAxisAlignment.CENTER)

        # Riga aggiunta alla lista di controlli della pagina
        self._page.controls.append(myRow)

    def aggiorna_GUI(self, v):
        self._myText.value = v
        self._page.update()