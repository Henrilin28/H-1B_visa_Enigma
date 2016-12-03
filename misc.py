def uni_wage(df):
    '''
    bc there are different wage unit such as week, bi-weekly, month, year.
    This function is used to unified wage in H-1B visa data.
    input: selected_data_frame
    output: unified_waged_data_frame
    '''

    attr_from = "lca_case_wage_rate_from"
    attr_to = "lca_case_wage_rate_to"
    for index, x in df.iterrows():

        if x["lca_case_wage_rate_unit"] == "Bi-Weekly":

            x[attr_from] = 24 * x[attr_from]
            x[attr_to] = 24 * x[attr_to]

        elif x["lca_case_wage_rate_unit"] == "Hour":

            if x[attr_from] < 50000 and x[attr_from] > 10:
                x[attr_from] = float(8760) * x[attr_from]
                x[attr_to] = float(8760) * x[attr_to]
            else:
                print "wrong_unit: Hour, pay:{}".format(x[attr_from])

        elif x["lca_case_wage_rate_unit"] == "Month":
            x[attr_from] = 12 * x[attr_from]
            x[attr_to] = 12 * x[attr_to]

        elif x["lca_case_wage_rate_unit"] == "UNKNOWN":

            drop_idx = index
            print drop_idx

        elif x["lca_case_wage_rate_unit"] == "Week":

            x[attr_from] = 48 * x[attr_from]
            x[attr_to] = 48 * x[attr_to]

        else:
            x[attr_from] = x[attr_from]
            x[attr_to] = x[attr_to]

    print "{} of application has been unified".format(len(df))

    return df


def generate_list(df):
    list_ = []
    for idx, row in df.iterrows():
        times = row.total_workers
        list_.extend([row.lca_case_wage_rate_from]*times)
    return list_
