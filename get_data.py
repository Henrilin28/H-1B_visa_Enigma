import json
import pprint
import cPickle as pickle
from urllib import urlopen
import sys
import pandas as pd


def get_jsonparsed_data(url):

    d = json.load(urlopen(url))
    return d

json_file = get_jsonparsed_data(sys.argv[1])

# save file for testing
with open('H1B_jason.pickle', 'wb') as handle:
    pickle.dump(json_file, handle)

for key, value in json_file["info"].iteritems():
    print key, value


df = pd.DataFrame(json_file["result"])
print df.info()
with open('H1B_df.pickle', 'wb') as handle:
    pickle.dump(df, handle)
