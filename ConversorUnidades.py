
# Importing the modules
import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk



#Trabalho para SEL0456 Sistemas Embarcados em Sistemas Operacionais


#Parte Estetica


# Janela
window  = tk.Tk()
window.geometry('500x450')
window.title('Conversor de Unidades')
window.configure(bg = '#415557')

# Configuracao das fontes
fontTitulo = font.Font(family = 'Monospace',size = '12')
font1 = font.Font(family = 'helvetica',size = '8')
font2 = font.Font(family = 'helvetica',size = '8')
font3 = font.Font(family = 'helvetica',size = '8')

# Variaveis do texto
number_from = StringVar()

# funcoes tkinter


def fromfunc(event):
    global result_from
    result_from = event.widget.get()

def tofunc(event):
    global result_to
    result_to = event.widget.get()

#########################################
# Gerar resposta
def resposta(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Atenção!','Colocar valores, selecionar as unidades e utilizar o (.) como separador decimal na entrada!')

    # Comprimento
    if result_from == 'Quilometros' and result_to == 'Milhas':
        calculate = number1*0.621371
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Quilometros' and result_to == 'Pes':
        calculate = number1*3280.84
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Quilometros' and result_to == 'Quilometros':
        calculate = number1*1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Milhas' and result_to == 'Quilometros':
        calculate = number1*1.60934
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Milhas' and result_to == 'Pes':
        calculate = number1*5280
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Milhas' and result_to == 'Milhas':
        calculate = number1*1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Pes' and result_to == 'Quilometros':
        calculate = number1*0.0003048
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Pes' and result_to == 'Milhas':
        calculate = number1*0.000189394
        result.cget('text')
        result.configure(text = (calculate,result_to))
    if result_from == 'Pes' and result_to == 'Pes':
        calculate = number1*1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    # Massa 

    elif result_from == 'Quilograma' and result_to == 'Toneladas':
        calculate = number1*0.001
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Quilograma' and result_to == 'Arroba':
        calculate = number1*0.0666
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Quilograma' and result_to == 'Quilograma':
        calculate = number1*1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Toneladas' and result_to == 'Quilograma':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Toneladas' and result_to == 'Arroba':
        calculate = number1*66.666
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Toneladas' and result_to == 'Toneladas':
        calculate = number1*1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Arroba' and result_to == 'Quilograma':
        calculate = number1*15
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Arroba' and result_to == 'Toneladas':
        calculate = number1*0.015
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Arroba' and result_to == 'Arroba':
        calculate = number1*1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    # Volume 
    if result_from == 'metros cubicos' and result_to == 'metros cubicos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'metros cubicos' and result_to == 'pes cubicos':
        calculate = number1*35.3147
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'metros cubicos' and result_to == 'litros':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'metros' and result_to == 'galoes':
        calculate = number1*264.172
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'metros cubicos' and result_to == 'centimetros cubicos':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'pes cubicos' and result_to == 'metros cubicos':
        calculate = number1*0.02831
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'pes cubicos' and result_to == 'pes cubicos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'pes cubicos' and result_to == 'litros':
        calculate = number1*28.31679
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'pes cubicos' and result_to == 'galoes':
        calculate = number1*7.4805
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'pes cubicos' and result_to == 'centimetros cubicos':
        calculate = number1*28316.8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'litros' and result_to == 'metros cubicos':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'litros' and result_to == 'pes cubicos':
        calculate = number1*0.0353146
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'litros' and result_to == 'litros':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'litros' and result_to == 'galoes':
        calculate = number1*0.26417
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'litros' and result_to == 'centimetros cubicos':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'galoes' and result_to == 'metros cubicos':
        calculate = number1*0.003785
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'galoes' and result_to == 'pes cubicos':
        calculate = number1*0.13368
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'galoes' and result_to == 'litros':
        calculate = number1*3.7854
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'galoes' and result_to == 'galoes':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'galoes' and result_to == 'centimetros cubicos':
        calculate = number1*3786.41
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'centimetros cubicos' and result_to == 'metros cubicos':
        calculate = number1*9.99999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'centimetros cubicos' and result_to == 'pes cubicos':
        calculate = number1*3.53146
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'centimetros cubicos' and result_to == 'litros':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'centimetros cubicos' and result_to == 'metros cubicos':
        calculate = number1*9.9999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'centimetros cubicos' and result_to == 'litros':
        calculate = number1*0.00099999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'centimetros cubicos' and result_to == 'galoes':
        calculate = number1*0.00026417
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'centimetros cubicos' and result_to == 'centimetros cubicos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
   
# funcao seletora
def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        fromdd['values'] = ('metros cubicos',
                            'pes cubicos',
                            'litros',
                            'galoes',
                            'centimetros cubicos')

        todd['values'] = ('metros cubicos',
                          'pes cubicos',
                          'litros',
                          'galoes',
                          'centimetros cubicos')

    elif unit == 'Comprimento':
        fromdd['values'] = ('Quilometros',
                            'Milhas',
                            'Pes')

        todd['values'] = ('Quilometros',
                          'Milhas',
                          'Pes')

    elif unit == 'Massa':
        fromdd['values'] = ('Quilograma',
                            'Toneladas',
                            'Arroba')

        todd['values'] = ('Quilograma',
                          'Toneladas',
                          'Arroba')
    


# Nome do aplicativo
main = tk.Label(window,text = 'Conversor de Unidades',bg = '#415557')
main['font'] = fontTitulo
main.place(relx = '0.48',rely = '0.1',anchor = 'center')

# Primeiro seletor
n = StringVar()
unitdd = ttk.Combobox(window,width = '25',textvariable = n)

# Grandezas
unitdd['values'] = ('Massa',
                    'Volume',
                    'Comprimento')

unitdd.place(relx = '0.57',rely = '0.3',anchor = 'center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

# Seletor de
f = StringVar()
fromdd = ttk.Combobox(window,width = '25',textvariable = f)

fromdd.place(relx = '0.57',rely = '0.38',anchor = 'center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

# caixa de texto
num_from = tk.Entry(window, width = 25, textvariable = number_from)
num_from.place(relx = '0.29',rely = '0.58')

resposta = partial(resposta,num_from)

# Seletor para
t = StringVar()
todd = ttk.Combobox(window,width = 25,textvariable = t)

todd.place(relx = '0.57',rely = '0.47',anchor = 'center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)


# Botao de resposta
get_resposta = tk.Button(window,text = 'Gerar Resposta',bg = 'white',command = resposta)
get_resposta['font'] = font2
get_resposta.place(relx = '0.29',rely = '0.72')

# Label disciplina SEL0456
art = tk.Label(window,text = 'Sistemas Embarcados SEL0456')
art['font'] = font3
art.place(relx = '0.35',rely = '0.9')

# Label grandeza
art2 = tk.Label(window,text = 'Grandeza',bg = '#415557')
art2['font'] = font3
art2.place(relx = '0.01',rely = '0.27')

# Label unidades
art3 = tk.Label(window,text = 'Unidade 2',bg = '#415557')
art3['font'] = font3
art3.place(relx = '0.01', rely = '0.43')

# Label unidades
art5 = tk.Label(window,text = 'Unidade 1',bg = '#415557')
art5['font'] = font3
art5.place(relx = '0.01',rely = '0.35')

# Label valor
art5 = tk.Label(window,text = 'Valor',bg = '#415557')
art5['font'] = font3
art5.place(relx = '0.01',rely = '0.58')

# Label resposta
art5 = tk.Label(window,text = 'Resposta',bg = '#415557')
art5['font'] = font3
art5.place(relx = '0.01',rely = '0.65')

# Caixa resultado
result = tk.Label(window,text = '',bg= 'white',width = 25)
result['font'] = font3
result.place(relx = '0.29',rely = '0.65')


# Aplicativo em loop
window.mainloop()