import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mode

def pie_chart_diagnostic(df):
    mean_beligno = mean_diagnostic(df, 2)
    mean_maligno = mean_diagnostic(df, 4)
    labels = 'Malignos', 'Belignos'
    sizes = [mean_maligno, mean_beligno]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


def bar_chart_diagnostic(df):
    print('maligno:')
    print(len(df.loc[df.Diagnostic == 4].values))
    print('belignos:')
    print(len(df.loc[df.Diagnostic == 2].values))

    plt.rcdefaults()
    objects = ('Malignos', 'Belignos')
    y_pos = np.arange(len(objects))
    count = [
        len(df.loc[df.Diagnostic == 4].values),
        len(df.loc[df.Diagnostic == 2].values)
    ]
    plt.bar(y_pos, count, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Cantidad')
    plt.title('Cantidad de datos')
    plt.show()


def mean_diagnostic(df, value):
    return len(df.loc[df.Diagnostic == value].values) / len(df.values)


def get_values_of(df, column, diagnostic=2):
    df_class = df.loc[df.Diagnostic == diagnostic]
    df_range = df.groupby(column).apply(list).reset_index()[column].values
    return df_class[column]


def show_graph(data, column, title):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(data, "|", markersize=5)
    plt.xlabel('Numero')
    plt.ylabel(column, fontsize=16)
    plt.gca().yaxis.grid(True)
    plt.title('{} de los {}.'.format(column, title), fontsize=16, color='b')
    # In the latest release, it is no longer necessary to do anything
    # special to share axes across figures:
    # ax1.sharex_foreign(ax2)
    # ax2.sharex_foreign(ax1)
    # ax1.sharey_foreign(ax2)
    # ax2.sharey_foreign(ax1)
    plt.show()


def mean(data):
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n


def _ss(data):
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss


def pstdev(data):
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n
    return pvar**0.5


def get_columns():
    return [
        'ID',
        'Radius',
        'Texture',
        'Perimeter',
        'Area',
        'Smoothness',
        'Compactness',
        'Concavity',
        'Concave',
        'Symmetry',
        'Diagnostic'
    ]


def get_dataframe():
    column_names = get_columns()
    return pd.read_csv('./breastCancerWisconsinCorrected.csv',
                       names=column_names)

if __name__ == "__main__":
    df = get_dataframe()
    column = 'Symmetry'
    beligno = 'Beligno'
    maligno = 'Maligno'
    columns = get_columns()
    columns.pop(0)
    columns.pop()
    for column in columns:
        beligno_data = get_values_of(df, column).values
        maligno_data = get_values_of(df, column, 4).values
        print(column)
        print(beligno)
        print("La media es: {}".format(mean(beligno_data)))
        print("La moda es: {}".format(mode(beligno_data)))
        print("La std es: {}".format(pstdev(beligno_data)))
        print(maligno)
        print("La media es: {}".format(mean(maligno_data)))
        print("La moda es: {}".format(mode(maligno_data)))
        print("La std es: {}".format(pstdev(maligno_data)))
        print()
        # show_graph(beligno_data, column, beligno)
        # show_graph(maligno_data, column, maligno)
# pie_chart_diagnostic(df)
# bar_chart_diagnostic(df)
