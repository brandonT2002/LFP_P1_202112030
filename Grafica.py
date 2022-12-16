from AFD import AFD
from GR import GR
import os
import webbrowser

class Grafica:
    def generarDotAFD(self,automata : AFD,cadenaMinima):
        dot = 'digraph G {\ngraph [labelloc=t];\nnode [shape=circle];\nfontsize=30;\nlabel = "' + automata.nombreAFD + '";NodeLabel [shape=none fontsize=18 label = \n<'

        elementos = ''
        for estado in automata.estados:
            elementos += f' {estado}'
        dot += f'\nEstados:{elementos}<br align="left"/>'
        elementos = ''
        for alfabeto in automata.alfabeto:
            elementos += f' {alfabeto}'
        dot += f'\nAlfabeto:{elementos}<br align="left"/>'
        elementos = ''
        for aceptado in automata.eAceptacion:
            elementos += f' {aceptado}'
        dot += f'\nEstados de Aceptación:{elementos}<br align="left"/>'
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

    def generarDotGR(self,gramatica : GR):
        dot = 'digraph G {\ngraph [labelloc=t];\nnode [shape=circle];\nfontsize=30;\nlabel = "' + gramatica.nombreGR + '";NodeLabel [shape=none fontsize=18 label = \n<'

        elementos = ''
        for noTerminal in gramatica.noTerminales:
            elementos += f' {noTerminal}'
        dot += f'\nNo terminales:{elementos}<br align="left"/>'
        elementos = ''
        for terminal in gramatica.terminales:
            elementos += f' {terminal}'
        dot += f'\nTerminales:{elementos}<br align="left"/>'
        elementos = ''
        for noTermIni in gramatica.noTerminalInicial:
            elementos += f' {noTermIni}'
        dot += f'\nNo terminal inicial:{elementos}<br align="left"/>'
        dot += f'\nProducciones:<br align="left"/>'
        elementos = ''
        for produccion in gramatica.producciones:
            if produccion.entrada != '$':
                elementos += f'\n{produccion.origen} &#62; {produccion.entrada} {produccion.destino}<br align="left"/>'
            else:
                elementos += f'\n{produccion.origen} &#62; {produccion.entrada}<br align="left"/>'
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