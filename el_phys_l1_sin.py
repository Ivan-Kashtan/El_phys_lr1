# Расчёт переходного процесса в RLC-контуре
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from numpy._core._multiarray_umath import sin
from scipy.integrate import solve_ivp

# from svglib.svglib import svg2rlg
# # from io import BytesIO
#
from in_dat import r1, r2, l, c, e
# from el_phys_l1_const import r1, r2, l, c, e


# Параметры схемы
# e = 1
# r1 = 1000
# r2 = 100
# l = 1
# c = 1E-6  # C = 20 * 10^(-6) Ф

# Функция с правыми частями системы уравнений
def fnc1(t, y):
    global e, r1, r2, l, c
    # Вводим обозначения неизвестных, вместо y0, y1
    uc = y[0]
    i = y[1]
    e_s = e*np.sin(2*np.pi*50*t)
    # Рассчитываем и возвращаем производные
    # duc = 1/C * (i + (E*np.sin(2*np.pi*50*t) - uc) / R1 - uc / R2)
    # di = (E - uc) / L
    duc = 1/c * (i + (e_s - uc) / r1 - uc / r2)
    di = (e_s - uc) / l
    return [duc, di]
'''
def fnc2(t, y):
    global e, r1, r2, l, c
    # Вводим обозначения неизвестных, вместо y0, y1
    uc = y[0]
    i = y[1]
    e_s = e*np.sin(2*np.pi*50*t + np.pi/2)
    # Рассчитываем и возвращаем производные
    # duc = 1/C * (i + (E*np.sin(2*np.pi*50*t) - uc) / R1 - uc / R2)
    # di = (E - uc) / L
    duc = 1/c * (i + (e_s - uc) / r1 - uc / r2)
    di = (e_s - uc) / l
    return [duc, di]
'''
# Задаем время решения
tmax = 0.1

# Задаем начальные условия
uc0 = 0
i0 = 0

# Вызываем решатель
slv1 = solve_ivp(fnc1, [0,tmax], [uc0,i0], method = 'BDF')
t1 = slv1.t
u_c1 = slv1.y[0, :]
i1 = slv1.y[1, :]
'''
slv2 = solve_ivp(fnc2, [0,tmax], [uc0,i0], method = 'BDF')
t2 = slv1.t
u_c2 = slv1.y[0, :]
i2 = slv1.y[1, :]
'''
# '''
# Строим графики решения
r'''
f_u1 = plt.figure(1)
plt.plot(t1, u_c1, 'k')
plt.title('Напряжение на емкости при $e = 1\\cdot sin\\omega t$')
plt.xlabel('$t$, с')
plt.ylabel('$u_c$, В')
ax_u = plt.gca()  # Создание экземпляра осей для возможности его редактирования
# ax.xaxis.set_major_locator(MultipleLocator(10))  # Основная цена деления оси Ox
ax_u.xaxis.set_minor_locator(MultipleLocator(0.005))  # Дополнительная цена деления оси Ox (t)
# ax.yaxis.set_major_locator(MultipleLocator(0.1))  # Основная цена деления оси Oy
ax_u.yaxis.set_minor_locator(MultipleLocator(0.1))  # Дополнительная цена деления оси Oy (t)
ax_u.grid()
# plt.savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\sin u.png', dpi=600)
plt.show()
'''

r'''
f_i1 = plt.figure(2)
plt.plot(t1, i1*10**3, 'k')
# plt.grid()
plt.title('Ток в индуктивности при $e = 1\\cdot sin\\omega t$')
plt.xlabel('$t$, с')
plt.ylabel('$i_L$, мА')
ax_i = plt.gca()  # Создание экземпляра осей для возможности его редактирования
# ax.xaxis.set_major_locator(MultipleLocator(10))  # Основная цена деления оси Ox
ax_i.xaxis.set_minor_locator(MultipleLocator(0.005))  # Дополнительная цена деления оси Ox (t)
# ax_i.yaxis.set_major_locator(MultipleLocator(100))  # Основная цена деления оси Oy
# ax_i.yaxis.set_minor_locator(MultipleLocator(1E-4))  # Дополнительная цена деления оси Oy (t)
ax_i.grid()
plt.savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\sin i.png', dpi=600)
'''
'''
f_u2 = plt.figure(1)
plt.plot(t2, u_c2)
plt.grid()
plt.title('Напряжение на емкости при $\\phi = \\dfrac {\\pi} {2}$')
plt.save()

f_i2 = plt.figure(2)
plt.plot(t2, i2)
plt.grid()
plt.title('Ток в индуктивности при $\\phi = \\dfrac {\\pi} {2}$')
plt.show()
'''
# '''
# '''

# imgdata = BytesIO()
# f1.savefig(imgdata, format='svg')
# imgdata.seek(0)  # rewind the data
# drw1=svg2rlg(imgdata)

# print(round(max(u_c), 2))
# print(round(max(i), 3))
