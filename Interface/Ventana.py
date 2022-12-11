import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from turtle import fd

class App():
    ALTO = 1325
    ANCHO = 600
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Proyecto1 - LFP")
        self.root.geometry(f'{App.ALTO}x{App.ANCHO}')
        self.root.state('zoomed')
        self.root.configure(bg='#212325')

        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_rowconfigure(0,weight=1)

        self.panelIzq = tk.Frame(master=self.root,width=200)
        self.panelIzq.configure(bg='#2A2D2E')
        self.panelIzq.grid(row=0,column=0,sticky='nswe')

        self.panelDer1 = tk.Frame(master=self.root)
        self.panelDer1.configure(bg='#2A2D2E')
        self.panelDer1.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer2 = tk.Frame(master=self.root)
        self.panelDer2.configure(bg='#2A2D2E')
        self.panelDer2.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer3 = tk.Frame(master=self.root)
        self.panelDer3.configure(bg='#2A2D2E')
        self.panelDer3.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()

        self.panelOpc()
        self.cargarArchivo()
        self.root.mainloop()

    def panelOpc(self):
        self.panelIzq.grid_rowconfigure(0,minsize=10)
        self.panelIzq.grid_rowconfigure(5,weight=1)
        self.panelIzq.grid_rowconfigure(8,minsize=20)
        self.panelIzq.grid_rowconfigure(11,minsize=10)

        self.opciones = tk.Label(master=self.panelIzq,text='Opciones',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        self.opciones.grid(row=1,column=0,pady=10,padx=10)

        self.cargar = tk.Button(master=self.panelIzq,text='Cargar Archivo',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.cargar.grid(row=2,column=0,pady=10,padx=20)

        self.crearAFD = tk.Button(master=self.panelIzq,text='Crear AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.crearAFD.grid(row=3,column=0,pady=10,padx=10)

        self.crearGR = tk.Button(master=self.panelIzq,text='Crear GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1)
        self.crearGR.grid(row=4,column=0,pady=10,padx=10)

        self.crearAFD = tk.Button(master=self.panelIzq,text='Salir',font=('Roboto Medium',11),bg='#D35B58',activebackground='#D35B58',foreground='white',activeforeground='white',width=15,height=1,command=quit)
        self.crearAFD.grid(row=9,column=0,pady=10,padx=10)

    def cargarArchivo(self):
        self.panelDer1.rowconfigure((0,1),weight=1)
        self.panelDer1.rowconfigure(5,weight=10)
        self.panelDer1.columnconfigure((0,1),weight=1)
        self.panelDer1.columnconfigure(5,weight=0)

        self.cargarAFD = tk.Button(master=self.panelDer1,text='Cargar AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.chooseFile)
        self.cargarAFD.grid(row=0,column=0,pady=10,padx=10,sticky='nwe')

        self.cargarAFD = tk.Button(master=self.panelDer1,text='Cargar GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.chooseFile)
        self.cargarAFD.grid(row=0,column=1,pady=10,padx=10,sticky='nwe')

        self.ruta = tk.Entry(master=self.panelDer1,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.ruta.insert(0,'Ruta')
        self.ruta.configure(disabledbackground='#343638',disabledforeground='white',state='disabled')
        self.ruta.grid(row=1,column=0,columnspan=2,pady=15,padx=20,sticky='nwe')

    def chooseFile(self):
        try:
            self.ruta.configure(state=tk.NORMAL)
            formatos = (
                ("form files","*.afd"),
                ("form files","*.grm"),
            )
            archivo = askopenfilename(
                title='Abrir Archivo',
                initialdir='',
                filetypes = formatos)
            #file = open(archivo).read()
            if not archivo == '':
                self.ruta.delete(0,'end')
                self.ruta.insert(0,str(archivo))
                self.ruta.configure(state='disabled')
                extension = archivo.split('.')
                if extension[1] == 'afd':
                    print('se cargó un autómata')
                else:
                    print('se cargó una gramática')
            self.tokens = None
            self.errores = None
        except:
            pass

if __name__ == '__main__':
    app = App()