from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors

from el_phys_p2 import *
from paragraph_styles import *
from page_number import *
from title_list import *
from eq import *
from graphic import grf

# from in_dat import *
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
sp_30 = Spacer(0, 30)
sp_50 = Spacer(0, 50)
sp_2 = Spacer(0, 2 * cm)
s_80 = Spacer(0, 80)
s_100 = Spacer(0, 100)
s_110 = Spacer(0, 110)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
s_150 = Spacer(0, 150)
p_b = PageBreak

f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_130, sity]),
     Paragraph('Цель работы', style=s_b),
     Paragraph('Исследовать переходные процессы в цепях с сосредоточенными параметрами', style=s_m),
     KeepTogether([Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\Исходная схема 2.png',
                         width=10 * cm, height=10 * cm, kind='proportional'),
                   Paragraph('Рис. 1 - Схема заданной цепи', style=s_cntr)]),
     Paragraph('Исходные данные', style=s_b),
     Table(data=[[fml(f'$L$, Гн'), fml(f'$C$, мкФ'), fml(f'Характер процесса')],
                 [fml(f'${cnst.l}$'), fml(f'${cnst.c * 10 ** 6}$'), fml(f'Колебательный')]],
           colWidths=150, rowHeights=20, spaceBefore=5,
           spaceAfter=5, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)]),
     # Paragraph('Задание', style=s_b),
     # Paragraph('Исследовать переходные процессы в цепях с сосредоточенными параметрами', style=s_m),
     Paragraph('Система уравнений, описывающих заданную цепь', style=st_0_10),
     # fml(f'$\\left\\{{\\begin{{array}}{{rcl}}'
     #     f'x^2+y^2&=&7\\x+y & = &3.\\ \\end{{array}} \\right$')
     # fml('$\\begin{equation}  \\left\\{\\begin{array}{@{}l@{}}    k_{i\\omega}/k_{p\\omega}=2\\pi\\times 10\\    \\left|      '
     #     '\\frac{k_{p\\omega}s+k_{i\\omega}}{s}\\cdot\\frac {1}{Ts+1}    '
     #     '\\right|_{S=\\mathrm{j}\\cdot2\\pi}=1  \\end{array}\\right.\\,.\\end{equation}$')
     fml('$i_L + i_1 - i_C - i_2 = 0; \\quad i_C = i_L + i_1 - i_2$'),
     sp_20,
     fml('$i_1R_1 + u_c = e; \\quad i_1 = \\dfrac{e - u_c} {R_1}$'),
     sp_20,
     fml('$i_2 = \\dfrac {u_C} {R_2}$'),
     sp_25,
     fml('$\\dfrac {du_C} {dt} = \\dfrac {1} {C} i_C$'),
     sp_25,
     fml('$\\dfrac {di_L} {dt} = \\dfrac {1} {L} i_1 R1$'),
     sp_30,
     fml('Подставим значения $i_1$ и $i_C$, выраженные через $i_L$ и $u_С$, в выражения в форме Коши'),
     sp_20,
     fml('$\\dfrac {du_C} {dt} = \\dfrac {1} {C} \\left[i_L + \\dfrac {e - u_c} {R_1} - \\dfrac {u_c} {R_2}\\right]$'),
     sp_30,
     fml('$\\dfrac {di_L} {dt} = e - u_C$'),
     Paragraph('Расчет переходного процесса по полученным выражениям произведен в среде Python с использованием '
               'функции solve_ivp библиотеки scipy.integrate. Вывод графиков осуществлен средствами'
               ' библиотеки matplotlib.pyplot', style=st_10_3),

     Paragraph('Результат расчета при постоянной ЭДС E = 1 В', style=st_5_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\const i.png',
                         width=15 * cm, height=15 * cm, kind='proportional'),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\const u.png',
                         width=15 * cm, height=15 * cm, kind='proportional'),
     # p_b,
     # grf(f1),
     # sp_50,
     # Image(drw1),
     Paragraph('Установившиеся значения тока и напряжения:', style=st_5_10),
     fml(f'$u_{{C_\u0020 уст}} = {cnst.u_c[-1]:.3f}$ В'),
     sp_10,
     fml(f'$i_{{L_\u0020 уст}} = {cnst.i[-1] * 10**3:.2f}$ мА'),
     Paragraph('Максимальные значения тока и напряжения:', style=st_20_20),
     fml(f'$u_{{C_\u0020 max}} = {max(cnst.u_c):.3f}$ В'),
     sp_10,
     fml(f'$i_{{L_\u0020 max}} = {max(cnst.i) * 10**3:.1f}$ мА'),

     KeepTogether([
          Paragraph('Результат расчета при переменной ЭДС', style=st_20_20),
          fml('$e(t) = sin \\left(\\omega t \\right)$'),
          sp_10,
          Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\sin i.png',
                         width=15*cm, height=15*cm, kind='proportional')]),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\sin u.png',
                         width=15*cm, height=15*cm, kind='proportional'),
     # p_b,
     # grf(f1),
     # Image(drw1),
     # '''
     # '''
     Paragraph('Амплитудные значения установившихся тока и напряжения:', style=st_20_20),
     fml(f'$u_{{C_\u0020 уст}} = {0.3}$ В'),
     sp_10,
     fml(f'$i_{{L_\u0020 уст}} = {2.7}$ мА'),

     Paragraph('Максимальные значения тока и напряжения:', style=st_20_20),
     fml(f'$u_{{C_\u0020 max}} = {max(sin.u_c1):.1f}$ В'),
     sp_10,
     fml(f'$i_{{L_\u0020 max}} = {max(sin.i1) * 10**3:.2f}$ мА'),

     KeepTogether(
          [Paragraph('Ручной расчет', style=st_b_10_2),
           Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\Scan_20250309_164207.jpg',
           width=10*cm, height=20*cm, kind='proportional')]),  # из тетради
     sp_10,
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\Scan_20250309_164254.jpg',
           width=10*cm, height=10*cm, kind='proportional'),
     # Paragraph('5.  а емкость - разрывом цепи. '),
     # Paragraph('При постоянной ЭДС индуктивность является закороткой, а емкость - разрывом цепи. '
     #           'Тогда:', style=st_5_5),
     # fml(f'$i_{{L_\u0020 вын}} = i_{{R_\u0020 2}} = \\dfrac {{e}} {{R_2}}; '
     #     f'\\quad i_{{L_\u0020 вын}} = \\dfrac {{{cnst.e}}} {{{cnst.r2}}} = {cnst.e / cnst.r2}$ А'),
     # sp_20,
     # fml(f'$u_{{C_\u0020 вын}} = e \\quad ;'
     #     f'u_{{c_\u0020 вын}} = {cnst.e}$ В'),

     Paragraph('При постоянной ЭДС E = 1 В', style=st_0_25),
     fml(f'$U_{{пер}} = \\sqrt {{(u_{{вын}}(0) - u_0)^2 + Z^2(i_{{вын}}(0) - i_0)^2}}$'),
     sp_20,
     fml(f'$I_{{пер}} = \\sqrt {{(u_{{вын}}(0) - u_0)^2 / Z^2 + (i_{{вын}}(0) - i_0)^2}}$'),
     sp_20,
     fml(f'где $Z = \\sqrt{{ \\dfrac {{L}} {{C}} }}$ - характеристическое сопротивление контура; $\\quad Z = {z_c}$'),
     sp_30,
     fml(f'$U_{{пер}} = \\sqrt {{({abs(u_c_f[1]):.2f} - {u0})^2 + {z_c:.0f}^2 \\cdot ({abs(i_l_f[1]):.4f} - {i0})^2}} = {abs(u_p[1]):.2f}$ В'),
     sp_25,
     fml(f'$I_{{пер}} = \\sqrt {{({abs(u_c_f[1]):.2f} - {u0})^2 / {z_c:.0f}^2 + ({abs(i_l_f[1]):.4f} - {i0})^2}}$ = {abs(i_f[1]):.4f} А'),
     sp_25,
     fml(f'$tan\\phi_{{п}} = -\\dfrac{{z(i_{{вын}}(0) - i0)}} {{u_{{вын}}(0) - u0}} = {abs(tg_phi_p[1]):.3f}$'),
     sp_30,
     fml(f'$t^u_{{max}} = \\dfrac{{ {{\\pi}} - \\phi_{{п}} }} {{\\omega_0}} = {abs(t_m_u[1] * 10 ** 3):.2f}$ мс'),
     sp_30,
     fml(f'$t^i_{{max}} = \\dfrac{{ {{\\pi / 2}} - \\phi_{{п}} }} {{\\omega_0}} = {abs(t_m_i[1] * 10 ** 3):.1f}$ мс'),
     sp_30,
     fml(f'$K_{{уд}}^u = e^{{-\\delta * t^u_max}} + 1 = {abs(k_s_u[1]):.3f}$'),
     sp_20,
     fml(f'$K_{{уд}}^i = e^{{-\\delta * t^i_max}} + 1 = {abs(k_s_i[1]):.3f}$'),
     sp_30,

     Paragraph('При переменной ЭДС', style=st_0_10),
     fml('$e(t) = sin \\left(\\omega t \\right)$'),
     sp_20,
     fml(f'$U_{{пер}} = \\sqrt {{({abs(u_c_f[0]):.2f} - {u0})^2 + {z_c:.0f}^2 \\cdot ({abs(i_l_f[0]):.4f} - {i0})^2}} = {abs(u_p[0]):.2f}$ В'),
     sp_25,
     fml(f'$I_{{пер}} = \\sqrt {{({u_c_f[0]:.2f} - {u0})^2 / {z_c:.0f}^2 + ({i_l_f[0]:.4f} - {i0})^2}}$ = {abs(i_f[0]):.4f} А'),
     sp_25,
     fml(f'$i_{{вын}} = \\dfrac {{e}} {{Z}}$'),
     sp_30,
     fml(f'$Z = \\dfrac{{x_c R_2}} {{x_c + R_2}} + \\dfrac {{x_L R1}} {{x_L + R_1}}; '
         f'Z = {polar(z_f)[0]:.1f} \u2220 {polar(z_f)[1]:.1f}$ Ом'),
     sp_30,
     fml(f'$i_{{вын}} = \\dfrac {{{e_a[0]}}} {{{z_f:.1f}}} '
         f'= {polar(i_f[0])[0] * 10 ** 3:.1f} \u2220 {polar(i_f[0])[1]:.1f}$ мА'),
     sp_30,
     fml(f'$i_{{L_\u0020 вын}} = i_{{вын}}  \\dfrac {{R_1}} {{x_l + R_1}} = '
         f'{polar(i_l_f[0]*10**3)[0]:.2f} \u2220 {polar(i_f[0])[1]:.1f}$ мА'),
     sp_25,
     fml(f'$i_{{1_\u0020 вын}} = i_{{вын}} - i_{{L_\u0020 вын}} = {i1_f[0]*10**3:.2f}$ мА'),
     sp_20,
     fml(f'$U_{{C_\u0020 вын}} = E - i_{{1_\u0020 вын}} R_1 = {u_c_f[0]:.3f}$ В'),
     sp_25,
     fml(f'$tan\\phi_{{п}} = -\\dfrac{{z(i_{{вын}}(0) - i0)}} {{u_{{вын}}(0) - u0}} = {abs(tg_phi_p[0]):.3f}$'),
     sp_30,
     fml(f'$t^u_{{max}} = \\dfrac{{ {{\\pi}} - \\phi_{{п}} }} {{\\omega_0}} = {abs(t_m_u[0] * 10**3):.2f}$ мс'),
     sp_30,
     fml(f'$t^i_{{max}} = \\dfrac{{ {{\\pi / 2}} - \\phi_{{п}} }} {{\\omega_0}} = {abs(t_m_i[0] * 10**3):.1f}$ мс'),
     sp_30,
     fml(f'$K_{{уд}}^u = e^{{-\\delta t^u_{{max}}}} + 1 = {abs(k_s_u[0]):.3f}$'),
     sp_20,
     fml(f'$K_{{уд}}^i = e^{{-\\delta t^i_{{max}}}} + 1 = {abs(k_s_i[0]):.3f}$'),
     Paragraph('Вывод: в результате работы выполнено моделирование переходного процесса '
               'в заданной схеме электрической цепи. Результат моделирования проверен ручным счетом.', style=st_10_3),
     ]

doc.build(f, onLaterPages=addPageNumber)
