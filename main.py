def main() -> None:
    print('A rombusz kerületét kiszámoló függvény!')
    a : float = float(input('a (oldal) = '))
    if a < 1:
        print('A megadott adattal nem lehet számolni!')
    else:
        rombusz_kerület: float = 4 * a
        print(f'A rombusz kerülete: {rombusz_kerület}')

    print('A rombusz területét kiszámoló függvény!')
    e : float = float(input('e (átló) = '))
    f : float = float(input('f (átló) = '))
    if e < 1 or f < 1:
        print('A megadott adatokkal nem lehet számolni!')
    else:
        rombusz_terület: float = (e + f) / 2
        print(f'A rombusz területe: {rombusz_terület}')
        

if __name__ == "__main__":
    main()