import pandas as pd


def mean_diagnostic(df, value):
    return len(df.loc[df.Diagnostic == value].values) / len(df.values)


def get_values_of(df, column, diagnostic=2):
    df_class = df.loc[df.Diagnostic == diagnostic]
    df_range = df.groupby(column).apply(list).reset_index()[column].values
    return df_class[column]


def get_frequency_of(df, column, diagnostic=2):
    df_class = df.loc[df.Diagnostic == diagnostic]
    df_range = df.groupby(column).apply(list).reset_index()[column].values
    df_normalized = df_class[column].value_counts().reindex(range(1, len(df_range) + 1)).fillna(0)
    return df_normalized.div(df_normalized.sum(axis=0), axis=0)


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
    return pd.read_csv('./Train.csv',
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
        if value > 0 :
            productorio_values = value * productorio_values
            prod += " x {0}".format(value)
        else:
            productorio_values = 0.001 * productorio_values
            prod += " x {0}".format(0.001)
    print(prod)
    print(productorio_values)
    return productorio_values


if __name__ == "__main__":
    df = get_dataframe()
    mean_beligno = mean_diagnostic(df, 2)
    mean_maligno = mean_diagnostic(df, 4)
    dtnb = dataframe_normalized(df, 2)
    dtnm = dataframe_normalized(df, 4)
    columns = get_columns()
    columns.pop(0)
    columns.pop()

    print(mean_beligno)
    print(dtnb)
    for idx, column in enumerate(columns, start=0):
        print(idx)
        print(column)
        prod_of_values(dtnb.iloc[idx], mean_beligno)

    print(mean_maligno)
    print(dtnm)
    print(mean_maligno)
    for idx, column in enumerate(columns, start=0):
        print(idx)
        print(column)
        prod_of_values(dtnb.iloc[idx], mean_maligno, 4)
