import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact = fact * i

    return fact


def nkCalc(n, k):
    if n-k == 0:
        const = 1
    else:
        const = n-k
    return factorial(n) / (factorial(const) * factorial(k))


def confCalc(n):
    conf = 0.0
    k = [1, n/2, n]
    p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    dados1 = {'p calculado': [],
        'confiabilidade': []
        }
    dados2 = {'p calculado': [],
        'confiabilidade': []
        }
    dados3 = {'p calculado': [],
        'confiabilidade': []
        }
    for m in p:
        for j in k:
            for i in range(int(j), n + 1):
                conf += nkCalc(n, i) * (m ** i) * ((1 - m) ** (n - i))
            if j == 1:
                dados1['confiabilidade'].append(conf*100)
                dados1['p calculado'].append(m)
            if j == n/2:
                dados2['p calculado'].append(m)
                dados2['confiabilidade'].append(conf*100)
            if j == n:
                dados3['p calculado'].append(m)
                dados3['confiabilidade'].append(conf*100)
            conf = 0
            

    return dados1, dados2, dados3


def central():
    n = maquinas.get(1.0, "end-1c")
    dados1, dados2, dados3 = confCalc(int(n))
    df1 = DataFrame(dados1, columns=['p calculado', 'confiabilidade'])
    df3 = DataFrame(dados2, columns=['p calculado', 'confiabilidade'])
    df4 = DataFrame(dados3, columns=['p calculado', 'confiabilidade'])
    root = tk.Tk()

    figure1 = plt.Figure(figsize=(6, 6), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)
    line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['p calculado', 'confiabilidade']].groupby('p calculado').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
    ax1.set_title('K = 1')

    figure2 = plt.Figure(figsize=(6, 6), dpi=100)
    ax3 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df3 = df3[['p calculado', 'confiabilidade']].groupby('p calculado').sum()
    df3.plot(kind='line', legend=True, ax=ax3, color='b', marker='o', fontsize=10)
    ax3.set_title('K = n/2')

    figure3 = plt.Figure(figsize=(6, 6), dpi=100)
    ax4 = figure3.add_subplot(111)
    line3 = FigureCanvasTkAgg(figure3, root)
    line3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df4 = df4[['p calculado', 'confiabilidade']].groupby('p calculado').sum()
    df4.plot(kind='line', legend=True, ax=ax4, color='y', marker='o', fontsize=10)
    ax4.set_title('k = n')

    
    root.mainloop()


# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('500x300')

# TextBox Creation
maquinas = tk.Text(frame,
                height = 2,
                width = 20)
maquinas.pack()

# Button Creation
printButton = tk.Button(frame,
                        text = "Calcular", 
                        command = central)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()