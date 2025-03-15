# Расчёт переходного процесса в RLC-контуре
from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.pyplot import MultipleLocator
# from numpy._core._multiarray_umath import sin
# from svglib.svglib import svg2rlg

from in_dat import r1, r2, l, c, e

# Параметры схемы
# E = 1
# e = 1
# r1 = 1000
# r2 = 100
# l = 1
# c = 1E-6  # C = 20 * 10^(-6) Ф

# Функция с правыми частями системы уравнений
def fnc(t, y):
    global e, r1, r2, l, c
    # Вводим обозначения неизвестных, вместо y0, y1
    uc = y[0]
    i = y[1]

    # Рассчитываем и возвращаем производные
    # duc = 1/C * (i + (E*np.sin(2*np.pi*50*t) - uc) / R1 - uc / R2)
    # di = (E - uc) / L
    duc = 1/c * (i + (e - uc) / r1 - uc / r2)
    di = (e - uc) / l
    return [duc, di]

# Задаем время решения
tmax = 0.1

# Задаем начальные условия
uc0 = 0
i0 = 0

# Вызываем решатель
slv = solve_ivp(fnc, [0, tmax], [uc0, i0], method = 'BDF')

t = slv.t
u_c = slv.y[0, :]
i = slv.y[1, :]

r'''
# Строим графики решения
f1 = plt.figure(1)
plt.plot(t, u_c, 'k')
# plt.grid()
plt.title('Напряжение на емкости при $E = 1 В$')
plt.xlabel('$t$, с')
plt.ylabel('$u_C$, В')
ax_u = plt.gca()  # Создание экземпляра осей для возможности его редактирования
# ax.xaxis.set_major_locator(MultipleLocator(10))  # Основная цена деления оси Ox
ax_u.xaxis.set_minor_locator(MultipleLocator(0.005))  # Дополнительная цена деления оси Ox (t)
# ax_u.yaxis.set_major_locator(MultipleLocator(0.05))  # Основная цена деления оси Oy
ax_u.yaxis.set_minor_locator(MultipleLocator(0.05))  # Дополнительная цена деления оси Oy (t)
ax_u.grid()
# plt.show()
plt.savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\const u.png', dpi=600)
'''

r'''
f2 = plt.figure(2)
plt.plot(t, i * 10**3, 'k')
plt.xlabel('$t$, с')
plt.ylabel('$i_L$, мА')
plt.title('Ток в индуктивности при $E = 1 В$')
ax_i = plt.gca()  # Создание экземпляра осей для возможности его редактирования
# ax.xaxis.set_major_locator(MultipleLocator(10))  # Основная цена деления оси Ox
ax_i.xaxis.set_minor_locator(MultipleLocator(0.005))  # Дополнительная цена деления оси Ox (t)
# ax_i.yaxis.set_major_locator(MultipleLocator(0.05))  # Основная цена деления оси Oy
ax_i.yaxis.set_minor_locator(MultipleLocator(0.05))  # Дополнительная цена деления оси Oy (t)
ax_i.grid()
# plt.grid()
# plt.show()
plt.savefig(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР1\const i.png', dpi=600)
'''

'''
imgdata = BytesIO()
f1.savefig(imgdata, format='svg')
imgdata.seek(0)  # rewind the data
drw1=svg2rlg(imgdata)
'''

# print(round(max(u_c), 2))
# print(round(max(i), 3))
