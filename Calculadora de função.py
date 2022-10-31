# Calculadora de equações
from math import sqrt, log, asin, acos, degrees

def p_grau():
    print('ax + b = c')
    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))
    rp = (c - b) / a
    print('x = {:.3f}'.format(rp))


def s_grau():
    print('ax² + bx + c = 0')
    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))
    delta = b ** 2 - (4 * a * c)
    if delta <= -1:
        rd = sqrt(abs(delta))/(2*a)
        rs = (-1 * b) / (2 * a)
        print('x = {:.3f} ± {:.3f}i'.format(rs, rd))
    else:
        rd = sqrt(delta)
        rs1 = (-1 * b + rd) / (2 * a)
        rs2 = (-1 * b - rd) / (2 * a)
        print('x¹ = {:.3f}, x² = {:.3f}'.format(rs1, rs2))


def logi():
    print('log a b = x')
    a = float(input('A = '))
    b = float(input('B = '))
    rl = log(b, a)
    print(('x = {:.3f}'.format(rl)))


def seno():
    print('a + b.senx = c')
    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))
    rs = (c - a) / b
    if 1 >= rs >= -1:
        rt = degrees(asin(rs))
        ime = (-1 * b) + a
        ima = b + a
        if ime < ima:
            print('x = {:.3f}°, Im = [{},{}]'.format(rt, ime, ima))
        else:
            print('x = {:.3f}°, Im = [{},{}]'.format(rt, ima, ime))
    else:
        print('\033[1;31mErro de matemática!\033[30m')


def coss():
    print('a + b.cosx = c')
    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))
    rc = (c - a) / b
    if 1 >= rc >= -1:
        rt = degrees(acos(rc))
        ime = (-1 * b) + a
        ima = b + a
        if ime < ima:
            print('x = {:.3f}°, Im = [{},{}]'.format(rt, ime, ima))
        else:
            print('x = {:.3f}°, Im = [{},{}]'.format(rt, ima, ime))
    else:
        print('\033[1;31mErro de matemática!\033[30m')


def per():
    print('\nQual equação deseja realizar:')
    print(' 1- 1° Grau \n 2- 2° Grau \n 3- Logaritmica \n 4- Seno \n 5- Cosseno')
    res = int(input('Qual? ').strip())
    if res == 1:
        p_grau()
    elif res == 2:
        s_grau()
    elif res == 3:
        logi()
    elif res == 4:
        seno()
    elif res == 5:
        coss()
    else:
        print('\033[1;31mOperação inválida! Insira novamente\033[30m')
        per()
    print('Deseja realiza outro calcúlo?')
    rr = input('[s]im ou [n]ão ')
    if rr != 's':
        print('Até mais!')
        exit()
    else:
        return per()


per()
