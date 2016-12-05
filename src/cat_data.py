import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def plot_cat_info(df, class_1, class_2, sort1=True):

    if sort1:

        dftype = df[[class_1, class_2]]
        dftype1 = dftype.groupby(class_2).count()
        dftype1 = dftype1.fillna(0)

        if len(dftype1) > 5:
            plot_df = dftype1.sort_values("visa_class")[::-1][:5]
            plot_df.plot(kind="barh")
        else:
            plot_df = dftype1.sort_values("visa_class")[::-1]
            plot_df.plot(kind="barh")
            plot_df.plot(kind="barh")
        plt.gca().invert_yaxis()

    else:

        dftype = df[[class_1, class_2]]
        dftype1 = dftype.groupby([class_1, class_2]).size().unstack()
        dftype1 = dftype1.fillna(0)
        dftype1.plot(kind="barh")
        plt.gca().invert_yaxis()

    return dftype1


def dummyEncode(df):
        columnsToEncode = list(df.select_dtypes(include=['category', 'object']))
        le = LabelEncoder()
        for feature in columnsToEncode:
            try:
                df[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df


def generate_word(df):
    list_ = []
    for idx, row in df.iterrows():
        times = row[1]
        list_.extend([row[0]]*times)
    return list_
