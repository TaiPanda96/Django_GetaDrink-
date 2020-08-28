import pandas as pd 
import sys
import json 
import csv

def dump(items_table):
    try:
        df = pd.DataFrame(data=items_table).to_dict(orient='records')
        print(df)
        return df 
    except:
        print(sys.exc_info()[0], sys.exc_info()[1])
    
def dump_category(items_table):
    try:
        df = pd.DataFrame(data=items_table)
        #print(df)
        return df 
    except:
        print(sys.exc_info()[0], sys.exc_info()[1])

