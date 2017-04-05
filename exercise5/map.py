import pandas as pd
import numpy as np
import csv
def mean_diagnostic(df, value):
    return len(df.loc[df.Class == value].values) / len(df.values)


def get_values_of(df, column, diagnostic=2):
    df_class = df.loc[df.Diagnostic == diagnostic]
    df_range = df.groupby(column).apply(list).reset_index()[column].values
    return df_class[column]


def get_frequency_of(df, column, cls=2):
    df_class = df.loc[df.Class == cls]
    df_range = df.groupby(column).apply(list).reset_index()[column].values
    df_normalized = df_class[column].value_counts().reindex(range(1, len(df_range) + 1)).fillna(0)
    return df_normalized.div(df_normalized.sum(axis=0), axis=0)


def get_columns():
    columns = open('columns.csv', 'r').read().split('\n')
    columns.pop()
    return columns


def get_values():
    values = open('values.csv', 'r').read().split('\n')
    values.pop()
    return values


def get_dataframe():
    column_names = get_columns()
    return pd.read_csv('./Robot_Train.csv',
                       names=column_names)


def dataframe_normalized(df, diagnostic=2):
    columns = get_columns()
    columns.pop(0)
    columns.pop()
    ls = []
    for column in columns:
        ls.append(get_frequency_of(df, column, diagnostic).values)
    return pd.DataFrame(ls, columns=list(range(1, 11)), index=columns)


def prod_of_values(df, mean, diagnostic=2):
    if diagnostic == 2:
        print("P(M) = {0}".format(abs(mean - 1)))
        prod = "P(B) = {0}".format(mean)
    else:
        print("P(B) = {0}".format(abs(mean - 1)))
        prod = "P(M) = {0}".format(mean)

    productorio_values = mean
    for value in df.values:
        if value > 0:
            productorio_values = value * productorio_values
            prod += " x {0}".format(value)
        else:
            productorio_values = 0.001 * productorio_values
            prod += " x {0}".format(0.001)
    print(prod)
    print(productorio_values)
    return productorio_values


def frequency_of(df, cls):
    df_class = df.loc[df.Class == cls]
    values = open('values.csv', 'r').read().split('\n')
    values.pop()
    columns = get_columns()
    columns.pop(0)
    dt = pd.DataFrame([], index=columns, columns=get_values()).fillna(1)
    for column in columns:
        counted = df_class[column].value_counts().tolist()
        index_list = df_class[column].value_counts().index.values
        for index, counted in enumerate(counted):
            dt[str(index_list[index])][column] = counted + dt[str(index_list[index])][column]
    dt.to_csv("{}_frequency.csv".format(cls), encoding='utf-8')
    return dt


def normalized_of(df, cls):
    # normalizar
    columns = get_columns()
    columns.pop(0)

    dtn = pd.DataFrame([], index=columns, columns=get_values()).fillna(0).astype('float64')
    for value in get_values():
        for column in columns:
            dtn[value][column] = float(df[value][column] / df[value].sum())
    dtn.to_csv("{}_normalized.csv".format(cls), encoding='utf-8')
    return dtn


def data():
    df = get_dataframe()
    # 1
    dt1 = frequency_of(df, 1)
    print("normalizando clase 1")
    dt1n = normalized_of(dt1, 1)
    # 2
    dt2 = frequency_of(df, 2)
    print("normalizando clase 2")
    dt2n = normalized_of(dt2, 2)
    # 3
    dt3 = frequency_of(df, 3)
    print("normalizando clase 3")
    dt3n = normalized_of(dt3, 3)
    # 4
    dt4 = frequency_of(df, 4)
    print("normalizando clase 4")
    dt4n = normalized_of(dt4, 4)
    # 5
    dt5 = frequency_of(df, 5)
    print("normalizando clase 5")
    dt5n = normalized_of(dt5, 5)


def test():
    ls = [1,2,3,4,5]
    mdf = [1,2,3,4,5]
    ls[0] = pd.DataFrame.from_csv("1_normalized.csv")
    ls[1] = pd.DataFrame.from_csv("2_normalized.csv")
    ls[2] = pd.DataFrame.from_csv("3_normalized.csv")
    ls[3] = pd.DataFrame.from_csv("4_normalized.csv")
    ls[4] = pd.DataFrame.from_csv("5_normalized.csv")
    df = get_dataframe()
    mdf[0] = mean_diagnostic(df, 1)
    mdf[1] = mean_diagnostic(df, 2)
    mdf[2] = mean_diagnostic(df, 3)
    mdf[3] = mean_diagnostic(df, 4)
    mdf[4] = mean_diagnostic(df, 5)
    columns = get_columns()
    columns.pop(0)
    result = []
    with open('Robot_Test.csv', 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            m = line[0].split(',')
            cls = m[0]
            print(int(cls))
            priori = mdf[int(cls) - 1]
            m.pop(0)
            df = ls[int(cls) - 1]

            for x, value in enumerate(m):
                print(df[value][columns[x]])
                priori = priori * df[value][columns[x]]
            result.append("{}, {}".format(cls, priori))
        print(result)
        my_df = pd.DataFrame(result)
        my_df.to_csv('result.csv', index=False, header=False)


if __name__ == "__main__":
    #    test()
    test()
