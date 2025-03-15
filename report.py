from math import degrees

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
sp_40 = Spacer(0, 30)
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
     fml('$i_L + i_1 - i_C - i_2 = 0 \\quad \u21d2 \\quad i_C = i_L + i_1 - i_2$'),
     sp_20,
     fml('$i_1R_1 + u_c = e \\quad \u21d2 \\quad i_1 = \\dfrac{e - u_c} {R_1}$'),
     sp_20,
     fml('$i_2 = \\dfrac {u_C} {R_2}$'),
     sp_25,
     fml('$\\dfrac {du_C} {dt} = \\dfrac {1} {C} i_C$'),
     sp_25,
     fml('$\\dfrac {di_L} {dt} = \\dfrac {1} {L} i_1 R_1$'),
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
     sp_10,
     fml(f'$i_{{L_\u0020 уст}} = {cnst.i[-1] * 10**3:.0f}$ мА'),
     sp_20,
     # fml(f'$i_{{L_\u0020 уст}} = {cnst.i[-1] * 10**3:.2f}$ мА'),
     fml(f'$i_{{L_\u0020 max}} = {max(cnst.i) * 10**3:.1f}$ мА'),
     sp_10,
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\const u.png',
                         width=15*cm, height=15*cm, kind='proportional'),
     # fml(f'$u_{{C_\u0020 уст}} = {cnst.u_c[-1]:.3f}$ В'),
     fml(f'$u_{{C_\u0020 уст}} = {cnst.u_c[-1]:.0f}$ В'),
     sp_20,
     fml(f'$u_{{C_\u0020 max}} = {max(cnst.u_c):.3f}$ В'),

     # p_b,
     # grf(f1),
     # sp_50,
     # Image(drw1),
     # Paragraph('Установившиеся значения тока и напряжения:', style=st_5_10),


     # Paragraph('Максимальные значения тока и напряжения:', style=st_20_20),

     KeepTogether([
          Paragraph('Результат расчета при переменной ЭДС', style=st_20_20),
          fml('$e(t) = sin \\left(\\omega t \\right)$'),
          sp_20,
          Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\sin i.png',
                         width=15*cm, height=15*cm, kind='proportional'),
         fml(f'$i_{{L_\u0020 max}} = {max(sin.i1) * 10**3:.2f}$ мА'),
         sp_20,
         fml(f'$i_{{L_\u0020 уст}} = {0.3}$ мА'),
         sp_10,]),


     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\sin u.png',
                         width=15*cm, height=15*cm, kind='proportional'),
     fml(f'$u_{{C_\u0020 max}} = {max(sin.u_c1):.1f}$ В'),
     sp_20,
     fml(f'$u_{{C_\u0020 уст}} = {1.1}$ В'),
     # p_b,
     # grf(f1),
     # Image(drw1),
     # '''
     # '''
     # Paragraph('Амплитудные значения установившихся тока и напряжения:', style=st_20_20),
     # Paragraph('Максимальные значения тока и напряжения:', style=st_20_20),

     KeepTogether(
          [Paragraph('Ручной расчет', style=st_b_10_2),
           Paragraph('Составим характеристическое уравнение вида:', style=st_0_20),
           fml(r'$p^2 + 2\delta + \beta^2 = 0$'),
           sp_20,
           fml(r'$z_{вх} = \dfrac {x_c R_2} {x_c + R_2} + \dfrac {x_L R_1} {x_L + R_1} = 0$')]),
     # Paragraph('Ручной расчет', style=st_b_10_2),
     sp_50,
     fml(r'$\dfrac {\dfrac{1} {pC} {R_2} } {\dfrac{1} {pC} + R_2} +'
         r' \dfrac {pL R_1} {pL + R_1} = 0$'),
     sp_50,
     fml(r'$\dfrac {\dfrac {R_2 \left(pL + R_1 \right)} {pC} } '
         r'{\left( \dfrac{1} {pC} + R_2 \right) \left(pL + R_1 \right)} + '
         r'\dfrac { pL R_1 \left( \dfrac {1} {pC} + R_2 \right)} '
         r'{\left(pL + R_1 \right) \left( \dfrac{1} {pC} + R_2 \right)} = 0$'),
     sp_50,
     fml(r'$R_2  \dfrac {L} {C} \dfrac {R_2 R_1} {pC} + \dfrac {L R_1} {C} + pL R_1 R_2 = 0$'),
     sp_30,
     fml(r'$p^2 L R_1 R_2 + p \left( \dfrac {R_2 L} {C} \dfrac {R_2 + R_1} {L R_1 R_2} \right) + '
         r'\dfrac {R_2 R_1} {pC} + \dfrac {L R_1} {C} = 0$'),
     sp_40,
     fml(r'$p^2 + p \left( \dfrac { \dfrac {L} {C} (R_2 + R_1)} {L R_1 R_2} \right) + '
         r'\dfrac {R_2 R_1} {C L R_1 R_2} = 0$'),
     sp_30,
     fml(r'$p^2 + p \dfrac {R_2 + R_1} {C R_1 R_2} + \dfrac {1} {CL} = 0$'),
     sp_30,
     fml(r'$\delta = \dfrac {R_2 + R_1} {2 C R_1 R_2}; \quad \beta = \sqrt{\dfrac{1} {CL}}$'),
     Paragraph('Подберем сопротивления R\u2081 R\u2082 для выполнения условия колебательного процесса', style=st_20_20),
     fml(rf'$\delta < \beta; \quad R_1 = {r1:.0e}$ Ом, $ R_2 = {r2:.0e}$ Ом'),
     sp_30,
     fml(rf'$\delta = \dfrac {{ {r2:.0e} + {r1:.0e} }} {{2 \cdot {c:.0e} \cdot {r1:.0e} \cdot {r2:.0e}}} =  {delta:.1f};' 
         rf'\quad \beta = \sqrt {{\dfrac {{1}} {{ {c:.0e} \cdot {l} }} }} = {beta:.1f}$'),
     sp_30,
     fml(rf'$ \omega_0 = \sqrt {{ \delta^2 + \beta^2}}; \quad'
         rf'\omega_0 = \sqrt {{ {delta:.1f}^2 + {beta:.1f}^2}} = {omega0:.1f}$'),

     #       Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\Scan_20250309_164207.jpg',
     #       width=15*cm, height=30*cm, kind='proportional')]),  # из тетради
     # Paragraph('Ручной расчет', style=st_b_10_10),
     # fml(f'$z_{{вх}} = \\dfrac {{x_c R_2}} {{x_c + R_2}} + \\dfrac {{x_L R_1}} {{x_L + R_1}}$'),
     # sp_40,
     # fml(f'$z_{{вх}} = \\dfrac {{\\dfrac{{1}} {{pC}} {{R_2}} }} {{\\dfrac{{1}} {{pC}} + R_2}} + \\dfrac {{x_L R_1}} {{x_L + R_1}}$'),
     # Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\Scan_20250309_164254.jpg',
     #       width=15*cm, height=30*cm, kind='proportional'),
     # Paragraph('5.  а емкость - разрывом цепи. '),
     # Paragraph('При постоянной ЭДС индуктивность является закороткой, а емкость - разрывом цепи. '
     #           'Тогда:', style=st_5_5),
     # fml(f'$i_{{L_\u0020 вын}} = i_{{R_\u0020 2}} = \\dfrac {{e}} {{R_2}}; '
     #     f'\\quad i_{{L_\u0020 вын}} = \\dfrac {{{cnst.e}}} {{{cnst.r2}}} = {cnst.e / cnst.r2}$ А'),
     # sp_20,
     # fml(f'$u_{{C_\u0020 вын}} = e \\quad ;'
     #     f'u_{{c_\u0020 вын}} = {cnst.e}$ В'),

     Paragraph('При постоянной ЭДС E = 1 В индуктивность является закороткой, а емкость - разрывом.',
               style=st_20_20),
     fml(f'$I_{{уст}} = I_L = I_2 = \\dfrac{{E}} {{R_2}} = {0.01} $ А'),
     sp_20,
     fml(f'$U_{{уст}} = U_C = E = 1 $ В'),
     sp_25,
     fml(f'$U_{{пер}} = \\sqrt {{(u_{{вын}}(0) - u_0)^2 + Z^2(i_{{вын}}(0) - i_0)^2}}$'),
     sp_20,
     fml(f'$I_{{пер}} = \\sqrt {{(u_{{вын}}(0) - u_0)^2 / Z^2 + (i_{{вын}}(0) - i_0)^2}}$'),
     sp_20,
     fml(f'где $Z = \\sqrt{{ \\dfrac {{L}} {{C}} }} \\text{{ - характеристическое сопротивление контура}}; \\quad '
         f'Z = \\sqrt{{ \\dfrac {{ {l} }} {{ {c:.1e} }} }} = {z_c}$'),
     sp_30,
     fml(f'$U_{{пер}} = \\sqrt {{({abs(u_c_f[1]):.2f} - {u0})^2 + {z_c:.0f}^2 \\cdot ({abs(i_l_f[1]):.4f} - {i0})^2}} = {abs(u_p[1]):.2f}$ В'),
     sp_25,
     fml(f'$I_{{пер}} = \\sqrt {{({abs(u_c_f[1]):.2f} - {u0})^2 / {z_c:.0f}^2 + ({abs(i_l_f[1]):.4f} - {i0})^2}} = '
         f'{abs(i_f[1]*10**3):.2f}$ мА'),
     sp_25,
     fml(f'$\\tan \\phi_{{п}} = -z \\cdot \\dfrac {{i_{{вын}}(0) - i0}} {{u_{{вын}}(0) - u0}}; \\quad '
         f'\\tan \\phi_{{п}} = -{z_c} \\cdot \\dfrac {{ {cnst.i0} - {cnst.i0} }}'
         f' {{ {cnst.uc0} - {cnst.uc0} }} = \u221e $'),
     sp_30,
     fml(f'$t^u_{{max}} = \\dfrac{{ \\pi - \\phi_{{п}} }} {{\\omega_0}}; \\quad'
         f't^u_{{max}} = \\dfrac{{ \\pi - {polar(phi[1])[0]:.3f} \\pi}} {{{omega0:.1f}}}'
         f' = {abs(t_m_u[1] * 10**3):.2f}$ мс'),
     sp_30,
     fml(f'$t^i_{{max}} = \\dfrac{{ {{\\pi / 2}} - \\phi_{{п}} }} {{\\omega_0}}; \\quad'
         f't^i_{{max}} = \\dfrac{{ {{\\pi / 2}} - {polar(phi[1])[0]:.3f} \\pi}} {{{omega0:.1f}}}'
         f' = {abs(t_m_i[1] * 10**3):.2f}$ мс'),
     sp_30,
     fml(f'$K_{{уд}}^u = e^{{-\\delta t^u_{{max}} }} + 1; \\quad'
         f'K_{{уд}}^u = e^{{ {-delta:.2f} \\cdot {abs(t_m_u[1]):.5f} }} + 1 = {abs(k_s_u[1]):.1f}$'),
     sp_20,
     fml(f'$K_{{уд}}^i = e^{{-\\delta t^i_{{max}} }} + 1; \\quad'
         f'K_{{уд}}^i = e^{{ {-delta:.2f} \\cdot {abs(t_m_i[1]):.2f} }} + 1 = {abs(k_s_i[1]):.1f}$'),

     Paragraph('При переменной ЭДС', style=st_10_10),
     fml('$e(t) = sin \\left(\\omega t \\right)$'),
     sp_20,
          fml(f'$i_{{вын}} = \\dfrac {{e}} {{z}}$'),
     sp_30,
     fml(f'$z_{{экв}} = \\dfrac {{x_c R_2}} {{x_c + R_2}} + \\dfrac {{x_L R1}} {{x_L + R_1}}; '
         f'z_{{экв}} = {polar(z_f)[0]:.1f} \u2220 {degrees(polar(z_f)[1]):.1f} \u00b0$ Ом'),
     sp_30,
     fml(f'$i_{{вын}} = \\dfrac {{{e_a[0]}}} {{{z_f:.1f}}} '
         f'= {polar(i_f[0])[0] * 10**3:.2f} \u2220 {degrees(polar(i_f[0])[1]):.2f} \u00b0$ мА'),
     sp_30,
     fml(f'$i_{{L_\u0020 вын}} = i_{{вын}}  \\dfrac {{R_1}} {{x_l + R_1}}; \\quad '
         f'i_{{L_\u0020 вын}} = {polar(i_l_f[0]*10**3)[0]:.2f} \u2220 {degrees(polar(i_f[0])[1]):.1f} \u00b0$ мА'),
     sp_25,
     fml(f'$i_{{1_\u0020 вын}} = i_{{вын}} - i_{{L_\u0020 вын}}; \\quad '
         f'i_{{1_\u0020 вын}} = {polar(i_f[0])[0] * 10**3:.1f} \u2220 {degrees(polar(i_f[0])[1]):.1f} \u00b0 - '
         f'{polar(i_l_f[0]*10**3)[0]:.2f} \u2220 {degrees(polar(i_f[0])[1]):.1f} \u00b0 = '
         f'{polar(i1_f[0]*10**3)[0]:.2f} \u2220 {degrees(polar(i1_f[0])[1]):.1f} \u00b0$ мА'),
     sp_20,
     fml(f'$U_{{C_\u0020 вын}} = E - i_{{1_\u0020 вын}} R_1; \\quad'
         f'U_{{C_\u0020 вын}} = {polar(e_a[0])[0]:.2f} \u2220 {degrees(polar(e_a[0])[1]):.1f}\u00b0 - '
         f'{polar(i1_f[0]*10**3)[0]:.2f} \u2220 {degrees(polar(i1_f[0])[1]):.1f} \u00b0 \\cdot {r1} '
         f'= {polar(u_c_f[0])[0]:.2f} \u2220 {degrees(polar(u_c_f[0])[1]):.1f} \u00b0$ В'),
     sp_25,
     fml(f'$U_{{пер}} = \\sqrt {{({polar(u_c_f[0])[0]:.2f} - {u0})^2 + {z_c:.0f}^2 \\cdot ({abs(i_l_f[0]):.4f} - '
         f'{i0})^2}} = {polar(u_p[0])[0]:.1f}$ В'),
     sp_25,
     fml(f'$I_{{пер}} = \\sqrt {{({u_c_f[0]:.2f} - {u0})^2 / {z_c:.0f}^2 + ({i_l_f[0]:.4f} - {i0})^2}} = '
         f'{abs(i_f[0]*10**3):.2f}$ мА'),
     sp_25,
     # fml(f'$tan\\phi_{{п}} = -z\\dfrac{{(i_{{вын }}(0) - i0) }} {{ u_{{вын}}(0) - u0 }}; \\quad'
     #     f'tan\\phi_{{п}} = -{z_c}\\dfrac {{{p(i1_f[0]*10**3)[0]:.2f} \u2220 {p(i1_f[0])[1]:.1f} - {i0}) }} '
     #     f'{{{p(u_c_f[0])[0]:.3f}}} \u2220 {p(u_c_f[0])[1]:.1f} - {u0}}} = {abs(tg_phi_p[0]):.3f }$'),
     #     fml(f'$tan\\phi_{{п}} = -z\\dfrac{{i_{{вын }}(0) - i0 }} {{ u_{{вын}}(0) - u0 }} = '
     #         f'{tg_phi_p[0]}$'),
     fml(f'$\\tan \\phi_{{п}} = -z \\cdot \\dfrac {{i_{{вын}}(0) - i0 }} {{ u_{{вын}}(0) - u0 }}; \\quad '
         f'\\tan \\phi_{{п}} = -{z_c} \\cdot \\dfrac {{ {abs(round(i_f[0], 2)) } - {i0} }} '
         f'{{ {abs(round(u_c_f[0], 2))} - {u0} }} = {abs(tg_phi_p)[0]:.3f}$'),
     # sp_30,
     # fml(f'$\\phi_{{п}} = \\arctan {{i_{{вын }}(0) - i0 }} {{ u_{{вын}}(0) - u0 }}; \\quad $'),
     sp_30,
     fml(f'$t^u_{{max}} = \\dfrac{{ {{\\pi}} - \\phi_{{п}} }} {{\\omega_0}}; \\quad '
         f't^u_{{max}} = \\dfrac{{ {{\\pi}} - {polar(phi[0])[0]:.3f} \\pi}} '
         f'{{ {omega0:.1f} }} = {abs(t_m_u[0]*10**3):.2f}$ мс'),
     sp_40,
     fml(f'$t^i_{{max}} = \\dfrac {{ \\dfrac {{\\pi}} {{2}} - \\phi_{{п}} }} {{ \\omega_0 }}; \\quad'
         f't^i_{{max}} = \\dfrac {{ \\dfrac {{\\pi}} {{2}} - {polar(phi[0])[0]:.3f} \\pi }} {{ {omega0:.1f} }} = '
         f'{abs(t_m_i[0]*10**3):.2f}$ мс'),
     sp_30,
     fml(f'$K_{{уд}}^u = e^{{-\\delta t^u_{{max}}}} + 1; \\quad'
         f'K_{{уд}}^u = e^{{ {-delta:.1f} \\cdot {abs(t_m_u[0]):.5f} }} + {1} = {abs(k_s_u[0]):.3f}$'),
     sp_20,
     fml(f'$K_{{уд}}^i = e^{{-\\delta t^i_{{max}}}} + 1; \\quad'
         f'K_{{уд}}^i = e^{{ {-delta:.1f} \\cdot {abs(t_m_i[0]):.5f}}} + {1} = {abs(k_s_i[0]):.3f}$'),
     Paragraph('Вывод: в результате работы выполнено моделирование переходного процесса '
               'в заданной схеме электрической цепи. Результат моделирования проверен ручным счетом.', style=st_10_3),
     ]

doc.build(f, onLaterPages=addPageNumber)
