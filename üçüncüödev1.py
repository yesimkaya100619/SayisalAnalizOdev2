import math
def f(x):
    return 4 * math.exp(-0.5 * x) - x


def f_prime(x):
    return -2 * math.exp(-0.5 * x)


def newton_raphson_method(ilk_tahmin, tol, max_yineleme):
    x0 = ilk_tahmin
    yineleme_sayımı = 0

    while yineleme_sayımı < max_yineleme:
        x0 = x0 - f(x0) / f_prime(x0)
        yineleme_sayımı += 1
        print(f" {yineleme_sayımı}.Iterasyon = {x0}")

    return x0


        # /////Başlangıç tahmini, tolerans ve maksimum iterasyon sayısı/////
initial_guess = 2.0
tolerance = 1e-5
max_iterations = 4

root = newton_raphson_method(initial_guess, tolerance, max_iterations)

print(f"\nSonuç => kök = {root}")
