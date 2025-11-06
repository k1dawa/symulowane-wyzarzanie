from algorithm import annealing
from functions import ex3_f, ex3_domain, ex4_f, ex4_domain

def main():
    print("Wybierz funkcję:")
    print("1. f(x) = -2|x+100|+10 dla x∈(-105,-95) oraz -2.2|x-100|+11 dla x∈(95,105)")
    print("2. f(x) = x*sin(10πx) + 1  dla x∈[-1,2]")

    while True:
        choice = input("Wybór (1/2): ").strip()
        if choice in ("1", "2"):
            break
        print("Błędny wybór, spróbuj ponownie.")

    if choice == "1":
        eval_fn = ex3_f
        domain = ex3_domain()
        func_name = "Funkcja 1 (rozdział 3)"
    else:
        eval_fn = ex4_f
        domain = ex4_domain()
        func_name = "Funkcja 2 (rozdział 4)"

    print(f"\nWybrano: {func_name}")
    print("Podaj parametry algorytmu symulowanego wyżarzania:")

    #parametry użytkownika
    T0 = float(input("Temperatura początkowa T0: "))
    alpha = float(input("Współczynnik chłodzenia α: "))
    M = int(input("Liczba iteracji M: "))
    k = float(input("Współczynnik k: "))

    print("\nRozpoczynam działanie algorytmu...\n")

    result = annealing(
        eval_fn=eval_fn,
        domain=domain,
        T0=T0,
        alpha=alpha,
        M=M,
        k=k
    )

    print("=== WYNIKI ===")
    print(f"Funkcja: {func_name}")
    print(f"x_best = {result['x_best']:.9f}")
    print(f"f_best = {result['f_best']:.9f}")
    print(f"Akceptacji ogółem: {result['n_accept']}")
    print(f"W tym gorszych: {result['n_worse']}")
    print(f"Czas działania: {result['time_sec']:.4f} s")

if __name__ == "__main__":
    main()
