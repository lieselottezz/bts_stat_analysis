from dev import stat_55, stat_56, stat_57, stat_58
import pandas as pd
def mainfunction():
    """Main function of Import part program"""
    csvfile = pd.read_csv('btsstat58csv.csv')
    dict_stat_55 = stat_55(csvfile, {})
    dict_stat_56 = stat_56(csvfile, {})
    dict_stat_57 = stat_57(csvfile, {})
    dict_stat_58 = stat_58(csvfile, {})
    for i in dict_stat_58:
        print(i)

mainfunction()
