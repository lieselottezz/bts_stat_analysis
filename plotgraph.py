"""Plot graph part"""
from importfile import stat_54, stat_55, stat_56, stat_57, stat_58
import pandas as pd
import pygal
def mainfunction():
    """Main function of Import part program"""
    csvfile = pd.read_csv('bts_all_stat.csv')
    dict_stat_54 = stat_54(csvfile, {})
    dict_stat_55 = stat_55(csvfile, {})
    dict_stat_56 = stat_56(csvfile, {})
    dict_stat_57 = stat_57(csvfile, {})
    dict_stat_58 = stat_58(csvfile, {})
    date_list = ['JAN 54', 'FEB 54', 'MAR 54', 'APR 54', 'MAY 54', 'JUN 54', 'JUL 54',\
    'AUG 54', 'SEP 54', 'OCT 54', 'NOV 54', 'DEC 54','JAN 55', 'FEB 55', 'MAR 55',\
    'APR 55', 'MAY 55', 'JUN 55', 'JUL 55','AUG 55', 'SEP 55', 'OCT 55', 'NOV 55',\
    'DEC 55', 'JAN 56', 'FEB 56', 'MAR 56','APR 56', 'MAY 56', 'JUN 56', 'JUL 56',\
    'AUG 56', 'SEP 56', 'OCT 56', 'NOV 56', 'DEC 56','JAN 57', 'FEB 57', 'MAR 57',\
    'APR 57', 'MAY 57', 'JUN 57', 'JUL 57', 'AUG 57', 'SEP 57', 'OCT 57', 'NOV 57',\
    'DEC 57', 'JAN 58', 'FEB 58', 'MAR 58', 'APR 58', 'MAY 58', 'JUN 58', 'JUL 58',\
    'AUG 58', 'SEP 58', 'OCT 58', 'NOV 58', 'DEC 58']
    mo_chit(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    saphan_khwai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    ari(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    sanam_pao(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    victory_monument(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    phaya_thai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    ratchathewi(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    siam(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    chit_lom(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    phloen_chit(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    nana(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    asok(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    phrom_phong(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    thong_lo(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    ekkamai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    phra_khanong(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    on_nut(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    bang_chak(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    punnawithi(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    udom_suk(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    bang_na(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    bearing(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    ratchadamri(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    sala_daeng(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    chong_nonsi(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    surasak(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    saphan_taksin(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    krung_thon_buri(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    wongwian_yai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    pho_nimit(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    talat_phlu(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    wutthakat(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    bang_wa(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)
    national_stadium(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list)

def mo_chit(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Mo Chit station statistics graph"""
    all_mo_chit = []
    for i in dict_stat_54['Mo Chit']:
        all_mo_chit.append(i)
    for i in dict_stat_55['Mo Chit']:
        all_mo_chit.append(i)
    for i in dict_stat_56['Mo Chit']:
        all_mo_chit.append(i)
    for i in dict_stat_57['Mo Chit']:
        all_mo_chit.append(i)
    for i in dict_stat_58['Mo Chit']:
        all_mo_chit.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Mo Chit station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Mo Chit', all_mo_chit)
    line_chart.render_to_file('linechart_mo_chit.svg')

def saphan_khwai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Saphan Khwai station statistics graph"""
    all_saphan_khwai = []
    for i in dict_stat_54['Saphan Khwai']:
        all_saphan_khwai.append(i)
    for i in dict_stat_55['Saphan Khwai']:
        all_saphan_khwai.append(i)
    for i in dict_stat_56['Saphan Khwai']:
        all_saphan_khwai.append(i)
    for i in dict_stat_57['Saphan Khwai']:
        all_saphan_khwai.append(i)
    for i in dict_stat_58['Saphan Khwai']:
        all_saphan_khwai.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Saphan Khwai station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Saphan Khwai', all_saphan_khwai)
    line_chart.render_to_file('linechart_saphan_khwai.svg')

def ari(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Ari station statistics graph"""
    all_ari = []
    for i in dict_stat_54['Ari']:
        all_ari.append(i)
    for i in dict_stat_55['Ari']:
        all_ari.append(i)
    for i in dict_stat_56['Ari']:
        all_ari.append(i)
    for i in dict_stat_57['Ari']:
        all_ari.append(i)
    for i in dict_stat_58['Ari']:
        all_ari.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Ari station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Ari', all_ari)
    line_chart.render_to_file('linechart_ari.svg')

def sanam_pao(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Sanam Pao station statistics graph"""
    all_sanam_pao = []
    for i in dict_stat_54['Sanam Pao']:
        all_sanam_pao.append(i)
    for i in dict_stat_55['Sanam Pao']:
        all_sanam_pao.append(i)
    for i in dict_stat_56['Sanam Pao']:
        all_sanam_pao.append(i)
    for i in dict_stat_57['Sanam Pao']:
        all_sanam_pao.append(i)
    for i in dict_stat_58['Sanam Pao']:
        all_sanam_pao.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Sanam Pao station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Sanam Pao', all_sanam_pao)
    line_chart.render_to_file('linechart_sanam_pao.svg')

def victory_monument(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Victory Monument station statistics graph"""
    all_victory_monument = []
    for i in dict_stat_54['Victory Monument']:
        all_victory_monument.append(i)
    for i in dict_stat_55['Victory Monument']:
        all_victory_monument.append(i)
    for i in dict_stat_56['Victory Monument']:
        all_victory_monument.append(i)
    for i in dict_stat_57['Victory Monument']:
        all_victory_monument.append(i)
    for i in dict_stat_58['Victory Monument']:
        all_victory_monument.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Victory Monument station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Victory Monument', all_victory_monument)
    line_chart.render_to_file('linechart_victory_monument.svg')

def phaya_thai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Phaya Thai station statistics graph"""
    all_phaya_thai = []
    for i in dict_stat_54['Phaya Thai']:
        all_phaya_thai.append(i)
    for i in dict_stat_55['Phaya Thai']:
        all_phaya_thai.append(i)
    for i in dict_stat_56['Phaya Thai']:
        all_phaya_thai.append(i)
    for i in dict_stat_57['Phaya Thai']:
        all_phaya_thai.append(i)
    for i in dict_stat_58['Phaya Thai']:
        all_phaya_thai.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Phaya Thai station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Phaya Thai', all_phaya_thai)
    line_chart.render_to_file('linechart_phaya_thai.svg')

def ratchathewi(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Ratchathewi station statistics graph"""
    all_ratchathewi = []
    for i in dict_stat_54['Ratchathewi']:
        all_ratchathewi.append(i)
    for i in dict_stat_55['Ratchathewi']:
        all_ratchathewi.append(i)
    for i in dict_stat_56['Ratchathewi']:
        all_ratchathewi.append(i)
    for i in dict_stat_57['Ratchathewi']:
        all_ratchathewi.append(i)
    for i in dict_stat_58['Ratchathewi']:
        all_ratchathewi.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Ratchathewi station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Ratchathewi', all_ratchathewi)
    line_chart.render_to_file('linechart_ratchathewi.svg')

def siam(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Siam station statistics graph"""
    all_siam = []
    for i in dict_stat_54['Siam']:
        all_siam.append(i)
    for i in dict_stat_55['Siam']:
        all_siam.append(i)
    for i in dict_stat_56['Siam']:
        all_siam.append(i)
    for i in dict_stat_57['Siam']:
        all_siam.append(i)
    for i in dict_stat_58['Siam']:
        all_siam.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Siam station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Siam', all_siam)
    line_chart.render_to_file('linechart_siam.svg')

def chit_lom(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Chit Lom station statistics graph"""
    all_chit_lom = []
    for i in dict_stat_54['Chit Lom']:
        all_chit_lom.append(i)
    for i in dict_stat_55['Chit Lom']:
        all_chit_lom.append(i)
    for i in dict_stat_56['Chit Lom']:
        all_chit_lom.append(i)
    for i in dict_stat_57['Chit Lom']:
        all_chit_lom.append(i)
    for i in dict_stat_58['Chit Lom']:
        all_chit_lom.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Chit Lom station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Chit Lom', all_chit_lom)
    line_chart.render_to_file('linechart_chit_lom.svg')

def phloen_chit(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Phloen Chit station statistics graph"""
    all_ploen_chit = []
    for i in dict_stat_54['Phloen Chit']:
        all_ploen_chit.append(i)
    for i in dict_stat_55['Phloen Chit']:
        all_ploen_chit.append(i)
    for i in dict_stat_56['Phloen Chit']:
        all_ploen_chit.append(i)
    for i in dict_stat_57['Phloen Chit']:
        all_ploen_chit.append(i)
    for i in dict_stat_58['Phloen Chit']:
        all_ploen_chit.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Phloen Chit station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Phloen Chit', all_ploen_chit)
    line_chart.render_to_file('linechart_ploen_chit.svg')

def nana(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Nana station statistics graph"""
    all_nana = []
    for i in dict_stat_54['Nana']:
        all_nana.append(i)
    for i in dict_stat_55['Nana']:
        all_nana.append(i)
    for i in dict_stat_56['Nana']:
        all_nana.append(i)
    for i in dict_stat_57['Nana']:
        all_nana.append(i)
    for i in dict_stat_58['Nana']:
        all_nana.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Nana station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Nana', all_nana)
    line_chart.render_to_file('linechart_nana.svg')

def asok(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Asok station statistics graph"""
    all_asok = []
    for i in dict_stat_54['Asok']:
        all_asok.append(i)
    for i in dict_stat_55['Asok']:
        all_asok.append(i)
    for i in dict_stat_56['Asok']:
        all_asok.append(i)
    for i in dict_stat_57['Asok']:
        all_asok.append(i)
    for i in dict_stat_58['Asok']:
        all_asok.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Asok station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Asok', all_asok)
    line_chart.render_to_file('linechart_asok.svg')

def phrom_phong(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Phrom Phong station statistics graph"""
    all_phrom_phong = []
    for i in dict_stat_54['Phrom Phong']:
        all_phrom_phong.append(i)
    for i in dict_stat_55['Phrom Phong']:
        all_phrom_phong.append(i)
    for i in dict_stat_56['Phrom Phong']:
        all_phrom_phong.append(i)
    for i in dict_stat_57['Phrom Phong']:
        all_phrom_phong.append(i)
    for i in dict_stat_58['Phrom Phong']:
        all_phrom_phong.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Phrom Phong station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Phrom Phong', all_phrom_phong)
    line_chart.render_to_file('linechart_phrom_phong.svg')

def thong_lo(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Thong Lo station statistics graph"""
    all_thong_lo = []
    for i in dict_stat_54['Thong Lo']:
        all_thong_lo.append(i)
    for i in dict_stat_55['Thong Lo']:
        all_thong_lo.append(i)
    for i in dict_stat_56['Thong Lo']:
        all_thong_lo.append(i)
    for i in dict_stat_57['Thong Lo']:
        all_thong_lo.append(i)
    for i in dict_stat_58['Thong Lo']:
        all_thong_lo.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Thong Lo station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Thong Lo', all_thong_lo)
    line_chart.render_to_file('linechart_thong_lo.svg')

def ekkamai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Ekkamai station statistics graph"""
    all_ekkamai = []
    for i in dict_stat_54['Ekkamai']:
        all_ekkamai.append(i)
    for i in dict_stat_55['Ekkamai']:
        all_ekkamai.append(i)
    for i in dict_stat_56['Ekkamai']:
        all_ekkamai.append(i)
    for i in dict_stat_57['Ekkamai']:
        all_ekkamai.append(i)
    for i in dict_stat_58['Ekkamai']:
        all_ekkamai.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Ekkamai station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Ekkamai', all_ekkamai)
    line_chart.render_to_file('linechart_ekkamai.svg')

def phra_khanong(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Phra Khanong station statistics graph"""
    all_phra_khanong = []
    for i in dict_stat_54['Phra Khanong']:
        all_phra_khanong.append(i)
    for i in dict_stat_55['Phra Khanong']:
        all_phra_khanong.append(i)
    for i in dict_stat_56['Phra Khanong']:
        all_phra_khanong.append(i)
    for i in dict_stat_57['Phra Khanong']:
        all_phra_khanong.append(i)
    for i in dict_stat_58['Phra Khanong']:
        all_phra_khanong.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Phra Khanong station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Phra Khanong', all_phra_khanong)
    line_chart.render_to_file('linechart_phra_khanong.svg')

def on_nut(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create On Nut station statistics graph"""
    all_on_nut = []
    for i in dict_stat_54['On Nut']:
        all_on_nut.append(i)
    for i in dict_stat_55['On Nut']:
        all_on_nut.append(i)
    for i in dict_stat_56['On Nut']:
        all_on_nut.append(i)
    for i in dict_stat_57['On Nut']:
        all_on_nut.append(i)
    for i in dict_stat_58['On Nut']:
        all_on_nut.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS On Nut station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS On Nut', all_on_nut)
    line_chart.render_to_file('linechart_on_nut.svg')

def bang_chak(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Bang Chak station statistics graph"""
    all_bang_chak = []
    for i in dict_stat_54['Bang Chak']:
        all_bang_chak.append(i)
    for i in dict_stat_55['Bang Chak']:
        all_bang_chak.append(i)
    for i in dict_stat_56['Bang Chak']:
        all_bang_chak.append(i)
    for i in dict_stat_57['Bang Chak']:
        all_bang_chak.append(i)
    for i in dict_stat_58['Bang Chak']:
        all_bang_chak.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Bang Chak station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Bang Chak', all_bang_chak)
    line_chart.render_to_file('linechart_bang_chak.svg')

def punnawithi(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Punnawithi station statistics graph"""
    all_punnawithi = []
    for i in dict_stat_54['Punnawithi']:
        all_punnawithi.append(i)
    for i in dict_stat_55['Punnawithi']:
        all_punnawithi.append(i)
    for i in dict_stat_56['Punnawithi']:
        all_punnawithi.append(i)
    for i in dict_stat_57['Punnawithi']:
        all_punnawithi.append(i)
    for i in dict_stat_58['Punnawithi']:
        all_punnawithi.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Punnawithi station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Punnawithi', all_punnawithi)
    line_chart.render_to_file('linechart_punnawithi.svg')

def udom_suk(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Udom Suk station statistics graph"""
    all_udom_suk = []
    for i in dict_stat_54['Udom Suk']:
        all_udom_suk.append(i)
    for i in dict_stat_55['Udom Suk']:
        all_udom_suk.append(i)
    for i in dict_stat_56['Udom Suk']:
        all_udom_suk.append(i)
    for i in dict_stat_57['Udom Suk']:
        all_udom_suk.append(i)
    for i in dict_stat_58['Udom Suk']:
        all_udom_suk.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Udom Suk station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Udom Suk', all_udom_suk)
    line_chart.render_to_file('linechart_udom_suk.svg')

def bang_na(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Bang Na station statistics graph"""
    all_bang_na = []
    for i in dict_stat_54['Bang Na']:
        all_bang_na.append(i)
    for i in dict_stat_55['Bang Na']:
        all_bang_na.append(i)
    for i in dict_stat_56['Bang Na']:
        all_bang_na.append(i)
    for i in dict_stat_57['Bang Na']:
        all_bang_na.append(i)
    for i in dict_stat_58['Bang Na']:
        all_bang_na.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Bang Na station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Bang Na', all_bang_na)
    line_chart.render_to_file('linechart_bang_na.svg')

def bearing(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Bearing station statistics graph"""
    all_bearing = []
    for i in dict_stat_54['Bearing']:
        all_bearing.append(i)
    for i in dict_stat_55['Bearing']:
        all_bearing.append(i)
    for i in dict_stat_56['Bearing']:
        all_bearing.append(i)
    for i in dict_stat_57['Bearing']:
        all_bearing.append(i)
    for i in dict_stat_58['Bearing']:
        all_bearing.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Bearing station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Bearing', all_bearing)
    line_chart.render_to_file('linechart_bearing.svg')

def ratchadamri(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Ratchadamri station statistics graph"""
    all_ratchadamri = []
    for i in dict_stat_54['Ratchadamri']:
        all_ratchadamri.append(i)
    for i in dict_stat_55['Ratchadamri']:
        all_ratchadamri.append(i)
    for i in dict_stat_56['Ratchadamri']:
        all_ratchadamri.append(i)
    for i in dict_stat_57['Ratchadamri']:
        all_ratchadamri.append(i)
    for i in dict_stat_58['Ratchadamri']:
        all_ratchadamri.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Ratchadamri station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Ratchadamri', all_ratchadamri)
    line_chart.render_to_file('linechart_ratchadamri.svg')

def sala_daeng(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Sala Daeng station statistics graph"""
    all_sala_daeng = []
    for i in dict_stat_54['Sala Daeng']:
        all_sala_daeng.append(i)
    for i in dict_stat_55['Sala Daeng']:
        all_sala_daeng.append(i)
    for i in dict_stat_56['Sala Daeng']:
        all_sala_daeng.append(i)
    for i in dict_stat_57['Sala Daeng']:
        all_sala_daeng.append(i)
    for i in dict_stat_58['Sala Daeng']:
        all_sala_daeng.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Sala Daeng station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Sala Daeng', all_sala_daeng)
    line_chart.render_to_file('linechart_sala_daeng.svg')

def chong_nonsi(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Chong Nonsi station statistics graph"""
    all_chong_nonsi = []
    for i in dict_stat_54['Chong Nonsi']:
        all_chong_nonsi.append(i)
    for i in dict_stat_55['Chong Nonsi']:
        all_chong_nonsi.append(i)
    for i in dict_stat_56['Chong Nonsi']:
        all_chong_nonsi.append(i)
    for i in dict_stat_57['Chong Nonsi']:
        all_chong_nonsi.append(i)
    for i in dict_stat_58['Chong Nonsi']:
        all_chong_nonsi.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Chong Nonsi station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Chong Nonsi', all_chong_nonsi)
    line_chart.render_to_file('linechart_chong_nonsi.svg')

def surasak(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Surasak station statistics graph"""
    all_surasak = []
    for i in dict_stat_54['Surasak']:
        all_surasak.append(i)
    for i in dict_stat_55['Surasak']:
        all_surasak.append(i)
    for i in dict_stat_56['Surasak']:
        all_surasak.append(i)
    for i in dict_stat_57['Surasak']:
        all_surasak.append(i)
    for i in dict_stat_58['Surasak']:
        all_surasak.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Surasak station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Surasak', all_surasak)
    line_chart.render_to_file('linechart_surasak.svg')

def saphan_taksin(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Saphan Taksin station statistics graph"""
    all_saphan_taksin = []
    for i in dict_stat_54['Saphan Taksin']:
        all_saphan_taksin.append(i)
    for i in dict_stat_55['Saphan Taksin']:
        all_saphan_taksin.append(i)
    for i in dict_stat_56['Saphan Taksin']:
        all_saphan_taksin.append(i)
    for i in dict_stat_57['Saphan Taksin']:
        all_saphan_taksin.append(i)
    for i in dict_stat_58['Saphan Taksin']:
        all_saphan_taksin.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Saphan Taksin station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Saphan Taksin', all_saphan_taksin)
    line_chart.render_to_file('linechart_saphan_taksin.svg')

def krung_thon_buri(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Krung Thon Buri station statistics graph"""
    all_krung_thon_buri = []
    for i in dict_stat_54['Krung Thon Buri']:
        all_krung_thon_buri.append(i)
    for i in dict_stat_55['Krung Thon Buri']:
        all_krung_thon_buri.append(i)
    for i in dict_stat_56['Krung Thon Buri']:
        all_krung_thon_buri.append(i)
    for i in dict_stat_57['Krung Thon Buri']:
        all_krung_thon_buri.append(i)
    for i in dict_stat_58['Krung Thon Buri']:
        all_krung_thon_buri.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Krung Thon Buri station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Krung Thon Buri', all_krung_thon_buri)
    line_chart.render_to_file('linechart_krung_thon_buri.svg')

def wongwian_yai(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Wongwian Yai station statistics graph"""
    all_wongwian_yai = []
    for i in dict_stat_54['Wongwian Yai']:
        all_wongwian_yai.append(i)
    for i in dict_stat_55['Wongwian Yai']:
        all_wongwian_yai.append(i)
    for i in dict_stat_56['Wongwian Yai']:
        all_wongwian_yai.append(i)
    for i in dict_stat_57['Wongwian Yai']:
        all_wongwian_yai.append(i)
    for i in dict_stat_58['Wongwian Yai']:
        all_wongwian_yai.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Wongwian Yai station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Wongwian Yai', all_wongwian_yai)
    line_chart.render_to_file('linechart_wongwian_yai.svg')

def pho_nimit(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Pho Nimit station statistics graph"""
    all_pho_nimit = []
    for i in dict_stat_54['Pho Nimit']:
        all_pho_nimit.append(i)
    for i in dict_stat_55['Pho Nimit']:
        all_pho_nimit.append(i)
    for i in dict_stat_56['Pho Nimit']:
        all_pho_nimit.append(i)
    for i in dict_stat_57['Pho Nimit']:
        all_pho_nimit.append(i)
    for i in dict_stat_58['Pho Nimit']:
        all_pho_nimit.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Pho Nimit station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Pho Nimit', all_pho_nimit)
    line_chart.render_to_file('linechart_pho_nimit.svg')

def talat_phlu(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Talat Phlu station statistics graph"""
    all_talat_phlu = []
    for i in dict_stat_54['Talat Phlu']:
        all_talat_phlu.append(i)
    for i in dict_stat_55['Talat Phlu']:
        all_talat_phlu.append(i)
    for i in dict_stat_56['Talat Phlu']:
        all_talat_phlu.append(i)
    for i in dict_stat_57['Talat Phlu']:
        all_talat_phlu.append(i)
    for i in dict_stat_58['Talat Phlu']:
        all_talat_phlu.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Talat Phlu station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Talat Phlu', all_talat_phlu)
    line_chart.render_to_file('linechart_talat_phlu.svg')

def wutthakat(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Wutthakat station statistics graph"""
    all_wutthakat = []
    for i in dict_stat_54['Wutthakat']:
        all_wutthakat.append(i)
    for i in dict_stat_55['Wutthakat']:
        all_wutthakat.append(i)
    for i in dict_stat_56['Wutthakat']:
        all_wutthakat.append(i)
    for i in dict_stat_57['Wutthakat']:
        all_wutthakat.append(i)
    for i in dict_stat_58['Wutthakat']:
        all_wutthakat.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Wutthakat station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Wutthakat', all_wutthakat)
    line_chart.render_to_file('linechart_wutthakat.svg')

def bang_wa(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create Bang Wa station statistics graph"""
    all_bang_wa = []
    for i in dict_stat_54['Bang Wa']:
        all_bang_wa.append(i)
    for i in dict_stat_55['Bang Wa']:
        all_bang_wa.append(i)
    for i in dict_stat_56['Bang Wa']:
        all_bang_wa.append(i)
    for i in dict_stat_57['Bang Wa']:
        all_bang_wa.append(i)
    for i in dict_stat_58['Bang Wa']:
        all_bang_wa.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS Bang Wa station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS Bang Wa', all_bang_wa)
    line_chart.render_to_file('linechart_bang_wa.svg')

def national_stadium(dict_stat_54, dict_stat_55, dict_stat_56, dict_stat_57, dict_stat_58, date_list):
    """Create National Stadium station statistics graph"""
    all_national_stadium = []
    for i in dict_stat_54['National Stadium']:
        all_national_stadium.append(i)
    for i in dict_stat_55['National Stadium']:
        all_national_stadium.append(i)
    for i in dict_stat_56['National Stadium']:
        all_national_stadium.append(i)
    for i in dict_stat_57['National Stadium']:
        all_national_stadium.append(i)
    for i in dict_stat_58['National Stadium']:
        all_national_stadium.append(i)
    line_chart = pygal.Line()
    line_chart.title = 'BTS National Stadium station statistics'
    line_chart.x_labels = map(str, date_list)
    line_chart.add('BTS National Stadium', all_national_stadium)
    line_chart.render_to_file('linechart_national_stadium.svg')

mainfunction()
