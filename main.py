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
    conf = 0.0
    for i in range(k, n + 1):
        conf += nkCalc(n, i) * (p ** i) * ((1 - p) ** (n - i))

    return conf


def main():
    data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
            'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
            }

    figure = plt.Figure(figsize=(6, 5), dpi=100)


    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().pack()
    df = df[['First Column', 'Second Column']].groupby('First Column').sum()
    df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
    ax.set_title('The Title for your chart')
    df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])
    
    print(df2)
    print('o confiabilidade da aplicação é:', confCalc(4, 3, 0.65))


if __name__ == "__main__":
    main()
