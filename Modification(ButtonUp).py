
#!Codigo Creado Por David Ruiz Velazquez. T2
#!Codigo Creado Por David Ruiz Velazquez. T2
#!Codigo Creado Por David Ruiz Velazquez. T2



import wx

class ParKingDavidRuizVelazquez(wx.Frame):
    def __init__(self, *args, **kwds):
        
        
        

        # begin wxGlade: ParKingDavidRuizVelazquez.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((510, 497))
        self.SetTitle("ParKing-DavidRuizVelazquez")
        self.Centre() #!Centra la ventana emergente en el Medio 
        self.SetBackgroundColour(wx.Colour(196, 242, 240))

        #Todo:Sino existe el archivo record lo crea con su sintaxix correspondiente
        try:
            f = open("records.txt","r")
        except FileNotFoundError: #!error si no se encuentra el archivo y le crea
            print("Error: No se encuentra el archivo record.txt, se procede a crear uno nuevo")
            f = open("records.txt","w")
            f.write("0000000000000000000000000000000000000000000000000000")

    
        
       

        SizerV = wx.BoxSizer(wx.VERTICAL)

        SizerH = wx.BoxSizer(wx.HORIZONTAL)
        SizerV.Add(SizerH, 1, 0, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        SizerH.Add(sizer_6, 1, wx.EXPAND, 0)

        TxtInfoSelectLvl = wx.StaticText(self, wx.ID_ANY, "Seleccione Un Nivel!\n")
        sizer_6.Add(TxtInfoSelectLvl, 0, wx.LEFT | wx.SHAPED | wx.TOP, 5)

        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)


        
    

        #Todo: Indica la cantidad de niveles disponibles a jugar segun el archivo de records
        ParKingDavidRuizVelazquez.ObtenciolistaRecord(self)
        self.cantidadNiveles = 0
        for i in self.listaRecord:
            if i == "-": #!Cada '-' que detecta es que hay un nivel disponible a jugar 
                self.cantidadNiveles+=1
        
        

        #Todo:Encargado de Mostrar solo los ninveles posibles en cada momento segun los records
        # if self.cantidadNiveles == 0: #!basicamente segun la cantidad de esteriscos que tengan los records escribe los Niveles necesarios en la listoBox
        self.List_Lvl = wx.ListBox(self, wx.ID_ANY, choices=[])
        sizer_7.Add(self.List_Lvl, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        try:
            ParKingDavidRuizVelazquez.GetPointsLabel(self)   #!obtiene un array con los records de cada nivel
            ParKingDavidRuizVelazquez.listBoxClear(self)  #!Añade el label con los records
        except Exception:
            print("Vuelva a abrirlo por favor")  #! si no se encuntra el archivo se cierra y se crean los records
            self.Close()
        
        
        
        
        
        
        #!Fin de MostrarLista segun los records
            

        self.StartButton = wx.Button(self, wx.ID_ANY, "Comenzar!")
        sizer_6.Add(self.StartButton, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 39)

        self.UndoButton = wx.Button(self, wx.ID_ANY, "Deshacer!")
        sizer_6.Add(self.UndoButton, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 15)

        self.botonArrriba = wx.Button(self, wx.ID_ANY, "Arriba!")
        sizer_6.Add(self.botonArrriba, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 15)
        
        TimerTxt = wx.StaticText(self, wx.ID_ANY, "Tiempo Restante")
        TimerTxt.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_6.Add(TimerTxt, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 32)

        self.TimerOutPut = wx.StaticText(self, wx.ID_ANY, "90\n", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.TimerOutPut.SetFont(wx.Font(59, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.TimerOutPut, 1, wx.EXPAND, 0)

        SizerGrind = wx.GridSizer(8, 8, 0, 0)
        SizerH.Add(SizerGrind, 3, wx.ALL | wx.EXPAND, 15)

        self.Borde1 =wx.Panel(self, wx.ID_ANY)  
        self.Borde1.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde1, 1, wx.EXPAND, 0)

        self.Borde2 = wx.Panel(self, wx.ID_ANY)  
        self.Borde2.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde2, 1, wx.EXPAND, 0)

        self.Borde3 =wx.Panel(self, wx.ID_ANY)  
        self.Borde3.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde3, 1, wx.EXPAND, 0)

        self.Borde4 = wx.Panel(self, wx.ID_ANY)  
        self.Borde4.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde4, 1, wx.EXPAND, 0)

        self.Borde5 = wx.Panel(self, wx.ID_ANY)  
        self.Borde5.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde5, 1, wx.EXPAND, 0)

        self.Borde6 = wx.Panel(self, wx.ID_ANY)  
        self.Borde6.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde6, 1, wx.EXPAND, 0)

        self.Borde7 =wx.Panel(self, wx.ID_ANY)  
        self.Borde7.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde7, 1, wx.EXPAND, 0)

        self.Borde8 = wx.Panel(self, wx.ID_ANY)  
        self.Borde8.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde8, 1, wx.EXPAND, 0)

        self.Borde9 = wx.Panel(self, wx.ID_ANY)  
        self.Borde9.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde9, 1, wx.EXPAND, 0)

        self.Coche00 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche00, 0, wx.EXPAND, 0)

        self.Coche01 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche01, 0, wx.EXPAND, 0)

        self.Coche02 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche02, 0, wx.EXPAND, 0)

        self.Coche03 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche03, 0, wx.EXPAND, 0)

        self.Coche04 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche04, 0, wx.EXPAND, 0)

        self.Coche05 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche05, 0, wx.EXPAND, 0)

        self.Borde10 = wx.Panel(self, wx.ID_ANY)  
        self.Borde10.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde10, 1, wx.EXPAND, 0)

        self.Borde11 = wx.Panel(self, wx.ID_ANY)  
        self.Borde11.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde11, 1, wx.EXPAND, 0)

        self.Coche10 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche10, 0, wx.EXPAND, 0)

        self.Coche11 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche11, 0, wx.EXPAND, 0)

        self.Coche12 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche12, 0, wx.EXPAND, 0)

        self.Coche13 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche13, 0, wx.EXPAND, 0)

        self.Coche14 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche14, 0, wx.EXPAND, 0)

        self.Coche15 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche15, 0, wx.EXPAND, 0)

        self.Borde12 =wx.Panel(self, wx.ID_ANY)  
        self.Borde12.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde12, 1, wx.EXPAND, 0)

        self.Borde13 = wx.Panel(self, wx.ID_ANY)  
        self.Borde13.SetBackgroundColour(wx.Colour(0, 0 , 0))
        SizerGrind.Add(self.Borde13, 1, wx.EXPAND, 0)

        self.Coche20 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche20, 0, wx.EXPAND, 0)

        self.Coche21 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche21, 0, wx.EXPAND, 0)

        self.Coche22 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche22, 0, wx.EXPAND, 0)

        self.Coche23 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche23, 0, wx.EXPAND, 0)

        self.Coche24 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche24, 0, wx.EXPAND, 0)

        self.Coche25 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche25, 0, wx.EXPAND, 0)

        self.BordeSalida = wx.Panel(self, wx.ID_ANY)    
        self.BordeSalida.SetBackgroundColour(wx.Colour(196, 242, 240))
        SizerGrind.Add(self.BordeSalida, 1, wx.EXPAND, 0)

        self.Borde15 = wx.Panel(self, wx.ID_ANY)  
        self.Borde15.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde15, 1, wx.EXPAND, 0)

        self.Coche30 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche30, 0, wx.EXPAND, 0)

        self.Coche31 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche31, 0, wx.EXPAND, 0)

        self.Coche32 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche32, 0, wx.EXPAND, 0)

        self.Coche33 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche33, 0, wx.EXPAND, 0)

        self.Coche34 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche34, 0, wx.EXPAND, 0)

        self.Coche35 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche35, 0, wx.EXPAND, 0)

        self.Borde16 = wx.Panel(self, wx.ID_ANY)  
        self.Borde16.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde16, 1, wx.EXPAND, 0)

        self.Borde17 = wx.Panel(self, wx.ID_ANY)  
        self.Borde17.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde17, 1, wx.EXPAND, 0)

        self.Coche40 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche40, 0, wx.EXPAND, 0)

        self.Coche41 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche41, 0, wx.EXPAND, 0)

        self.Coche42 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche42, 0, wx.EXPAND, 0)

        self.Coche43 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche43, 0, wx.EXPAND, 0)

        self.Coche44 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche44, 0, wx.EXPAND, 0)

        self.Coche45 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche45, 0, wx.EXPAND, 0)

        self.Borde18 = wx.Panel(self, wx.ID_ANY)  
        self.Borde18.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde18, 1, wx.EXPAND, 0)

        self.Borde19 = wx.Panel(self, wx.ID_ANY)  
        self.Borde19.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde19, 1, wx.EXPAND, 0)

        self.Coche50 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche50, 0, wx.EXPAND, 0)

        self.Coche51 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche51, 0, wx.EXPAND, 0)

        self.Coche52 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche52, 0, wx.EXPAND, 0)

        self.Coche53 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche53, 0, wx.EXPAND, 0)

        self.Coche54 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche54, 0, wx.EXPAND, 0)

        self.Coche55 = wx.Button(self, wx.ID_ANY, "\n")
        SizerGrind.Add(self.Coche55, 0, wx.EXPAND, 0)

        self.Borde20 = wx.Panel(self, wx.ID_ANY)  
        self.Borde20.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde20, 1, wx.EXPAND, 0)

        self.Borde21 = wx.Panel(self, wx.ID_ANY)  
        self.Borde21.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde21, 1, wx.EXPAND, 0)

        self.Borde22 = wx.Panel(self, wx.ID_ANY)  
        self.Borde22.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde22, 1, wx.EXPAND, 0)

        self.Borde23 = wx.Panel(self, wx.ID_ANY)  
        self.Borde23.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde23, 1, wx.EXPAND, 0)

        self.Borde24 = wx.Panel(self, wx.ID_ANY)  
        self.Borde24.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde24, 1, wx.EXPAND, 0)

        self.Borde25 = wx.Panel(self, wx.ID_ANY)  
        self.Borde25.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde25, 1, wx.EXPAND, 0)

        self.Borde26 = wx.Panel(self, wx.ID_ANY)  
        self.Borde26.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde26, 1, wx.EXPAND, 0)

        self.Borde27 = wx.Panel(self, wx.ID_ANY)  
        self.Borde27.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde27, 1, wx.EXPAND, 0)

        self.Borde28 = wx.Panel(self, wx.ID_ANY)  
        self.Borde28.SetBackgroundColour(wx.Colour(0, 0, 0))
        SizerGrind.Add(self.Borde28, 1, wx.EXPAND, 0)

        self.infoTxt = wx.StaticText(self, wx.ID_ANY, u"Seleccione un Nivel.", wx.DefaultPosition, wx.DefaultSize, 0)
        self.infoTxt.SetFont(wx.Font(10, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        SizerV.Add(self.infoTxt, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, 50)
    
#Todo: asginaccion a self.timer el wx.timer
        self.timer = wx.Timer(self) #!wx.timer
    


        self.SetSizer(SizerV)

        self.Layout()

    #Todo:Binds de eventos con su respectivo starter
        self.Bind(wx.EVT_TIMER, self.EventTimer, self.timer) #!bind del timer
        self.Bind(wx.EVT_LISTBOX, self.EventList, self.List_Lvl) #!bind de lista
        self.Bind(wx.EVT_BUTTON, self.EventComenzarButton, self.StartButton) #!bind de boton comenzar
        self.Bind(wx.EVT_BUTTON, self.EventDeshacerButton, self.UndoButton) #!bind de boton deshacer
        self.Bind(wx.EVT_BUTTON, self.EventoBotonArrriba, self.botonArrriba) #!Bind de boton  para realizar todos los movimientos de arriba que sean de forma posible
        self.Bind(wx.EVT_BUTTON, self.Button00, self.Coche00)
        self.Bind(wx.EVT_BUTTON, self.Button01, self.Coche01)
        self.Bind(wx.EVT_BUTTON, self.Button02, self.Coche02)
        self.Bind(wx.EVT_BUTTON, self.Button03, self.Coche03)
        self.Bind(wx.EVT_BUTTON, self.Button04, self.Coche04)
        self.Bind(wx.EVT_BUTTON, self.Button05, self.Coche05)
        self.Bind(wx.EVT_BUTTON, self.Button10, self.Coche10)
        self.Bind(wx.EVT_BUTTON, self.Button11, self.Coche11)
        self.Bind(wx.EVT_BUTTON, self.Button12, self.Coche12)
        self.Bind(wx.EVT_BUTTON, self.Button13, self.Coche13)
        self.Bind(wx.EVT_BUTTON, self.Button14, self.Coche14)
        self.Bind(wx.EVT_BUTTON, self.Button15, self.Coche15)
        self.Bind(wx.EVT_BUTTON, self.Button20, self.Coche20)
        self.Bind(wx.EVT_BUTTON, self.Button21, self.Coche21)
        self.Bind(wx.EVT_BUTTON, self.Button22, self.Coche22)
        self.Bind(wx.EVT_BUTTON, self.Button23, self.Coche23)
        self.Bind(wx.EVT_BUTTON, self.Button24, self.Coche24)
        self.Bind(wx.EVT_BUTTON, self.Button25, self.Coche25)
        self.Bind(wx.EVT_BUTTON, self.Button30, self.Coche30)
        self.Bind(wx.EVT_BUTTON, self.Button31, self.Coche31)
        self.Bind(wx.EVT_BUTTON, self.Button32, self.Coche32)
        self.Bind(wx.EVT_BUTTON, self.Button33, self.Coche33)
        self.Bind(wx.EVT_BUTTON, self.Button34, self.Coche34)
        self.Bind(wx.EVT_BUTTON, self.Button35, self.Coche35)
        self.Bind(wx.EVT_BUTTON, self.Button40, self.Coche40)
        self.Bind(wx.EVT_BUTTON, self.Button41, self.Coche41)
        self.Bind(wx.EVT_BUTTON, self.Button42, self.Coche42)
        self.Bind(wx.EVT_BUTTON, self.Button43, self.Coche43)
        self.Bind(wx.EVT_BUTTON, self.Button44, self.Coche44)
        self.Bind(wx.EVT_BUTTON, self.Button45, self.Coche45)
        self.Bind(wx.EVT_BUTTON, self.Button50, self.Coche50)
        self.Bind(wx.EVT_BUTTON, self.Button51, self.Coche51)
        self.Bind(wx.EVT_BUTTON, self.Button52, self.Coche52)
        self.Bind(wx.EVT_BUTTON, self.Button53, self.Coche53)
        self.Bind(wx.EVT_BUTTON, self.Button54, self.Coche54)
        self.Bind(wx.EVT_BUTTON, self.Button55, self.Coche55)


        self.StartButton.Disable() #!el boton de Comenzar siempre esta desactivado a no ser que se seleccione un nivel previamente
        self.UndoButton.Disable() #? Mantener en oculto hasta que el boton se impelemente definitivamente
        self.botonArrriba.Disable() #
    #Todo: Alamcenamos los coches en una matriz para que sea de mejor acceso
        self.matrizTablero =[[self.Coche00,self.Coche01,self.Coche02,self.Coche03,self.Coche04,self.Coche05], #!Solucion más sencilla que se me ocurrio,
                            [self.Coche10,self.Coche11,self.Coche12,self.Coche13,self.Coche14,self.Coche15],  #!Basicamente es una forma de impelementar la forma del codigo anterior,
                            [self.Coche20,self.Coche21,self.Coche22,self.Coche23,self.Coche24,self.Coche25],  #!y tener mejor un mejor acceso y control a los elementos en las funciones.
                            [self.Coche30,self.Coche31,self.Coche32,self.Coche33,self.Coche34,self.Coche35],
                            [self.Coche40,self.Coche41,self.Coche42,self.Coche43,self.Coche44,self.Coche45],
                            [self.Coche50,self.Coche51,self.Coche52,self.Coche53,self.Coche54,self.Coche55]]

        ParKingDavidRuizVelazquez.VaciarTablero(self) #!LLamamos a la funcion vaciar tabalero, para poder limpiarlo antes de emepzar y que no salga la pantalla llena de botones
       
    #Todo: Lista con colores posibles para el background de los coches
        self.RGB = [[255,0,0],
                    [255,255,0],
                    [0,255,0],
                    [0,255,255],
                    [0,0,255],
                    [255,0,255],
                    [128,0,0],
                    [128,128,0],
                    [0,128,0],
                    [0,128,128],
                    [0,0,128],
                    [128,0,128],
                    [64,0,0],
                    [64,64,0],
                    [0,64,0],
                    [0,64,64],
                    [0,0,64],
                    [64,0,64],
                    [192,0,0],
                    [192,192,0]]



#Todo:Funcion para Vaciar el tablero al empezar un juego Desde 0 y  limpiar el color de los botones
    def VaciarTablero(self):
        for i in self.matrizTablero:
            for j in i:
                j.Hide() #!Oculta los botones
                j.Enable() #!reiniciamos su estado a encendido
                j.SetLabel("") #!reinicamos su label a null
                j.SetBackgroundColour(wx.Colour(255,255,255)) #!reiniciamos su color a blanco
        
#Todo: obtiene cada elemento de la matrizTablero y lo desabilita
    def DisableButton(self):
        for i in self.matrizTablero:
            for j in i:
                j.Disable()



        
 #Todo:Funcion que lee el archivo, remueve los "\n" , y guarda el contenido en uan lista para que sea mas facil acceder
    def LeerArchivo(self):
        f = open("niveles.txt","r")
        self.listaNiveles = f.read().splitlines()
        f.close()
#Todo:Obtiene self.listaRecord
    def ObtenciolistaRecord(self):
        f = open("records.txt","r")  
        self.listaRecord = f.read()
        f.close()

    

   

#Todo:Obtiene la cantidad de coches de ese nivel y la posicion de la lista donde comienza ese nivel
    def GetListaCoches(self):
        
        lvl = self.nivelSeleccionado #! Nivel seleccionado segun el eventList
        continuar = False
        veces = 0
        self.levelIndex = 1
        while continuar != True :             
            self.numeroCoches = int(self.listaNiveles[self.levelIndex])
            self.levelIndex += self.numeroCoches + 1
            veces += 1
            if veces == lvl : 
                continuar = True
                self.levelIndex -= (self.numeroCoches+1)
        self.levelIndex+=1  #!le sumo 1 ya que necesito la posicion del primer coche no la posicion donde empieza esta parte del fichero

        self.listaCoches = [] #!Lista para almacenar los tipos de coches
        self.listaCoches = self.listaNiveles[self.levelIndex:self.levelIndex+self.numeroCoches:1]

        self.listaMov = [] #!Lista para almacenar el mov previo
        self.indexList = [] #!Lista para la lista de indices del moviento
        self.contadorMov = 0 #!Contador para saber el num de mov

#Todo: Funcion que realiza las colisiones con los muros
    def WallColiders(col,fil,coche):
        
        if coche.GetLabel() == "<": #!colision Horizontal izquierda
            if col == 0:
                return True
        if coche.GetLabel() == ">": #!colision Horizontal derecha
            if col == 5 and fil != 2: #!Para que no se salga del tablero en la salida
                return True
        if coche.GetLabel() == "^": #!colision Vertical arriba
            if fil == 0:
                return True
        if coche.GetLabel() == "v": #!colision Vertical abajo
            if fil == 5:
                return True
#Todo: funcion que realiza las colisiones con los demas coches
    def CarColider(CocheSiguiente):
        if CocheSiguiente.IsShown():  #!determina si el boton previo esta mostrado o y develve True a la colision
            return True

#Todo: Funcion que se va a encargar de registrar el movmiento previo
        
#Todo: Funcion que remplaza el mov sig, por la posicion que se encontraba antes

#Todo: Escribe la lista que se le pase por parametro en el fichero "records.txt"
    def EscrituraRecord(lista):
        f = open("records.txt","w") 
        for i in lista:
            f.write(str(i))
        f.close()             
        
#Todo: obtiene en un array la sintaxis para escribir los records en List_Lvl
    def GetPointsLabel(self):
        nuevaLista = []
        for i in self.listaRecord:
            nuevaLista.append(i)  #!obtenemos la lista en otra local
        self.R2 = ["Nivel 1:"+nuevaLista[0] + nuevaLista[1],"Nivel 2:"+nuevaLista[3] + nuevaLista[4],"Nivel 3:"+nuevaLista[6] + nuevaLista[7],"Nivel 4:"+nuevaLista[9] + nuevaLista[10],"Nivel 5:"+nuevaLista[12] + nuevaLista[13],"Nivel 6:"+nuevaLista[15] + nuevaLista[16],"Nivel 7:"+nuevaLista[18] + nuevaLista[19],"Nivel 8:"+nuevaLista[21] + nuevaLista[22],"Nivel 9:"+nuevaLista[24] + nuevaLista[25],"Nivel 10:"+nuevaLista[27] + nuevaLista[28]]
 
        
           
    
#Todo: Escribe en Records.txt  usando la sintaxix -pt-
    def InfoRecord(self):
        nuevaLista = []
        posicion = 0
        for i in self.listaRecord:
            nuevaLista.append(i)  #!obtenemos la lista en otra local
        if self.nivelSeleccionado != int(self.listaNiveles[0]):
            posicion = ((self.nivelSeleccionado*2)+(self.nivelSeleccionado-1))-2 #!formula para saber la posicon de las decenas de la lista de records
            if self.cantidadNiveles <= int(self.listaNiveles[0])-1: #!no se pasa de los niveles que hay marcados
                if int(self.tiempoRestante) > int(nuevaLista[posicion])*10+int(nuevaLista[posicion+1]):
                    if self.tiempoRestante <=9:
                        nuevaLista[posicion] = "0"
                        nuevaLista[posicion+1] = str(self.tiempoRestante)
                        nuevaLista[posicion+2] = "-"
                    else:
                        unidades = int(self.tiempoRestante%10)
                        decenas = int((self.tiempoRestante/10))
                        nuevaLista[posicion] = str(decenas)
                        nuevaLista[posicion+1] = str(unidades)
                        nuevaLista[posicion+2] = "-"
                
        else:
            posicion = ((self.nivelSeleccionado*2)+(self.nivelSeleccionado-1))-2 #!formula para saber la posicon de las decenas de la lista de records
            if int(self.tiempoRestante) > int(nuevaLista[posicion])*10+int(nuevaLista[posicion+1]):

                if self.tiempoRestante <=9:
                    nuevaLista[posicion] = "0"
                    nuevaLista[posicion+1] = str(self.tiempoRestante)
                    
                else:
                    unidades = int(self.tiempoRestante%10)
                    decenas = int((self.tiempoRestante/10))
                    nuevaLista[posicion] = str(decenas)
                    nuevaLista[posicion+1] = str(unidades)
        
            ParKingDavidRuizVelazquez.EscrituraRecord(nuevaLista) 

#Todo Actualiza la lista de records si se gana con algunas condiciones
    def listBoxClearWin(self):
        if self.cantidadNiveles ==  0 and int(self.listaNiveles[0]) >=0:
            self.List_Lvl.SetItems([self.R2[0]])
        elif self.cantidadNiveles == 1  and int(self.listaNiveles[0]) >=1:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1]])
        elif self.cantidadNiveles == 2 and int(self.listaNiveles[0]) >=2:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2]])
        elif self.cantidadNiveles == 3 and int(self.listaNiveles[0]) >=3:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3]])
        elif self.cantidadNiveles == 4 and int(self.listaNiveles[0]) >=4:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4]])
        elif self.cantidadNiveles == 5 and int(self.listaNiveles[0]) >=5:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5]])
        elif self.cantidadNiveles == 6 and int(self.listaNiveles[0]) >=6:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6]])
        elif self.cantidadNiveles == 7 and int(self.listaNiveles[0]) >=7:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7]])
        elif self.cantidadNiveles == 8 and int(self.listaNiveles[0]) >=8:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7],self.R2[8]])
        elif self.cantidadNiveles == 9 and int(self.listaNiveles[0]) >=9:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7],self.R2[8],self.R2[9]])
        elif self.cantidadNiveles == 10 and int(self.listaNiveles[0]) >=10:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7],self.R2[8],self.R2[9],self.R2[10]])
                  
