def pifagor_table(n):
    for x in range(1, n+1):
        for y in range(1, n+1):
            print(f'{x*y:3}', end=' ')
        print()

pifagor_table(5)
