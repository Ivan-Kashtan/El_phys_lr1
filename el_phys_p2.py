from numpy import array, round, empty, atan, pi, cos, sin, e, sqrt, inf
from cmath import rect, polar
# from math import pi, cos, sin, e, sqrt, inf
# from numpy._core._multiarray_umath import sqrt, cos, sin, e
from in_dat import *

# from cmath import rect, radians, polar

'''
def p_d(x: complex):
    if x.imag == 0:
        return x, 0
    else:
        x_m = abs(x)
        phi = atan(x.imag / x.real) * pi / 180
        # phi = atan(x.imag / x.real) * 180 / pi
        return x_m, phi

def p_r(x: complex):
    if x.imag == 0:
        return x, 0
    else:
        x_m = abs(x)
        phi = atan(x.imag / x.real)
        # phi = atan(x.imag / x.real) * 180 / pi
        return x_m, phi

def rect(x_m, phi):
    a = x_m * cos(phi)
    b = x_m * sin(phi)
    return a+1j*b
'''

# def forced(c, l, r1, r2, e):
#     omega = 2 * pi * 50
#     x_c = 1 / (1j * omega * c)
#     x_l = 1j * omega * l
#     e = rect(1, radians(0))
    # z = x_c * r2 / (x_c + r2) + x_l * r1 / (x_l + r1)
    # i = e / z
    # i_l = i * r1 / (x_l + r1)
    # i1 = i - i_l
    # u_c = e - i1 * r1
    # return u_c, i_l
    # return polar(i_l), polar(u_c)

# def periodic(c, l, r1, r2, e):
#     u_c = sqrt(forced(c, l, r1, r2, e)**2)

    # return
# E = (1, 1)
e_a = array([1+0j, 1])
# e_a = arra
i0 = 0
u0 = 0
beta = sqrt(1 / (c * l))
delta = (r2 + r1) / (2 * c * r1 * r2)
omega0 = sqrt(beta**2 - delta**2)

omega = 2 * pi * 50
x_c = 1 / (1j * omega * c)
x_l = 1j * omega * l

# forced
# z = 1000.108 + 1j*348.561
z_f = x_c * r2 / (x_c + r2) + x_l * r1 / (x_l + r1)
i_f = e_a / z_f
i_l_f = i_f * r1 / (x_l + r1)
i1_f = i_f - i_l_f
u_c_f = e_a - i1_f * r1

i_l_f[1] = 0.01
u_c_f[1] = 1

# i_l_f_m =
# i_l_phi = -1.98 * pi / 180
# i_l_f = rect(0.110882, -1.98 * pi / 180)
# u_c_f = rect(0.034834, -1.82 * pi / 180)
# periodic
z_c = sqrt(l / c)
# u_p = sqrt(u_c_f**2 + z_c**2 * i_l_f**2)
# u_p = sqrt(u_c_f**2 + i_l_f**2)

# i_l_f = sin( -1.98 * pi / 180)
# u_c_f = sin(-1.82 * pi / 180)

u_p = empty(2, dtype='complex')
i_p = empty(2, dtype='complex')

u_p[1] = sqrt((u_c_f[1] - u0)**2 + z_c**2*(i_l_f[1] - i0)**2)
i_p[1] = sqrt((u_c_f[1] - u0)**2/z_c**2 + (i_l_f[1] - i0)**2)

u_p[0] = sqrt((sin(polar((u_c_f[0] - pi/2))[1]) - polar(u0)[1])**2 + z_c**2*(sin(polar(i_l_f[0])[1] - polar(i0)[1]))**2)
i_p[0] = sqrt((u_c_f[0] - u0)**2/z_c**2 + (i_l_f[0] - i0)**2)

# u_p_const = sqrt(u_c_const**2 + z_c**2 * i_l_const**2)
# omega0 = 998.5
# z = 1000
tg_phi_p = empty(2, dtype='complex')

# tg_phi_p[1] = -z_c*((i0 - i0) / (u0 - u0))
tg_phi_p[1] = inf
tg_phi_p[0] = -z_c*((i_l_f[0] - i0) / (u_c_f[0] - u0))
# tg_phi_p = abs(-z * (i_l_f - i0) / (u_c_f - u0))
phi = atan(tg_phi_p)
t_m_u = (pi - phi) / omega0
t_m_i = (pi/2 - phi) / omega0
# delta = 54.5

k_s_u = e**(-delta*t_m_u) + 1
k_s_i = e**(-delta*t_m_i) + 1

# print(f'\u03b2 = {beta}')
# print(f'\u03b4 = {delta}')
# print(f'{z_c=}')
# print(f'{u_c_f=}')
# print(f'{u_p[0]=}')
# print(round(polar(atg), 5))
# print(polar(1+0j), 4)

# print(round(polar(tg_phi_p), 5))