#Todo Añade en Choices dependiendo de la cantidad de niveles jugables, junto con su puntuaccion
    def listBoxClear(self):
        if self.cantidadNiveles ==  0 :
            self.List_Lvl.SetItems([self.R2[0]])
        elif self.cantidadNiveles == 1  :
            self.List_Lvl.SetItems([self.R2[0],self.R2[1]])
        elif self.cantidadNiveles == 2:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2]])
        elif self.cantidadNiveles == 3:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3]])
        elif self.cantidadNiveles == 4:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4]])
        elif self.cantidadNiveles == 5:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5]])
        elif self.cantidadNiveles == 6:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6]])
        elif self.cantidadNiveles == 7:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7]])
        elif self.cantidadNiveles == 8:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7],self.R2[8]])
        elif self.cantidadNiveles == 9:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7],self.R2[8],self.R2[9]])
        elif self.cantidadNiveles == 10:
            self.List_Lvl.SetItems([self.R2[0],self.R2[1],self.R2[2],self.R2[3],self.R2[4],self.R2[5],self.R2[6],self.R2[7],self.R2[8],self.R2[9],self.R2[10]])
                  

   
#Todo: funcion que realiza los movientos horizontales segun su label     
    def MovimientosHorizontales(col,fil,coche,self):
        Ncol = col+1
        Nfil = fil+1
        NLista = []
        for i in self.listaCoches:
            index = 0

            if coche.GetLabel() == "<":
                if i[0] == "H": 
                    if int(i[1]) == Ncol and int(i[2]) == Nfil:  #! se coge el numero del boton y se intercambian los valores y se les suma 1 a cada uno 
                        if col-1 == -1: #!evitamso el error IndexError
                            return
                        cocheSiguiente = self.matrizTablero[fil][col-1] #!obtiene el coche anterior para comprobar la colision
                        if ParKingDavidRuizVelazquez.CarColider(cocheSiguiente) == True:
                            return
                        if ParKingDavidRuizVelazquez.WallColiders(col,fil,coche) == True: #!llamada de funcion colision con muros,
                            return

                        index = self.listaCoches.index(i)
                        nuevoMov = "H"+str(Ncol-1)+str(Nfil)+str(i[3])

                        ParKingDavidRuizVelazquez.RegistroMovmientos(i,index,self) #! funcion registro
                        

                        self.listaCoches[index] = nuevoMov
                        ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                        ParKingDavidRuizVelazquez.GenElements(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                        return

    
        for i in reversed(self.listaCoches):
            index = 0
            if coche.GetLabel() == ">":
                if i[0] == "H":
                    if int(i[2]) == Nfil:
                        NLista.append(i)
                        for j in NLista:
                            r = Ncol-(int(j[3])-1)
                            nuevoMov = "H"+str(r)+str(Nfil)+str(j[3])
                            if nuevoMov in self.listaCoches:
                                if col+1 == 6 : #! evitamos el error IndexError
                                    return
                                cocheSiguiente = self.matrizTablero[fil][col+1] #!obtiene el coche sig para comprobar la colision 
                                if ParKingDavidRuizVelazquez.CarColider(cocheSiguiente) == True:
                                    return 
                                if ParKingDavidRuizVelazquez.WallColiders(col,fil,coche) == True: #!llamada de funcion colision con muros
                                    return
                                
                                index = self.listaCoches.index(nuevoMov)
                                nuevoMov = "H"+str(r+1)+str(Nfil)+str(j[3])

                                ParKingDavidRuizVelazquez.RegistroMovmientos(i,index,self) #!funcion registro
                                

                                self.listaCoches[index] = nuevoMov
                                ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                                ParKingDavidRuizVelazquez.GenElements(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                                return


#Todo: funcion que realiza los movientos horizontales segun su label
    def MovimientoVerticales(col,fil,coche,self):
        Ncol = col+1
        Nfil = fil+1
        NLista = []

        for i in self.listaCoches:
            index = 0
            if coche.GetLabel() == "^":
                if i[0] == "V": 
                    if int(i[1]) == Ncol and int(i[2]) == Nfil:  #! se coge el numero del boton y se intercambian los valores y se les suma 1 a cada uno
                        if fil-1 == -1: #!evitamso el error IndexError
                            return
                        cocheSiguiente = self.matrizTablero[fil-1][col] #!obtiene el coche anterior para comprobar la colision
                        if ParKingDavidRuizVelazquez.CarColider(cocheSiguiente) == True:
                            return 
                        if ParKingDavidRuizVelazquez.WallColiders(col,fil,coche) == True: #!llamada de funcion colision con muros,
                            return 
                        index = self.listaCoches.index(i)
                        nuevoMov = "V"+str(Ncol)+str(Nfil-1)+str(i[3])

                        ParKingDavidRuizVelazquez.RegistroMovmientos(i,index,self) #!funcion registro

                        self.listaCoches[index] = nuevoMov
                        ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                        ParKingDavidRuizVelazquez.GenElements(self) #!Llamamos a la funcion GenElements
                        return

        for i in reversed(self.listaCoches):
            index = 0
            if coche.GetLabel() == "v":
                if Ncol == int(i[1]):
                    NLista.append(i)
                    for j in NLista:
                        r = Nfil -(int(j[3])-1)
                        nuevoMov = "V"+str(Ncol)+str(r)+str(j[3])
                        if nuevoMov in self.listaCoches:
                            if fil+1 == 6: #!evitanos el IndexError
                                return
                            cocheSiguiente = self.matrizTablero[fil+1][col] #!obtiene el coche anterior para comprobar la colision
                       
                            if ParKingDavidRuizVelazquez.CarColider(cocheSiguiente) == True:
                                return 

                            if ParKingDavidRuizVelazquez.WallColiders(col,fil,coche) == True: #!llamada de funcion colision con muros,
                                return
                            index = self.listaCoches.index(nuevoMov)
                            nuevoMov = "V"+str(Ncol)+str(r+1)+str(j[3])

                            ParKingDavidRuizVelazquez.RegistroMovmientos(i,index,self) #!funcion registro

                            self.listaCoches[index] = nuevoMov
                            ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                            ParKingDavidRuizVelazquez.GenElements(self) #!Llamamos a la funcion GenElements
                            return          
    
    def RegistroMovmientos(coche,index,self):
        self.contadorMov +=1 #! incremento de contador de movmientos
        self.listaMov.append(coche)
        self.indexList.append(index)
                          
    def DeshacerMovmientos(self):
        if self.contadorMov == 0: 
            return False
        self.contadorMov -=1
        self.listaCoches[self.indexList[-1]] = self.listaMov[-1] #!Reemplazar el anterior mov por el de la lista de registros
        self.listaMov.pop() #!eliminar el ultimo 
        self.indexList.pop() #!eliminar el ultimo
        ParKingDavidRuizVelazquez.VaciarTablero(self) 
        ParKingDavidRuizVelazquez.GenElements(self) 

        return True
    def MoverArriba(self):
        lista = []
        for i in self.listaCoches:
            lista.append(i)
        
        
        for i in lista:
            if i[0] == 'V':
                indice = lista.index(i)
                if int(i[2])-1  != 0:
                     if self.matrizTablero[int(i[2])-2][int(i[1])-1].IsShown() == False:
                        
                        nuevoC = "V"+str(i[1])+str(int(i[2])-1)+str(i[3])
                        self.listaCoches[indice] = nuevoC
                        coche = i     
                        ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
                        ParKingDavidRuizVelazquez.GenElements(self) 
              
                        ParKingDavidRuizVelazquez.RegistroMovmientos(coche,indice,self)
                        
                



        return
    

    def EventoBotonArrriba(self,event): 

        ParKingDavidRuizVelazquez.MoverArriba(self)
        event.Skip()


#Todo:Posicionar los coches en el tablero.
    def GenElements(self):
        #Todo: Movimientos si es horizontal
        RGB = 0
        for i in self.listaCoches:
            
            if i[0] == 'H':
                colInicialH = int(i[1])-1 #! hay que restarle 1 debido a que el tablero empieza en 0 y en la lista en 1
                filInicialH = int(i[2])-1 #! hay que restarle 1 debido a que el tablero empieza en 0 y en la lista en 1
                tamanoH = int(i[3])-1  #! hay que restarle 1 ya que ya esta colocada la primera posicion
                finalH = tamanoH + colInicialH
                
                
                self.matrizTablero[filInicialH][colInicialH].Show() #!punto incial
                self.matrizTablero[filInicialH][colInicialH].SetLabel("<") #!inserta el label
                self.matrizTablero[filInicialH][colInicialH].SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, "")) #!cambia la fuente del label
                self.matrizTablero[filInicialH][colInicialH].SetBackgroundColour(wx.Colour(int(self.RGB[RGB][0]),int(self.RGB[RGB][1]),int(self.RGB[RGB][2]))) #!cambia el color del label
                
                for j in range(finalH-colInicialH-1):
                    self.matrizTablero[filInicialH][colInicialH+j+1].Show() #!puntos medios
                    self.matrizTablero[filInicialH][colInicialH+j+1].Disable() #! huecos entre medias (color plano sin texto y desabilitado)
                    self.matrizTablero[filInicialH][colInicialH+j+1].SetBackgroundColour(wx.Colour(int(self.RGB[RGB][0]),int(self.RGB[RGB][1]),int(self.RGB[RGB][2])))  
                
                

                self.matrizTablero[filInicialH][finalH].Show() #!punto final
                self.matrizTablero[filInicialH][finalH].SetLabel(">") #!inserta el label
                self.matrizTablero[filInicialH][finalH].SetBackgroundColour(wx.Colour(int(self.RGB[RGB][0]),int(self.RGB[RGB][1]),int(self.RGB[RGB][2]))) #!cambia el color del label
                self.matrizTablero[filInicialH][finalH].SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, "")) #!cambia la fuente del label
                
                

                
                RGB += 1 #!avanzamos un color

                #Todo: Movimientos si es Vertical
            if i[0] == 'V':
                colInicialV = int(i[1])-1 #! hay que restarle 1 debido a que el tablero empieza en 0 y en la lista en 1
                filInicialV = int(i[2])-1 #! hay que restarle 1 debido a que el tablero empieza en 0 y en la lista en 1
                tamanoV = int(i[3])-1  #! hay que restarle 1 ya que ya esta colocada la primera posicion
                finalV = tamanoV + colInicialV
                
                self.matrizTablero[filInicialV][colInicialV].Show() #!punto incial
                self.matrizTablero[filInicialV][colInicialV].SetLabel("^") #!inserta el label
                self.matrizTablero[filInicialV][colInicialV].SetFont(wx.Font(35, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, "")) #!cambia la fuente del label
                self.matrizTablero[filInicialV][colInicialV].SetBackgroundColour(wx.Colour(int(self.RGB[RGB][0]),int(self.RGB[RGB][1]),int(self.RGB[RGB][2])))
                
                for k in range(finalV-colInicialV-1): #! huecos entre medias (color plano sin texto y desabilitado)
                    self.matrizTablero[filInicialV+k+1][colInicialV].Show()
                    self.matrizTablero[filInicialV+k+1][colInicialV].Disable()
                    self.matrizTablero[filInicialV+k+1][colInicialV].SetBackgroundColour(wx.Colour(int(self.RGB[RGB][0]),int(self.RGB[RGB][1]),int(self.RGB[RGB][2])))
                    

                self.matrizTablero[filInicialV+tamanoV][colInicialV].Show() #!punto final
                self.matrizTablero[filInicialV+tamanoV][colInicialV].SetLabel("v") #!inserta el label
                self.matrizTablero[filInicialV+tamanoV][colInicialV].SetFont(wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, "")) #!cambia la fuente del label
                self.matrizTablero[filInicialV+tamanoV][colInicialV].SetBackgroundColour(wx.Colour(int(self.RGB[RGB][0]),int(self.RGB[RGB][1]),int(self.RGB[RGB][2])))

                

                RGB += 1 #! avanzamos un color

