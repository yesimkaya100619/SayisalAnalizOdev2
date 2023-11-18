import math
def f(x):
    return x ** (1 / 3)


def f_prime(x):
    return (1 / 3) * x ** (-2 / 3)


def newton_raphson_method(ilk_tahmin, tol, max_yineleme):
    x0 = ilk_tahmin
    yineleme_sayımı = 0

    while yineleme_sayımı < max_yineleme:
        x0 = x0 - f(x0) / f_prime(x0)
        yineleme_sayımı += 1
        print(f" {yineleme_sayımı}.Iterasyon = {x0}")

    return x0


         # /////Başlangıç tahmini, tolerans ve maksimum iterasyon sayısı////
baslangıc_tahmini = 1.0
hata_payi = 1e-5
max_yineleme= 4

kök= newton_raphson_method(baslangıc_tahmini, hata_payi, max_yineleme)

print(f"\nSonuç => kök = {kök}")
