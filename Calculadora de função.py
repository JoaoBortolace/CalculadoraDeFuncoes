# Calculadora de equações
from math import atan, sin, cos, radians, sqrt, log, asin, acos, degrees


def p_grau():
    print('ax + b = c')
    ain = input('A = ').replace(',', '.')
    bin = input('B = ').replace(',', '.')
    cin = input('C = ').replace(',', '.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
        rp = round((c - b) / a, 3)
        print(f'x = {rp}')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


def s_grau():
    print('ax² + bx + c = 0')
    ain = input('A = ').replace(',', '.')
    bin = input('B = ').replace(',', '.')
    cin = input('C = ').replace(',', '.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
        delta = b ** 2 - (4 * a * c)
        if delta <= -1:
            rd = round(sqrt(abs(delta))/(2*a), 3)
            rs = round((-1 * b) / (2 * a), 3)
            print(f'x = {rs} ± {rd}i')
        else:
            rd = sqrt(delta)
            rs1 = round((-1 * b + rd) / (2 * a), 3)
            rs2 = round((-1 * b - rd) / (2 * a), 3)
            print(f'x¹ = {rs1}, x² = {rs2}')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


def logi():
    print('log a b = x')
    ain = input('A = ').replace(',', '.')
    bin = input('B = ').replace(',', '.')
    try:
        a = float(ain)
        b = float(bin)
        rl = round(log(b, a), 3)
        print(f'x = {rl}')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


def seno():
    print('a + b.senx = c')
    ain = input('A = ').replace(',', '.')
    bin = input('B = ').replace(',', '.')
    cin = input('C = ').replace(',', '.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
        rs = (c - a) / b
        if 1 >= rs >= -1:
            rt = round(degrees(asin(rs)), 3)
            ime = round((-1 * b) + a, 3)
            ima = round(b + a, 3)
            if ime < ima:
                print(f'x = {rt}°, Im = [{ime},{ima}]')
            else:
                print(f'x = {rt}°, Im = [{ima},{ime}]')
        else:
            print('\033[1;31mErro de matemática!\033[30m')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


def coss():
    print('a + b.cosx = c')
    ain = input('A = ').replace(',', '.')
    bin = input('B = ').replace(',', '.')
    cin = input('C = ').replace(',', '.')
    try:
        a = float(ain)
        b = float(bin)
        c = float(cin)
        rc = (c - a) / b
        if 1 >= rc >= -1:
            rt = round(degrees(acos(rc)), 3)
            ime = round((-1 * b) + a, 3)
            ima = round(b + a, 3)
            if ime < ima:
                print(f'x = {rt}°, Im = [{ime},{ima}]')
            else:
                print(f'x = {rt}°, Im = [{ima},{ime}]')
        else:
            print('\033[1;31mErro de matemática!\033[37m')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


def ret():
    print('A⌊θ° -> a + bi')
    modin = input('A = ').replace(',', '.')
    tetain = input('θ° = ').replace(',', '.')
    try:
        mod = float(modin)
        teta = float(tetain)
        a = round(mod*cos(radians(teta)), 3)
        b = round(mod*sin(radians(teta)), 3)
        print(f'{mod}⌊{teta}° -> {a} + {b}i')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


def pol():
    print('a + bi -> A⌊θ°')
    ain = input('a = ').replace(',', '.')
    bin = input('b = ').replace(',', '.')
    try:
        a = float(ain)
        b = float(bin)
        mod = round(sqrt((a**2) + (b**2)), 3)
        ang = round(degrees(atan(b/a)), 3)
        print(f'{a} + {b}i -> {mod}⌊{ang}°')
    except (TypeError, ValueError, KeyError) as e:
        print('\033[1;31mDados inseridos de forma incorreta\033[37m')
        pass  # types not compatible


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
            print('\033[1;31mOperação inválida! Insira novamente\033[37m')
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
