import pandas as pd


def demo():
    df_feature = pd.read_csv('./static/uploads/feature.csv')
    df_review = pd.read_csv('./static/uploads/review_feature.csv')
    df = pd.merge(df_feature, df_review, on="FeatureID")
    df_matrix = pd.read_csv('./static/uploads/matrix.csv')
    df_no = df.pivot_table(index=["ReviewID"], columns=[
                           "FeatureID"], values="n")
    df_no = df_no.fillna(0).reset_index()
    cols = list(df_no.columns)
    df_matrix.drop("Unnamed: 0", axis=1, inplace=True)
    cols_matrix = list(df_matrix.columns)
    # change type column df_matrix matching column table
    for i in range(len(cols_matrix)):
        for j in range(len(cols)):
            if cols_matrix[i] == cols[j]:
                df_matrix[cols_matrix[i]
                          ] = df_matrix[cols_matrix[i]].astype(float)
                break
    # remove first column of 2 data frames
    df_matrix.drop(df_matrix.columns[0], axis=1, inplace=True)
    df_no.drop(df_no.columns[0], axis=1, inplace=True)

    # add row 1 -> len of df_no to df_matrix
    len_no = len(df_no)
    len_matrix = len(df_matrix)
    for i in range(len_no):
        row = df_no.iloc[i]
        df_matrix.loc[len_matrix + i] = row.values

    print(df_matrix)

    return df_matrix.to_json(orient='records')
