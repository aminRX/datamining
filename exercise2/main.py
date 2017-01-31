import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def diagnosis_of_heart_disease_graph(df):
    x = df[58].values
    labels = '0', '1', '2', '3', '4'
    sizes = [
        np.count_nonzero(x == 0),
        np.count_nonzero(x == 1),
        np.count_nonzero(x == 2),
        np.count_nonzero(x == 3),
        np.count_nonzero(x == 4)
    ]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


def history_of_diabetes(df):
    not_diabetes = count_group_equals_to(-9, 17, df)
    ind = np.arange(5)
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, not_diabetes, width, color='y')
    diabetes = count_group_equals_to(1, 17, df)
    rects2 = ax.bar(ind + width, diabetes, width, color='r')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Camparacion de los grupos con antecedentes de diabetes')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('0', '1', '2', '3', '4'))
    ax.legend(
        (rects1[0], rects2[0]),
        ('Sin antecedentes de diabetes', 'Con antecedentes de diabetes')
    )
    plt.show()


def smoke_deseases_by_groups(df):
    not_smokers = count_group_equals_to(0, 14, df)
    ind = np.arange(5)
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, not_smokers, width, color='y')
    smokers = count_group_more_zero(0, 14, df)
    rects2 = ax.bar(ind + width, smokers, width, color='r')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Camparacion de los grupos por si fuman o no')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('0', '1', '2', '3', '4'))
    ax.legend((rects1[0], rects2[0]), ('No Fumadores', 'Fumadores'))
    plt.show()


def family_history_of_coronary_artery(df):
    not_famhist = count_group_equals_to(0, 18, df)
    ind = np.arange(5)
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, not_famhist, width, color='y')
    famhist = count_group_equals_to(1, 18, df)
    rects2 = ax.bar(ind + width, famhist, width, color='r')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Camparacion de los grupos por si tienen'
                 'familia con problemas cardiacos')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('0', '1', '2', '3', '4'))
    ax.legend(
        (rects1[0], rects2[0]),
        ('Sin historial familiar', 'Con historial familiar')
    )
    plt.show()


def get_all_58_groups(df):
    return (
        df.loc[df[58] == 0],
        df.loc[df[58] == 1],
        df.loc[df[58] == 2],
        df.loc[df[58] == 3],
        df.loc[df[58] == 4]
    )


def count_group_equals_to(value, index, df):
    group_0, group_1, group_2, group_3, group_4 = get_all_58_groups(df)
    return (
        np.count_nonzero(group_0[index].values == value),
        np.count_nonzero(group_1[index].values == value),
        np.count_nonzero(group_2[index].values == value),
        np.count_nonzero(group_3[index].values == value),
        np.count_nonzero(group_4[index].values == value)
    )


def count_group_more_zero(value, index, df):
    group_0, group_1, group_2, group_3, group_4 = get_all_58_groups(df)
    return (
        np.count_nonzero(group_0[index].values > value),
        np.count_nonzero(group_1[index].values > value),
        np.count_nonzero(group_2[index].values > value),
        np.count_nonzero(group_3[index].values > value),
        np.count_nonzero(group_4[index].values > value)
    )


if __name__ == "__main__":
    df = pd.read_excel('./heartdisease.xlsx')
    family_history_of_coronary_artery(df)
