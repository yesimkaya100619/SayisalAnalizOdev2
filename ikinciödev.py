def f(x):
    return x ** 3 - 2 * x ** 2 - 5


def bisection_method(a, b, tol, max_tekrar):
    if f(a) * f(b) > 0:
        print("Bu kapalı aralıkta  bir kök içermiyor.")
        return None

    yineleme_sayımı= 0

    while (b - a) / 2 > tol and yineleme_sayımı < max_tekrar:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

        yineleme_sayımı += 1

    return (a + b) / 2


         # [2, 4] kapalı aralığında kökü bulur:
a = 2
b = 4
hata_payi = 1e-5
max_yineleme = 4

kök = bisection_method(a, b, hata_payi, max_yineleme)

if kök is not None:
    print(f"Verilen kapalı aralıkta bulunan kök: {kök}")
else:
    print("Verilen kapalı aralıkta kök bulunamadı.")