#Todo: Funcion encargada de resetart las variables principales una vez terminado el juego.
    def GameOver(self):
        self.nivelSeleccionado = 0
        self.levelIndex = 0
        self.numeroCoches = 0 #!Vaciamos el numero de coches y el index del nivel anteriormente seleccionado
        self.TimerOutPut.SetLabel("90")
        self.infoTxt.SetLabel("Game Over,Seleccione un nivel")
        ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero
        self.listaCoches = [] #!Vaciamos la lista de los coches
   
    def WinGame(self):
        if self.nivelSeleccionado-1 == self.cantidadNiveles and self.nivelSeleccionado != int(self.listaNiveles[0]):
            self.cantidadNiveles +=1 
            
        

        ParKingDavidRuizVelazquez.InfoRecord(self)  #!obtenemos info de los records
        ParKingDavidRuizVelazquez.GetPointsLabel(self)  #!actualizamos la lista record
        ParKingDavidRuizVelazquez.ObtenciolistaRecord(self) #!leemos y obtenemos de nuevo la lista de los record
        ParKingDavidRuizVelazquez.GetPointsLabel(self) #!volvemos a obtener R2
        ParKingDavidRuizVelazquez.listBoxClearWin(self)  #!actualizamos los choices de la lista


        self.TimerOutPut.SetLabel("90")
        self.timer.Stop()
        self.infoTxt.SetLabel("Victoria,Seleccione un nivel")
        ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero
        self.Coche22.Show(),self.Coche23.Show(),self.Coche24.Show()
        self.Coche22.Disable(),self.Coche23.Disable(),self.Coche24.Disable()
        self.Coche22.SetLabel("W"),self.Coche23.SetLabel("I"),self.Coche24.SetLabel("N")
        

