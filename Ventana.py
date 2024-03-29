import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
from idlelib.tooltip import Hovertip
from ControladorAFD import ControladorAFD
from ControladorGR import ControladorGR
from Grafica import Grafica

class App():
    ALTO = 1325
    ANCHO = 600
    def __init__(self):
        self.ctrlAFD = ControladorAFD()
        self.ctrlGR = ControladorGR()
        self.gr = Grafica()

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

        self.panelDer4 = tk.Frame(master=self.root)
        self.panelDer4.configure(bg='#2A2D2E')
        self.panelDer4.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer5 = tk.Frame(master=self.root)
        self.panelDer5.configure(bg='#2A2D2E')
        self.panelDer5.grid(row=0,column=1,sticky="nswe",padx=20,pady=20)

        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer4.grid_remove()
        self.panelDer5.grid_remove()

        self.panelOpc()
        self.panelCargarArchivo()
        self.panelCrearAFD()
        self.panelCrearGR()
        self.panelAyudaAFD()
        self.panelAyudaGR()

    def panelOpc(self):
        self.panelIzq.grid_rowconfigure(0,minsize=10)
        self.panelIzq.grid_rowconfigure(7,weight=1)
        self.panelIzq.grid_rowconfigure(8,minsize=20)
        self.panelIzq.grid_rowconfigure(11,minsize=10)

        self.opciones = tk.Label(master=self.panelIzq,text='Opciones',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        self.opciones.grid(row=1,column=0,pady=10,padx=10)

        self.cargar = tk.Button(master=self.panelIzq,text='Cargar Archivo',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion1)
        self.cargar.grid(row=2,column=0,pady=10,padx=20)

        self.crearAFD = tk.Button(master=self.panelIzq,text='Módulo AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion2)
        self.crearAFD.grid(row=3,column=0,pady=10,padx=10)

        self.crearGR = tk.Button(master=self.panelIzq,text='Módulo GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion3)
        self.crearGR.grid(row=4,column=0,pady=10,padx=10)

        self.ayudaAFD = tk.Button(master=self.panelIzq,text='Ayúda AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion4)
        self.ayudaAFD.grid(row=5,column=0,pady=10,padx=10)

        self.ayudaGR = tk.Button(master=self.panelIzq,text='Ayúda GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.opcion5)
        self.ayudaGR.grid(row=6,column=0,pady=10,padx=10)

        self.salir = tk.Button(master=self.panelIzq,text='Salir',font=('Roboto Medium',11),bg='#D35B58',activebackground='#D35B58',foreground='white',activeforeground='white',width=15,height=1,command=quit)
        self.salir.grid(row=9,column=0,pady=10,padx=10)

    def panelCargarArchivo(self):
        self.panelDer1.rowconfigure((0,1,2,3,4),weight=1)
        self.panelDer1.rowconfigure(5,weight=10)
        self.panelDer1.columnconfigure((0,1),weight=1)
        self.panelDer1.columnconfigure(5,weight=0)

        self.panelD = tk.Frame(master=self.panelDer1)
        self.panelD.configure(bg='#343638')
        self.panelD.grid(row=0,column=0,columnspan=2,sticky="nswe",padx=20,pady=20)
        self.panelDatos()

        self.cargarAFD = tk.Button(master=self.panelDer1,text='Cargar AFD',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.chooseFile)
        self.cargarAFD.grid(row=1,column=0,pady=(20,0),padx=(20,10),sticky='nwe')

        self.cargarAFD = tk.Button(master=self.panelDer1,text='Cargar GR',font=('Roboto Medium',11),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.chooseFile)
        self.cargarAFD.grid(row=1,column=1,pady=(20,0),padx=(10,20),sticky='nwe')

        self.ruta = tk.Entry(master=self.panelDer1,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.ruta.insert(0,'Ruta')
        self.ruta.configure(disabledbackground='#343638',disabledforeground='white',state='disabled')
        self.ruta.grid(row=2,column=0,columnspan=2,padx=20,sticky='nwe')

    def panelDatos(self):
        self.panelD.rowconfigure((0,1),weight=1)
        self.panelD.rowconfigure(2,weight=10)
        self.panelD.columnconfigure((0,1),weight=1)
        self.panelD.columnconfigure(2,weight=0)

        title1 = tk.Label(master=self.panelD,text='Lenguajes Formales y de Programación - N',font=('Roboto Medium',20),background='#343638',foreground='white')
        title1.grid(row=0,column=0,columnspan=2,pady=20,padx=20,sticky='we')

        title1 = tk.Label(master=self.panelD,text='Brandon Tejaxún',font=('Roboto Medium',20),background='#343638',foreground='white')
        title1.grid(row=1,column=0,columnspan=1,pady=20,padx=20,sticky='e')

        title1 = tk.Label(master=self.panelD,text='202112030',font=('Roboto Medium',20),background='#343638',foreground='white')
        title1.grid(row=1,column=1,columnspan=1,pady=20,padx=20,sticky='w')

    def panelCrearAFD(self):
        self.panelDer2.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
        self.panelDer2.rowconfigure(13,weight=10)
        self.panelDer2.columnconfigure((0,1,2,3),weight=1)
        self.panelDer2.columnconfigure(4,weight=0)

        title1 = tk.Label(master=self.panelDer2,text='Crear Autómata Finito Determinista',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        title1.grid(row=0,column=0,columnspan=4,pady=(15,0),padx=20,sticky='w')

        nombre = tk.Label(master=self.panelDer2,text='Nombre: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        nombre.grid(row=1,column=0,padx=20,sticky='nw')

        self.nombreAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.nombreAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.nombreAFD.grid(row=2,column=0,columnspan=2,padx=20,sticky='nwe')

        estados = tk.Label(master=self.panelDer2,text='Estados: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        estados.grid(row=1,column=2,padx=20,sticky='nw')

        self.estadosAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.estadosAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.estadosAFD.grid(row=2,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.estadosAFD,'Ejemplo: A;B;C;D (Separados por punto y coma)')

        alfabeto = tk.Label(master=self.panelDer2,text='Alfabeto: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        alfabeto.grid(row=3,column=0,padx=20,sticky='nw')

        self.alfabetoAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.alfabetoAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.alfabetoAFD.grid(row=4,column=0,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.alfabetoAFD,'Ejemplo: 0;1;2 (Separados por punto y coma)')

        eIni = tk.Label(master=self.panelDer2,text='Estado Inicial: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        eIni.grid(row=3,column=2,padx=20,sticky='nw')

        self.eInicialAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.eInicialAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.eInicialAFD.grid(row=4,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.eInicialAFD,'El estado inicial debe existir en los estados')

        eAcept = tk.Label(master=self.panelDer2,text='Estados de Aceptación: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        eAcept.grid(row=5,column=0,padx=20,sticky='nw')

        self.eAceptAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.eAceptAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.eAceptAFD.grid(row=6,column=0,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.eAceptAFD,'Ejemplo: A;B;C (Separados por punto y coma)')

        transiciones = tk.Label(master=self.panelDer2,text='Transiciones: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        transiciones.grid(row=5,column=2,padx=20,sticky='nw')

        self.transiAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.transiAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.transiAFD.grid(row=6,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.transiAFD,'Ejemplo: A,0,B;A,1,C - origen,entrada,destino ; origen,entrada,destino')

        self.guardarAFD = tk.Button(master=self.panelDer2,text='Guardar AFD',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.agregarAFD)
        self.guardarAFD.grid(row=7,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nwe')

        # ====================
        self.validacionesAFD()

    def validacionesAFD(self):
        self.tituloAFD = tk.Label(master=self.panelDer2,text='Alfabeto del AFD: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        self.tituloAFD.grid(row=8,column=2,padx=20,sticky='sw')

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#343638", background= "#fff", selectforeground='white',activebackground='#343638',activeforeground='black',foreground='white')

        self.cbAFD = ttk.Combobox(master=self.panelDer2,values=[],font=('Roboto Medium',16))
        self.cbAFD.bind('<<ComboboxSelected>>',self.verAlfabeto)
        self.cbAFD.grid(row=9,column=0,columnspan=2,padx=20,pady=(10,10),sticky='we')
        self.cbAFD.set('Seleccione un AFD')

        self.cadenaAFD = tk.Entry(master=self.panelDer2,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.cadenaAFD.configure(disabledbackground='#343638',disabledforeground='white')
        self.cadenaAFD.grid(row=9,column=2,columnspan=2,padx=20,pady=(10,10),sticky='we')
        self.agregarNota(self.cadenaAFD,'Ingrese una cadena para validar el AFD')

        self.generarReporteAFD = tk.Button(master=self.panelDer2,text='Generar Reporte',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.generarReportePdfAFD)
        self.generarReporteAFD.grid(row=10,column=0,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

        self.validarCadAFD = tk.Button(master=self.panelDer2,text='Validar Cadena',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.validarCadenaAFD)
        self.validarCadAFD.grid(row=10,column=2,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

        self.rutaAFD = tk.Button(master=self.panelDer2,text='Mostrar Ruta',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.generarRutaAFD)
        self.rutaAFD.grid(row=11,column=2,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

    def agregarAFD(self):
        if self.nombreAFD.get().replace(' ','') == '' or self.estadosAFD.get().replace(' ','') == '' or self.alfabetoAFD.get().replace(' ','') == '' or self.eInicialAFD.get().replace(' ','') == '' or self.eAceptAFD.get().replace(' ','') == '' or self.transiAFD.get().replace(' ','') == '':
            messagebox.showinfo('Información','Todos los campos son obligatorios')  
        else:
            for simbolo in self.alfabetoAFD.get().split(';'):
                for estado in self.estadosAFD.get().split(';'):
                    if str(simbolo) == str(estado):
                        messagebox.showinfo('Información',f'El simbolo {simbolo} es parte de los estados')
                        return
            dup = [x for i, x in enumerate(self.alfabetoAFD.get().split(';')) if x in self.alfabetoAFD.get().split(';')[:i]]
            if len(dup) > 0:
                messagebox.showinfo('Información',f'El alfabeto contiene elementos repetidos {dup}')
                return

            self.dic = {}

            for estado in self.estadosAFD.get().split(';'):
                self.dic[estado] = {}

            transiciones = self.transiAFD.get().split(';')
            for transicion in transiciones:
                transicion = transicion.split(',')
                transicion[0] = transicion[0].replace(' ','')
                expresiones = []
                expresiones.append(transicion[1])
                expresiones.append(transicion[2])
                transicion.pop(2)
                transicion[1] = expresiones

                try:
                    self.dic[transicion[0]][transicion[1][0]] = transicion[1][1]
                except:
                    pass
            
            estados = []
            alfabeto = []
            for estado,value in self.dic.items():
                estados.append(estado)
                for entrada,destino in value.items():
                    if not entrada in alfabeto:
                        alfabeto.append(entrada)

            for estado,value in self.dic.items():
                for entrada,destino in value.items():
                    if not destino in estados:
                        estados.append(destino)

            for estado in estados:
                if not estado in self.estadosAFD.get().split(';'):
                    messagebox.showinfo('Información',f'El estado {estado} no ha sido declarado')
                    return
            for entrada in alfabeto:
                if not entrada in self.alfabetoAFD.get().split(';'):
                    messagebox.showinfo('Información',f'El simbolo {entrada} no ha sido declarado como parte del alfabeto')
                    return

            if not self.eInicialAFD.get() in self.estadosAFD.get().split(';'):
                messagebox.showinfo('Información',f'El estado inicial {self.eInicialAFD.get()} no es parte de los estados')
            elif set(self.eAceptAFD.get().split(';')).difference(set(self.estadosAFD.get().split(';'))):
                if len(set(self.eAceptAFD.get().split(';')).difference(set(self.estadosAFD.get().split(';')))) >= 2:
                    messagebox.showinfo('Información',f"Los estados de aceptación {set(self.eAceptAFD.get().split(';')).difference(set(self.estadosAFD.get().split(';')))} no han sido declarados")
                else:
                    messagebox.showinfo('Información',f"El estado de aceptación {set(self.eAceptAFD.get().split(';')).difference(set(self.estadosAFD.get().split(';')))} no han sido declarado")
            else:
                if self.ctrlAFD.agregarAFD(self.nombreAFD.get(),self.estadosAFD.get(),self.alfabetoAFD.get(),self.eInicialAFD.get(),self.eAceptAFD.get(),self.transiAFD.get().split(';'),self.dic):
                    messagebox.showinfo('Información','Autómata creado exitosamente')
                    #self.ctrlAFD.verAutomatas()
                    self.limpiarFormAFD()
                    self.nombAFD = []
                    for i in range(len(self.ctrlAFD.automatas)):
                        self.nombAFD.append(f'{i + 1} - {self.ctrlAFD.automatas[i].nombreAFD}')
                    self.cbAFD.configure(values=self.nombAFD)
                else:
                    messagebox.showerror('Error','El Autómata no es determinista')
                    self.dic = {}

    def generarReportePdfAFD(self):
        if self.cbAFD.get() == 'Seleccione un AFD':
            messagebox.showinfo('Información','No se ha seleccionado ningún Autómata')
        else:
            cadena = self.cbAFD.get().split(' - ')
            indice = int(cadena[0]) - 1
            self.ctrlAFD.generarReporte(indice)
            self.cadenaAFD.delete(0,'end')
            self.tituloAFD.configure(text=f'Alfabeto del AFD:')
            self.cbAFD.set('Seleccione un AFD')

    def validarCadenaAFD(self):
        if self.cbAFD.get() == 'Seleccione un AFD':
            messagebox.showinfo('Información','No se ha seleccionado ningún Autómata')
        else:
            afd = self.cbAFD.get().split(' - ')
            indice = int(afd[0]) - 1
            if self.ctrlAFD.validarCadena(self.cadenaAFD.get(),indice):
                messagebox.showinfo('Información',f'La cadena es válida')
            else:
                messagebox.showerror('Error','La cadena no es válida')

    def generarRutaAFD(self):
        if self.cbAFD.get() == 'Seleccione un AFD':
            messagebox.showinfo('Información','No se ha seleccionado ningún Autómata')
        else:
            afd = self.cbAFD.get().split(' - ')
            indice = int(afd[0]) - 1
            if self.ctrlAFD.validarCadena(self.cadenaAFD.get(),indice):
                self.ctrlAFD.generarRuta(self.cadenaAFD.get(),indice)
            else:
                messagebox.showerror('Error','La cadena no es válida')

    def panelCrearGR(self):
        self.panelDer3.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
        self.panelDer3.rowconfigure(13,weight=10)
        self.panelDer3.columnconfigure((0,1,2,3),weight=1)
        self.panelDer3.columnconfigure(4,weight=0)

        title1 = tk.Label(master=self.panelDer3,text='Crear Gramática Regular',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        title1.grid(row=0,column=0,columnspan=4,pady=(15,0),padx=20,sticky='w')

        nombre = tk.Label(master=self.panelDer3,text='Nombre: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        nombre.grid(row=1,column=0,padx=20,sticky='nw')

        self.nombreGR = tk.Entry(master=self.panelDer3,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.nombreGR.configure(disabledbackground='#343638',disabledforeground='white')
        self.nombreGR.grid(row=2,column=0,columnspan=2,padx=20,sticky='nwe')

        noTerminales = tk.Label(master=self.panelDer3,text='No Terminales: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        noTerminales.grid(row=1,column=2,padx=20,sticky='nw')

        self.noTerminalesGR = tk.Entry(master=self.panelDer3,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.noTerminalesGR.configure(disabledbackground='#343638',disabledforeground='white')
        self.noTerminalesGR.grid(row=2,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.noTerminalesGR,'Ejemplo: A;B;C;D (Separados por punto y coma)')

        terminales = tk.Label(master=self.panelDer3,text='Terminales: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        terminales.grid(row=3,column=0,padx=20,sticky='nw')

        self.terminalesGR = tk.Entry(master=self.panelDer3,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.terminalesGR.configure(disabledbackground='#343638',disabledforeground='white')
        self.terminalesGR.grid(row=4,column=0,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.terminalesGR,'Ejemplo: 0;1;2 (Separados por punto y coma)')

        noTerminalInicial = tk.Label(master=self.panelDer3,text='No Terminal Inicial: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        noTerminalInicial.grid(row=3,column=2,padx=20,sticky='nw')

        self.noTermIniGR = tk.Entry(master=self.panelDer3,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.noTermIniGR.configure(disabledbackground='#343638',disabledforeground='white')
        self.noTermIniGR.grid(row=4,column=2,columnspan=2,padx=20,sticky='nwe')
        self.agregarNota(self.noTermIniGR,'El estado inicial debe existir en los estados')

        producciones = tk.Label(master=self.panelDer3,text='Producciones: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        producciones.grid(row=5,column=0,padx=20,sticky='nw')

        self.producGR = tk.Entry(master=self.panelDer3,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.producGR.configure(disabledbackground='#343638',disabledforeground='white')
        self.producGR.grid(row=6,column=0,columnspan=4,padx=20,sticky='nwe')
        self.agregarNota(self.producGR,'Ejemplo: A > 0 B;A > 1 C - No terminal > Expresión ; Expresión;No terminal > Expresión')

        self.guardarGR = tk.Button(master=self.panelDer3,text='Guardar GR',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.agregarGR)
        self.guardarGR.grid(row=7,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nwe')

        self.guardarGR = tk.Button(master=self.panelDer3,text='Guardar GR',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.agregarGR)
        self.guardarGR.grid(row=7,column=0,columnspan=4,pady=(20,0),padx=20,sticky='nwe')

        # ====================
        self.validacionesGR()

    def validacionesGR(self):
        self.tituloGR = tk.Label(master=self.panelDer3,text='Terminales de la GR: ',font=('Roboto Medium',16),background='#2A2D2E',foreground='white')
        self.tituloGR.grid(row=8,column=2,padx=20,sticky='sw')

        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "#343638", background= "#fff", selectforeground='white',activebackground='#343638',activeforeground='black',foreground='white')

        self.nombGR = []
        self.cbGR = ttk.Combobox(master=self.panelDer3,values=[],font=('Roboto Medium',16))
        self.cbGR.bind('<<ComboboxSelected>>',self.verTerminales)
        self.cbGR.grid(row=9,column=0,columnspan=2,padx=20,pady=(10,10),sticky='we')
        self.cbGR.set('Seleccione una GR')

        self.cadenaGR = tk.Entry(master=self.panelDer3,width=120,bg='#343638',foreground='white',font=('Roboto Medium',16))
        self.cadenaGR.configure(disabledbackground='#343638',disabledforeground='white')
        self.cadenaGR.grid(row=9,column=2,columnspan=2,padx=20,pady=(10,10),sticky='we')
        self.agregarNota(self.cadenaGR,'Ingrese una cadena para validar la GR')

        self.generarReporteGR = tk.Button(master=self.panelDer3,text='Generar Reporte',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.generarReportePdfGR)
        self.generarReporteGR.grid(row=10,column=0,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

        self.validarCadGR = tk.Button(master=self.panelDer3,text='Validar Cadena',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.validarCadenaGR)
        self.validarCadGR.grid(row=10,column=2,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

        self.rutaGR = tk.Button(master=self.panelDer3,text='Mostrar Ruta',font=('Roboto Medium',15),bg='#0059b3',activebackground='#0059b3',foreground='white',activeforeground='white',width=15,height=1,command=self.generarRutaGR)
        self.rutaGR.grid(row=11,column=2,columnspan=2,pady=(20,0),padx=20,sticky='nwe')

    def agregarGR(self):
        if self.nombreGR.get().replace(' ','') == '' or self.noTerminalesGR.get().replace(' ','') == '' or self.terminalesGR.get().replace(' ','') == '' or self.noTermIniGR.get().replace(' ','') == '' or self.producGR.get().replace(' ','') == '':
            messagebox.showinfo('Información','Todos los campos son obligatorios')  
        else:
            if not self.noTermIniGR.get() in self.noTerminalesGR.get().split(';'):
                messagebox.showinfo('Información','El no terminal inicial no está declaro en los no terminales')
                return
            dup = []
            dup = [x for i, x in enumerate(self.noTerminalesGR.get().split(';')) if x in self.noTerminalesGR.get().split(';')[:i]]
            if len(dup) > 0:
                messagebox.showinfo('Información',f'Los no terminales contienen elementos repetidos {dup}')
                return
            for estado in self.noTerminalesGR.get().split(';'):
                for simbolo in self.terminalesGR.get().split(';'):
                    if str(estado) == str(simbolo):
                        messagebox.showinfo('Información',f'El terminal {simbolo} es parte de los no terminales')
                        return
            dup = []
            dup = [x for i, x in enumerate(self.terminalesGR.get().split(';')) if x in self.terminalesGR.get().split(';')[:i]]
            if len(dup) > 0:
                messagebox.showinfo('Información',f'Los terminales contienen elementos repetidos {dup}')
                return

            #A > 0 B;A > 1 C;B > 0 A;B > 1 D;C > 0 D;C > 1 A;C > $;D > 0 C;D > 1 B
            self.dic = {}
            producciones = self.producGR.get().split(';')
            for produccion in producciones:
                produccion = produccion.split('>')
                produccion[0] = produccion[0].replace(' ','')
                expresiones = produccion[1].split(' ')
                expresiones = [s for s in expresiones if s]
                produccion[1] = expresiones

                if not self.existeEstado(produccion[0]):
                    self.dic[produccion[0]] = {}

                try:
                    self.dic[produccion[0]][produccion[1][0]] = produccion[1][1]
                except:
                    self.dic[produccion[0]][produccion[1][0]] = 'ACEPTADO'

            #print(dic)
            noTerm = []
            termin = []
            eAcept = []
            for estado,value in self.dic.items():
                noTerm.append(estado)
                for entrada,destino in value.items():
                    if entrada != '$':
                        if not entrada in termin:
                            termin.append(entrada)
                    elif entrada == '$':
                        eAcept.append(estado)
            for estado,value in self.dic.items():
                for entrada,destino in value.items():
                    if entrada != '$':
                        if not entrada in termin:
                            termin.append(entrada)
                        elif not destino in noTerm:
                            noTerm.append(destino)

            for estado in noTerm:
                if not estado in self.noTerminalesGR.get().split(';'):
                    messagebox.showinfo('Información',f'El no terminal {estado} no han sido declarado')
                    return
            for entrada in termin:
                if not entrada in self.terminalesGR.get().split(';'):
                    messagebox.showinfo('Información',f'El terminal {entrada} no han sido declarado')
                    return
            
            self.ctrlGR.agregarGramatica(self.nombreGR.get(),self.noTerminalesGR.get(),eAcept,self.terminalesGR.get(),self.noTermIniGR.get(),self.dic)
            messagebox.showinfo('Información','Gramática creada exitosamente')
            self.limpiarFormGR()
            #self.ctrlGR.verGramaticas()
            self.nombGR = []
            for i in range(len(self.ctrlGR.gramaticas)):
                self.nombGR.append(f'{i + 1} - {self.ctrlGR.gramaticas[i].nombreGR}')
            self.cbGR.configure(values=self.nombGR)

    def existeEstado(self,nuevo):
        for estado in self.dic:
            if nuevo == estado:
                return True
        return False

    def generarReportePdfGR(self):
        if self.cbGR.get() == 'Seleccione una GR':
            messagebox.showinfo('Información','No se ha seleccionado ninguna gramática')
        else:
            cadena = self.cbGR.get().split(' - ')
            indice = int(cadena[0]) - 1
            self.ctrlGR.generarReporte(indice)
            self.cbGR.set('Seleccione una GR')
            self.tituloGR.configure(text='Terminales de la GR:')

    def validarCadenaGR(self):
        if self.cbGR.get() == 'Seleccione una GR':
            messagebox.showinfo('Información','No se ha seleccionado ninguna Gramática')
        else:
            gr = self.cbGR.get().split(' - ')
            indice = int(gr[0]) - 1
            if self.ctrlGR.validarCadena(self.cadenaGR.get(),indice):
                messagebox.showinfo('Información',f'La cadena es válida')
            else:
                messagebox.showerror('Error','La cadena no es válida')

    def generarRutaGR(self):
        if self.cbGR.get() == 'Seleccione una GR':
            messagebox.showinfo('Información','No se ha seleccionado ninguna Gramática')
        else:
            gr = self.cbGR.get().split(' - ')
            indice = int(gr[0]) - 1
            if self.ctrlGR.validarCadena(self.cadenaGR.get(),indice):
                self.ctrlGR.generarRuta(self.cadenaGR.get(),indice)
            else:
                messagebox.showerror('Error','La cadena no es valida')

    def panelAyudaAFD(self):
        self.panelDer4.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
        self.panelDer4.rowconfigure(13,weight=10)
        self.panelDer4.columnconfigure((0,1,2,3),weight=1)
        self.panelDer4.columnconfigure(4,weight=0)

        texto = tk.Label(master=self.panelDer4,text='¿Qué es un Autómata Finito Determinista - AFD?',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        texto.grid(row=0,column=0,columnspan=4,pady=(15,0),padx=20,sticky='we')

        texto = tk.Label(master=self.panelDer4,text='Un AFD tiene un conjunto finito de estados y un conjunto finito de símbolos de entrada. El término “determinista”\nhace referencia al hecho de que para cada entrada sólo existe uno y sólo un estado al que el autómata puede hacer\nla transición a partir de su estado actual. Un estado se diseña para que sea el estado inicial, y cero o más\nestados para que sean estados de aceptación. Una función de transición determina cómo cambia el estado cada vez\nque se procesa un símbolo de entrada.',font=('Roboto Medium',15),background='#2A2D2E',foreground='white')
        texto.grid(row=1,column=0,columnspan=4,rowspan=1,pady=(15,0),padx=20,sticky='wen')

        imagen = Image.open('images/afd.png')
        imagen = imagen.resize((500,400),Image.ANTIALIAS)
        imagen = ImageTk.PhotoImage(imagen)
        
        canva = Canvas(self.panelDer4)
        label = Label(self.panelDer4,image=imagen)
        label.img = imagen
        label.grid(row=3,column=0,columnspan=4,padx=20,pady=20)

    def panelAyudaGR(self):
        self.panelDer5.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
        self.panelDer5.rowconfigure(13,weight=10)
        self.panelDer5.columnconfigure((0,1,2,3),weight=1)
        self.panelDer5.columnconfigure(4,weight=0)

        texto = tk.Label(master=self.panelDer5,text='¿Qué es una Gramática Regular - GR?',font=('Roboto Medium',20),background='#2A2D2E',foreground='white')
        texto.grid(row=0,column=0,columnspan=4,pady=(15,0),padx=20,sticky='we')

        texto = tk.Label(master=self.panelDer5,text='Una gramática regular es un cuádruplo (V, Σ, R, S) en donde:\nV es un alfabeto de variables\nΣ es un alfabeto de constantes\nR, el conjunto de reglas, es un subconjunto finito de V × (ΣV ∪ Σ)\nS, el símbolo inicial, es un elemento de V',font=('Roboto Medium',15),background='#2A2D2E',foreground='white')
        texto.grid(row=1,column=0,columnspan=4,rowspan=1,pady=(15,0),padx=20,sticky='wen')

        imagen = Image.open('images/gr.png')
        imagen = imagen.resize((500,400),Image.ANTIALIAS)
        imagen = ImageTk.PhotoImage(imagen)
        
        canva = Canvas(self.panelDer5)
        label = Label(self.panelDer5,image=imagen)
        label.img = imagen
        label.grid(row=3,column=0,columnspan=4,padx=20,pady=20)

    def opcion1(self):
        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer4.grid_remove()
        self.panelDer5.grid_remove()
        self.panelDer1.grid()

    def opcion2(self):
        self.panelDer1.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer4.grid_remove()
        self.panelDer5.grid_remove()
        self.panelDer2.grid()

    def opcion3(self):
        self.panelDer1.grid_remove()
        self.panelDer2.grid_remove()
        self.panelDer4.grid_remove()
        self.panelDer5.grid_remove()
        self.panelDer3.grid()

    def opcion4(self):
        self.panelDer1.grid_remove()
        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer5.grid_remove()
        self.panelDer4.grid()

    def opcion5(self):
        self.panelDer1.grid_remove()
        self.panelDer2.grid_remove()
        self.panelDer3.grid_remove()
        self.panelDer4.grid_remove()
        self.panelDer5.grid()

    def chooseFile(self):
        try:
            self.ruta.configure(state=tk.NORMAL)
            formatos = (
                ("form files","*.afd"),
                ("form files","*.gre"),
            )
            archivo = askopenfilename(
                title='Abrir Archivo',
                initialdir='',
                filetypes = formatos)
            if not archivo == '':
                self.ruta.delete(0,'end')
                self.ruta.insert(0,str(archivo))
                self.ruta.configure(state='disabled')
                extension = archivo.split('.')
                if extension[1] == 'afd':
                    self.ctrlAFD.leerArchivo(archivo)
                    self.ctrlAFD.reconocimientoAutomata()
                    self.nombAFD = []
                    for i in range(len(self.ctrlAFD.automatas)):
                        self.nombAFD.append(f'{i + 1} - {self.ctrlAFD.automatas[i].nombreAFD}')
                    self.cbAFD.configure(values=self.nombAFD)
                elif extension[1] == 'gre':
                    self.ctrlGR.leerArchivo(archivo)
                    self.ctrlGR.reconocimientoGramatica()
                    self.nombGR = []
                    for i in range(len(self.ctrlGR.gramaticas)):
                        self.nombGR.append(f'{i + 1} - {self.ctrlGR.gramaticas[i].nombreGR}')
                    self.cbGR.configure(values=self.nombGR)
                else:
                    pass
        except:
            pass

    def agregarNota(self,componente,texto):
        self.myTip = Hovertip(componente,f'\n     {texto}     \n')

    def limpiarFormAFD(self):
        self.nombreAFD.delete(0,'end')
        self.estadosAFD.delete(0,'end')
        self.alfabetoAFD.delete(0,'end')
        self.eInicialAFD.delete(0,'end')
        self.eAceptAFD.delete(0,'end')
        self.transiAFD.delete(0,'end')

    def limpiarFormGR(self):
        self.nombreGR.delete(0,'end')
        self.noTerminalesGR.delete(0,'end')
        self.terminalesGR.delete(0,'end')
        self.noTermIniGR.delete(0,'end')
        self.producGR.delete(0,'end')

    def verAlfabeto(self,event):
        indice = int(self.cbAFD.get().split(' - ')[0]) - 1
        self.tituloAFD.configure(text=f'Alfabeto del AFD: {self.ctrlAFD.obtenerAlfabeto(indice)}')

    def verTerminales(self,event):
        indice = int(self.cbGR.get().split(' - ')[0]) - 1
        self.tituloGR.configure(text=f'Terminales de la GR: {self.ctrlGR.obtenerTerminales(indice)}')

if __name__ == '__main__':
    app = App()
    #self.root.mainloop()
    app.root.mainloop()