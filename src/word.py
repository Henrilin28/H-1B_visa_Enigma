def generate_word(df):
    list_ = []
    for idx, row in df.iterrows():
        times = row[1]
        list_.append([row[0]]*times)
    return list_

def extract_word(word_l):
    temp = []
    for x in word_l:
        for y in x:
            a = y.split(" ")
            if len(a) >1:
                for j in a:
                    temp.append(j)
            else:
                temp.append(a[0])
    return temp
