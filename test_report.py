from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors

from paragraph_styles import *
from page_number import *
from title_list import *
from eq import *
from graphic import grf

# from in_dat import *
# from el_phys_l1_const import f1, f2, drw1, u_c, i
import el_phys_l1_const as cnst
import el_phys_l1_sin as sin

doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Кашталапов, Эн1-22, ЛР 1')

sp_10 = Spacer(0, 10)
sp_15 = Spacer(0, 15)
sp_20 = Spacer(0, 20)
sp_1 = Spacer(0, 1 * cm)
sp_25 = Spacer(0, 25)
sp_50 = Spacer(0, 50)
sp_2 = Spacer(0, 2 * cm)
s_80 = Spacer(0, 80)
s_100 = Spacer(0, 100)
s_110 = Spacer(0, 110)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
s_150 = Spacer(0, 150)
p_b = PageBreak

r'''
f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_130, sity]),
     p_b,
     Paragraph('Цель работы', style=s_b),
     Paragraph('Исследовать переходные процессы в цепях с сосредоточенными параметрами', style=s_m),
     # KeepTogether([Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\Заданная схема.png',
     #                     width=10*cm, height=10*cm, kind='proportional'),
     # Paragraph('Рис. 1 - Схема заданной цепи', style=s_cntr)]),
     # Paragraph('Исходные данные', style=s_b),
     # Table(data = [[fml(f'$L$, Гн'), fml(f'$C$, мкФ'), fml(f'Характер процесса')],
     #               [fml(f'${cnst.l}$'), fml(f'${cnst.c*10**6}$'), fml(f'Колебательный')]],
     #       colWidths=70, rowHeights=20, spaceBefore=5,
     # spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1, colors.black)]),
     # # Paragraph('Задание', style=s_b),
     # # Paragraph('Исследовать переходные процессы в цепях с сосредоточенными параметрами', style=s_m),
     # Paragraph('Система уравнений, описывающих заданную цепь', style=st_0_20),
     # '''
     # fml(f'$\\left\\{{\\begin{{array}}{{rcl}}'
     #     f'x^2+y^2&=&7\\x+y & = &3.\\ \\end{{array}} \\right$')
# fml('$\\begin{equation}  \\left\\{\\begin{array}{@{}l@{}}    k_{i\\omega}/k_{p\\omega}=2\\pi\\times 10\\    \\left|      '
#     '\\frac{k_{p\\omega}s+k_{i\\omega}}{s}\\cdot\\frac {1}{Ts+1}    '
#     '\\right|_{S=\\mathrm{j}\\cdot2\\pi}=1  \\end{array}\\right.\\,.\\end{equation}$')
     fml('$i_L + i_1 - i_C - i_2 = 0; \\quad i_C = i_L + i_1 - i_2$'),
     sp_15,
     fml('$i_1R_1 + u_c = e \\quad i_1 = \\dfrac{e - u_c} {R_1}$'),
     sp_20,
     fml('$i_2 = u_c \\dfrac {u_C} {R_2}$'),
     sp_20,
     fml('$\\dfrac {du_C} {dt} = \\dfrac {1} {C} i_C$'),
     sp_20,
     fml('$\\dfrac {di_L} {dt} = \\dfrac {1} {L} i_1 R1$'),
     sp_15,
     fml('Подставим значения $i_1$ и $i_C$, выраженные через $i_L$ и $u_С$, в выражения в форме Коши'),
     sp_20,
     fml('$\\dfrac {du_C} {dt} = \\dfrac {1} {C} \\left[i_L + \\dfrac {e - u_c} {R_1} - \\dfrac {u_c} {R_2}\\right]$'),
     sp_20,
     fml('$\\dfrac {di_L} {dt} = e - u_C$'),
     Paragraph('Расчет переходного процесса по полученным выражениям произведен в среде Python с использованием '
               'функции 𝘴𝘰𝘭𝘷𝘦_𝘪𝘷𝘱 библиотеки 𝘴𝘤𝘪𝘱𝘺.𝘪𝘯𝘵𝘦𝘨𝘳𝘢𝘵𝘦. Вывод графиков осуществлен средствами'
               ' библиотеки 𝘮𝘢𝘵𝘱𝘭𝘰𝘵𝘭𝘪𝘣.𝘱𝘺𝘱𝘭𝘰𝘵', style=st_20_20),

     Paragraph('Результат расчета при постоянной ЭДС E = 1 В', style=st_20_20),
     # p_b,
     # grf(f1),
     # sp_50,
     # Image(drw1),
     '''
     Paragraph('Установившиеся значения тока и напряжения:', style=st_20_20),
     fml(f'$u_{{C_\u0020 уст}} = {cnst.u_c[-1]}$'),
     sp_10,
     fml(f'$i_{{L_\u0020 уст}} = {cnst.i[-1]}$'),
     Paragraph('Максимальные значения тока и напряжения:', style=st_20_20),
     fml(f'$u_{{C_\u0020 max}} = {max(cnst.u_c)}$'),
     sp_10,
     fml(f'$i_{{L_\u0020 max}} = {max(cnst.i)}$'),

     Paragraph('Результат расчета при переменной ЭДС', style=st_20_20),
     fml('$e_1(t) = sin \\left(\\omega t + phi1\\right); \\quad \\phi_1 = 0$'),

     # p_b,
     # grf(f1),
     # Image(drw1),
     # '''

'''
     Paragraph('Установившиеся значения тока и напряжения:', style=st_15_5),
     fml(f'$u_{{C_\u0020 уст}} = {sin.u_c1[-1]}$'),
     sp_10,
     fml(f'$i_{{L_\u0020 уст}} = {sin.i1[-1]}$'),
     Paragraph('Максимальные значения тока и напряжения:', style=st_15_5),
     fml(f'$u_{{C_\u0020 max}} = {max(sin.u_c1)}$'),
     sp_10,
     fml(f'$i_{{L_\u0020 max}} = {max(sin.i1)}$'),
     sp_50,
     fml('$e_2(t) = sin \\left(\\omega t + phi2\\right); \\quad \\phi_2 = \\dfrac {\\pi} {2}$'),
     Paragraph('Установившиеся значения тока и напряжения:', style=st_0_10),
     fml(f'$u_{{C_\u0020 уст}} = {sin.u_c2[-1]}$'),
     sp_10,
     fml(f'$i_{{L_\u0020 уст}} = {sin.i2[-1]}$'),
     Paragraph('Максимальные значения тока и напряжения:', style=st_0_10),
     fml(f'$u_{{C_\u0020 max}} = {max(sin.u_c2)}$'),
     sp_10,
     fml(f'$i_{{L_\u0020 max}} = {max(sin.i2)}$'),
     Paragraph('Ручной расчет', style=st_b_5_0),
     Paragraph('При постоянной ЭДС индуктивность является закороткой, а емкость - разрывом цепи. Тогда:', style=st_5_5),
     fml(f'$i_{{L_\u0020 max}} = {max(sin.i2)}$'),
     # '''
     ]
'''
f = 
doc.build(f, onLaterPages=addPageNumber)

