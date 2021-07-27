import pyautogui
import win32api, win32con
from tkinter import *

root = Tk()

segundos_entry = Entry(root)

tp = float(segundos_entry.get())

class teste():
    def gravar(self):
        import mascara
        mascara.lote()


class Aplication(teste):

    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botao()
        root.mainloop()

    def tela(self):
        self.root.title('AUTOMAÇÃO EZCAD')
        self.root.geometry('300x200')
        self.root.resizable(True, True)
        self.root.configure(background='#B0C4DE')
        self.root.maxsize(width=400, height=300)
        self.root.minsize(width=300, height=200)

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg='#F5FFFA', highlightbackground='#87CEFA', highlightthickness=0.5)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.94)

    def botao(self):
        self.bt_iniciar = Button(self.frame1, text='Iniciar', bd=6, bg='#FF0000', fg='white',
                                 font=('verdana', 12, 'bold'), command=lambda: self.gravar())

        self.bt_iniciar.place(relx=0.15, rely=0.50, relwidth=0.7, relheight=0.30)

        # Campo de determinação do tempo de gravação
        self.tempo = Label(self.frame1, text='Tempo de gravação', bg='#F5FFFA', fg='#008B8B',
                           font=('verdana', 8, 'bold'))
        self.tempo.place(relx=0.17, rely=0.30)

        # Campo de preenchimento dos segundos
        self.segundos = Entry(self.frame1, bd=2, bg='#F5FFFA', fg='black', font=('verdana', 10, 'bold'))
        self.segundos.place(relx=0.65, rely=0.28, relwidth=0.15, relheight=0.15)


Aplication()

def gravar():
    import mascara
    mascara.lote()

def click1(x, y):
    import win32api, win32con
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def loop():
    contador = 0
    while contador < 1:
        while True:
            sc = pyautogui.screenshot(region=(489, 300, 108, 92))
            widht, height = sc.size
            for x in range(0, widht, 5):
                for y in range(0, height, 5):
                    r, g, b = sc.getpixel((x, y))
                    if r == 240 and g == 240 and b == 240:
                        contador = contador + 1
                    break
                break
            break


def LOTE1():
    import pyautogui
    import time
    l = int(184)  # y
    coluna = int(332)  # x
    linha = (l)
    cl = coluna
    lin = linha

    def select():
        import time
        import win32api, win32con

        def click(x, y):
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

        time.sleep(tp)
        click(156, 396)
        time.sleep(1)

    def click2():
        win32api.SetCursorPos((cl, lin))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    while lin < 424:
        while True:
            sc = pyautogui.screenshot(region=(489, 300, 108, 92))
            widht, height = sc.size
            for x in range(0, widht, 5):
                for y in range(0, height, 5):
                    r, g, b = sc.getpixel((x, y))
                    print(r, g, b)
                    if r == 240 and g == 240 and b == 240:
                        select()
                        time.sleep(0.1)
                        click2()
                        time.sleep(0.1)
                        click2()
                        lin = lin + 20
                        time.sleep(0.5)

                    break
                break
            break