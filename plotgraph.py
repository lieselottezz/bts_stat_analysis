from importfile import stat_55, stat_56, stat_57, stat_58
import pandas as pd
import pygal
def mainfunction():
    """Main function of Import part program"""
    csvfile = pd.read_csv('bts_all_stat.csv')
    dict_stat_55 = stat_55(csvfile, {})
    dict_stat_56 = stat_56(csvfile, {})
    dict_stat_57 = stat_57(csvfile, {})
    dict_stat_58 = stat_58(csvfile, {})
    all_onnut = []
    date_list = ['JAN 55', 'FEB 55', 'MAR 55', 'APR 55', 'MAY 55', 'JUN 55', 'JUL 55',\
     'AUG 55', 'SEP 55', 'OCT 55', 'NOV 55', 'DEC 55', 'JAN 56', 'FEB 56', 'MAR 56',\
      'APR 56', 'MAY 56', 'JUN 56', 'JUL 56', 'AUG 56', 'SEP 56', 'OCT 56', 'NOV 56', 'DEC 56',\
      'JAN 57', 'FEB 57', 'MAR 57', 'APR 57', 'MAY 57', 'JUN 57', 'JUL 57', 'AUG 57', 'SEP 57',\
       'OCT 57', 'NOV 57', 'DEC 57', 'JAN 58', 'FEB 58', 'MAR 58', 'APR 58', 'MAY 58', 'JUN 58',\
        'JUL 58', 'AUG 58', 'SEP 58', 'OCT 58', 'NOV 58', 'DEC 58']
    for i in dict_stat_55['On Nut']:
        all_onnut.append(i)
    for i in dict_stat_56['On Nut']:
        all_onnut.append(i)
    for i in dict_stat_57['On Nut']:
        all_onnut.append(i)
    for i in dict_stat_58['On Nut']:
        all_onnut.append(i)

    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    date_chart.x_labels = map(lambda d: d.strftime('%Y-%m')\
        , [datetime(2013, 1), datetime(2013, 2),\
        datetime(2013, 3), datetime(2013, 4)])
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS On Nut', all_onnut)
    line_chart.render_to_file('linechart_onnut.svg')

mainfunction()
