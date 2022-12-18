from AFD import AFD
from GR import GR
import os
import webbrowser

class Grafica:
    def generarDotAFD(self,automata : AFD,cadenaMinima):
        dot = 'digraph G {\ngraph [labelloc=t];\nnode [shape=circle];\nfontsize=30;\nlabel = "' + automata.nombreAFD + '";NodeLabel [shape=none fontsize=18 label = \n<'

        dot += f'\nEstados: {", ".join(automata.estados)}<br align="left"/>'
        dot += f'\nAlfabeto: {", ".join(automata.alfabeto)}<br align="left"/>'
        dot += f'\nEstados de Aceptación: {", ".join(automata.eAceptacion)}<br align="left"/>'
        dot += f'\nEstados Inicial: {automata.eInicial}<br align="left"/>'
        dot += '\nProducciones:<br align="left"/>'
        elementos = ''
        for produccion in automata.transiciones:
            elementos += f'\n{produccion.origen}, {produccion.entrada}; {produccion.destino}<br align="left"/>'
        elementos += f'\nCadena mínima: {cadenaMinima}<br align="left"/>'
        dot += f'{elementos}\n>\n];'
        dot += '\nrankdir=LR;\n'  

        elementos = ''
        for estado in automata.estados:
            elementos += f'{estado};'
        dot += elementos
        #S1 [peripheries=2];
        elementos = ''
        for aceptado in automata.eAceptacion:
            elementos += f'\n{aceptado} [peripheries=2];'
        dot += elementos

        dot += '\nFlecha[shape=rarrow label=""];'
        dot += f'\nNodeLabel -> Flecha -> {automata.eInicial} [color=none];'

        elementos = ''
        for produccion in automata.transiciones:
            elementos += f'\n{produccion.origen} -> {produccion.destino} [label="{produccion.entrada}"];'
        dot += elementos
        dot += '\n}'

        with open('Reports/reporteAFD.txt','w',encoding='utf-8') as reporte:
            reporte.write(dot)

        os.system('dot -Tpdf Reports/reporteAFD.txt -o ReporteAFD.pdf')
        webbrowser.open('ReporteAFD.pdf')

    def generarRuta(self,nombre,ruta,inicial):
        dot = 'digraph G {\n\tgraph [labelloc=t fontsize=20];\n\trankdir = LR;\n\tlabel = "' + nombre + '";\n\tinicial [label = ' + inicial + '];\n'

        if len(ruta) > 0:
            for i in range(len(ruta)):
                dot += f'\tn{i} [label = "{ruta[i][1]}"];\n'

            dot += f'\tinicial -> n{0} [label = "{ruta[0][0]}"];\n'

            for i in range(len(ruta) - 1):
                dot += f'\tn{i} -> n{i + 1} [label = "{ruta[i + 1][0]}"];\n'

        dot += '}'
        
        with open('Reports/rutaAFD.txt','w',encoding='utf-8') as reporte:
            reporte.write(dot)

        os.system('dot -Tpdf Reports/rutaAFD.txt -o rutaAFD.pdf')
        webbrowser.open('rutaAFD.pdf')

    def generarDotGR(self,gramatica : GR,cadenaMinima):
        dot = 'digraph G {\ngraph [labelloc=t];\nnode [shape=circle];\nfontsize=30;\nlabel = "' + gramatica.nombreGR + '";NodeLabel [shape=none fontsize=18 label = \n<'

        dot += f'\nNo terminales: {", ".join(gramatica.noTerminales)}<br align="left"/>'
        dot += f'\nTerminales: {", ".join(gramatica.terminales)}<br align="left"/>'
        dot += f'\nNo terminal inicial: {gramatica.noTerminalInicial}<br align="left"/>'
        dot += f'\nProducciones:<br align="left"/>'
        elementos = ''
        for produccion in gramatica.producciones:
            if produccion.entrada != '$':
                elementos += f'\n{produccion.origen} &#62; {produccion.entrada} {produccion.destino}<br align="left"/>'
            else:
                elementos += f'\n{produccion.origen} &#62; {produccion.entrada}<br align="left"/>'
        elementos += f'\nCadena mínima: {cadenaMinima}<br align="left"/>'
        dot += f'{elementos}\n>\n];'
        dot += '\nrankdir=LR;\n' 

        elementos = ''
        for noTerm in gramatica.noTerminales:
            elementos += f'{noTerm};'
        dot += elementos
        #S1 [peripheries=2];
        elementos = ''
        for aceptado in gramatica.producciones:
            if aceptado.entrada == '$' and aceptado.destino == 'ACEPTADO':
                elementos += f'\n{aceptado.origen}[peripheries=2];'
        dot += elementos

        dot += '\nFlecha[shape=rarrow label=""];'
        dot += f'\nNodeLabel -> Flecha -> {gramatica.noTerminalInicial} [color=none];'

        elementos = ''
        for produccion in gramatica.producciones:
            if produccion.entrada != '$':
                elementos += f'\n{produccion.origen} -> {produccion.destino} [label="{produccion.entrada}"];'
        dot += elementos
        dot += '\n}'

        with open('Reports/reporteGR.txt','w',encoding='utf-8') as reporte:
            reporte.write(dot)

        os.system('dot -Tpdf Reports/reporteGR.txt -o ReporteGR.pdf')
        webbrowser.open('ReporteGR.pdf')

    #def generarRutaGR(self,nombre,ruta,)