#Todo: Evento de cuenta atras y sistema de perder por tiempo
    def EventTimer(self, event):
        self.tiempoRestante -= 1 #!Disminumos el contador de tiempo (instanciado en 90)
        self.TimerOutPut.SetLabel(str(self.tiempoRestante)) #!Actalizamos el label de TimerOutput
        if self.tiempoRestante == 10: self.infoTxt.SetLabel("Se esta acabando el tiempo!")
        if self.tiempoRestante == 0: #!si el tiempo restante es 0:
            self.timer.Stop() #!Paramos la cuenta atras una vez esta ha llegado a 0
            self.TimerOutPut.SetLabel("0") #!Mantener en 0 el contador por seguridad
            ParKingDavidRuizVelazquez.GameOver(self) #!Llamamos a la funcion GameOver para poder Resetar las variables.
            


#Todo: Evento de la lista de niveles
    def EventList(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        self.timer.Stop() #! Paramos el temporizador mientras se esta cambiando de nivel o se ha parado la partida
        self.UndoButton.Enable() #!
       
        
        self.TimerOutPut.SetLabel("90") #!Devolvemos el txt del temporizador a 90
        self.infoTxt.SetLabel(u"Seleccione Comenzar cuando este listo")
        ParKingDavidRuizVelazquez.LeerArchivo(self) #!Llamamos a la funcion LeerArchivo
        self.nivelSeleccionado = int(self.List_Lvl.GetSelection()+1) #!Selecicona el nivel
        ParKingDavidRuizVelazquez.ObtenciolistaRecord(self)
        self.StartButton.Enable() #!Habilita el boton de comenzar una vez ya esta seleccionado el nivel
        ParKingDavidRuizVelazquez.VaciarTablero(self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
        ParKingDavidRuizVelazquez.GetListaCoches(self) #!Llamamos a la funcion GetListaCoches para obtener la lista de coches del nivel elejido
        ParKingDavidRuizVelazquez.GenElements(self) #!Llamamos a la funcion GenElements para generar los coches 
        ParKingDavidRuizVelazquez.DisableButton(self)
                 
                        
        event.Skip()


    def EventComenzarButton(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        self.infoTxt.SetLabel(u"Juego en curso, si deseas acabar elija otro nivel")
        self.StartButton.Disable() #!Desactiva el boton de comenzar una vez ya se ha empezado el juego, y no se muestra hasta que se cambie de modo.
        self.tiempoRestante = 90 #! devolvemos el tiempo restante a 90 cada vez que comienza una nueva partida
        self.timer.Start(1000) #!Intervalos de 1 segundo en el reloj, debido a que esta en miliseegundos
        ParKingDavidRuizVelazquez.VaciarTablero(self) #!vaciamos y ponemos en .Enable()
        ParKingDavidRuizVelazquez.GenElements(self) #!Llamamos a la funcion GenElements para generar los coches 
        self.botonArrriba.Enable() #
        


        event.Skip()

    def EventDeshacerButton(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        ParKingDavidRuizVelazquez.DeshacerMovmientos(self)
        event.Skip()
 




    def Button00(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        
        col = 0
        fil = 0
        coche = self.Coche00
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        
        event.Skip()

    def Button01(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 1
        fil = 0
        coche = self.Coche01
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button02(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 2
        fil = 0
        coche = self.Coche02


        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
            


        event.Skip()


    def Button03(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 3
        fil = 0
        coche = self.Coche03
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()



    def Button04(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 4
        fil = 0
        coche = self.Coche04
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        


        event.Skip()


    def Button05(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 5
        fil = 0
        coche = self.Coche05
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button10(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 0
        fil = 1
        coche = self.Coche10
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()

    def Button11(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 1
        fil = 1
        coche = self.Coche11
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button12(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 2
        fil = 1
        coche = self.Coche12
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button13(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 3
        fil = 1
        coche = self.Coche13
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button14(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 4
        fil = 1
        coche = self.Coche14
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)

        event.Skip()

    def Button15(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 5
        fil = 1
        coche = self.Coche15
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self) 
        event.Skip()

    def Button20(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 0
        fil = 2
        coche = self.Coche20
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button21(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 1
        fil = 2
        coche = self.Coche21
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
        event.Skip()

    def Button22(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 2
        fil = 2
        coche = self.Coche22
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
        event.Skip()

    def Button23(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 3
        fil = 2
        coche = self.Coche23
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button24(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 4
        fil = 2
        coche = self.Coche24
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button25(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 5
        fil = 2
        coche = self.Coche25
        if self.listaCoches[0] == "H532":
            
            ParKingDavidRuizVelazquez.WinGame(self)
        else:
            ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
            ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)

        event.Skip()

    def Button30(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 0
        fil = 3
        coche = self.Coche30
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)

        event.Skip()
    def Button31(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 1
        fil = 3
        coche = self.Coche31
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)

        event.Skip()

    def Button32(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 2
        fil = 3
        coche = self.Coche32
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button33(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 3
        fil = 3
        coche = self.Coche33
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()

    def Button34(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 4
        fil = 3
        coche = self.Coche34
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button35(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 5
        fil = 3
        coche = self.Coche35
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button40(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 0
        fil = 4
        coche = self.Coche40
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)

        event.Skip()

    def Button41(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>

        col = 1
        fil = 4
        coche = self.Coche41
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()

    def Button42(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 2
        fil = 4
        coche = self.Coche42
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()

    def Button43(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 3
        fil = 4
        coche = self.Coche43
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()

    def Button44(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 4
        fil = 4
        coche = self.Coche44
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button45(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 5
        fil = 4
        coche = self.Coche45
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self) #!Llamamos a la funcion VaciarTablero para limpiar al elegir otro nivel
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)

        event.Skip()

    def Button50(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 0
        fil = 5
        coche = self.Coche50
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)

        event.Skip()

    def Button51(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 1
        fil = 5
        coche = self.Coche51
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button52(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 2
        fil = 5
        coche = self.Coche52
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        
        event.Skip()

    def Button53(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 3
        fil = 5
        coche = self.Coche53
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button54(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 4
        fil = 5
        coche = self.Coche54
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        event.Skip()

    def Button55(self, event):  # wxGlade: ParKingDavidRuizVelazquez.<event_handler>
        col = 5
        fil = 5
        coche = self.Coche55
        ParKingDavidRuizVelazquez.MovimientosHorizontales(col,fil,coche,self)
        ParKingDavidRuizVelazquez.MovimientoVerticales(col,fil,coche,self)
        event.Skip()

# end of class ParKingDavidRuizVelazquez

class Main(wx.App):
    def OnInit(self):
        self.ParkingDavidRuizVelazquez = ParKingDavidRuizVelazquez(None, wx.ID_ANY, "")
        self.SetTopWindow(self.ParkingDavidRuizVelazquez)
        self.ParkingDavidRuizVelazquez.Show()
        return True

# end of class Main

if __name__ == "__main__":
    app = Main(0)
    app.MainLoop()
    

