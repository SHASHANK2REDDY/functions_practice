def generators():
    yield 12+16
    yield 2*2
    yield 25**2
    yield 16**(1/2)
check=generators()
for i in check:
    print(i)
