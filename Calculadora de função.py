# Calculadora de equações
from math import atan, sin, cos, radians, sqrt, log, asin, acos, degrees

def p_grau():
    print('ax + b = c')
    ain = input('A = ').replace(',','.')
    bin = input('B = ').replace(',','.')
    cin = input('C = ').replace(',','.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
        rp = (c - b) / a
        print('x = {:.3f}'.format(rp))
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m') 
        pass # types not compatible


def s_grau():
    print('ax² + bx + c = 0')
    ain = input('A = ').replace(',','.')
    bin = input('B = ').replace(',','.')
    cin = input('C = ').replace(',','.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
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
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m') 
        pass # types not compatible


def logi():
    print('log a b = x')
    ain = input('A = ').replace(',','.')
    bin = input('B = ').replace(',','.')
    try:
        a = float(ain)
        b = float(bin)
        rl = log(b, a)
        print(('x = {:.3f}'.format(rl)))
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m') 
        pass # types not compatible


def seno():
    print('a + b.senx = c')
    ain = input('A = ').replace(',','.')
    bin = input('B = ').replace(',','.')
    cin = input('C = ').replace(',','.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
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
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m') 
        pass # types not compatible


def coss():
    print('a + b.cosx = c')
    ain = input('A = ').replace(',','.')
    bin = input('B = ').replace(',','.')
    cin = input('C = ').replace(',','.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
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
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m') 
        pass # types not compatible


def ret():
    print('A⌊θ° -> a + bi')
    modin = input('A = ').replace(',','.')
    tetain = input('θ° = ').replace(',','.')
    try:
        mod = float(modin)
        teta = float(tetain)
        a = mod*cos(radians(teta))
        b = mod*sin(radians(teta))
        print(f'{mod:.2f}⌊{teta:.2f}° -> {a:.2f} + {b:.2f}i')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m') 
        pass # types not compatible
        

def pol():
    print('a + bi -> A⌊θ°')
    ain = input('a = ').replace(',','.')
    bin = input('b = ').replace(',','.')
    try:
        a = float(ain)
        b = float(bin)
        mod = sqrt((a**2) + (b**2))
        ang = degrees(atan(a/b))
        print(f'{a:.2f} + {b:.2f}i -> {mod:.2f}⌊{ang:.2f}°')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass # types not compatible


def per():
    print('\n\033[37mQual equação deseja realizar:')
    print(' 1 - 1° Grau \n 2 - 2° Grau \n 3 - Logaritmica \n 4 - Seno \n 5 - Cosseno \n 6 - Forma retângular \n 7 - Forma Polar \n 8 - Sair')
    option = input('Qual? ').strip()
    if option.isnumeric():
        res = int(option)
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
        elif res == 6:
            ret()
        elif res == 7:
            pol()
        elif res == 8:
            print('Até mais!')
            exit()
        else:
            print('\033[1;31mOperação inválida! Insira novamente\033[30m')
            per()
    else:
        print('\033[1;31mOperação inválida! Insira novamente\033[37m')
        per()
    print('\nDeseja realiza outro calcúlo?')
    rr = input('[s]im ou [n]ão ')
    while (rr != 's') & (rr != 'n'):
        print('\n\033[1;31mOperação inválida! Insira novamente\033[37m')
        rr = input('[s]im ou [n]ão ')
    if rr != 's':
        print('Até mais!')
        exit()
    else:
        return per()
per()
