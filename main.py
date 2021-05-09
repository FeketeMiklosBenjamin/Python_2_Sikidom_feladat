def main() -> None:
    print('A rombusz kerületét kiszámoló függvény!')
    a : float = float(input('a (oldal) = '))
    if a < 1:
        print('A megadott adattal nem lehet számolni!')
    else:
        rombusz_kerület: float = 4 * a
        print(f'A rombusz kerülete: {rombusz_kerület}')
