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


def confCalc(n, k, p):
    dados1 = {'maquinas': [],
        'confiabilidade': []
        };
    conf = 0.0
    for i in range(k, n + 1):
        dados1['maquinas'].append(i)
        conf += nkCalc(n, i) * (p ** i) * ((1 - p) ** (n - i))
        dados1['confiabilidade'].append(conf*100)

    return dados1


def central():
    n = maquinas.get(1.0, "end-1c")
    k = minimo.get(1.0, "end-1c")
    p = confInd.get(1.0, "end-1c")
    dados = confCalc(int(n), int(k), float(p))
    dadoscomp = confCalc(int(1), int(1), float(p))
    df1 = DataFrame(dados, columns=['maquinas', 'confiabilidade'])
    df2 = DataFrame(dadoscomp, columns=['maquinas', 'confiabilidade'])
    root = tk.Tk()

    figure2 = plt.Figure(figsize=(6, 6), dpi=100)
    ax1 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['maquinas', 'confiabilidade']].groupby('maquinas').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
    ax1.set_title('caso com replicação')

    figure2 = plt.Figure(figsize=(6, 6), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['maquinas', 'confiabilidade']].groupby('maquinas').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('caso sem replicação')
    
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

minimo = tk.Text(frame,
                height = 2,
                width = 20)
minimo.pack()


confInd = tk.Text(frame,
                height = 2,
                width = 20)
confInd.pack()

# Button Creation
printButton = tk.Button(frame,
                        text = "Calcular", 
                        command = central)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()