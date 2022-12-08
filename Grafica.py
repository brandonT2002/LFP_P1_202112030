from AFD import AFD
import os
import webbrowser

class Grafica:
    def generarDot(self,automata : AFD):
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

        with open('Reports/reporte.txt','w',encoding='utf-8') as reporte:
            reporte.write(dot)

        os.system('dot -Tpdf Reports/reporte.txt -o Reporte.pdf')
        webbrowser.open('Reporte.pdf')