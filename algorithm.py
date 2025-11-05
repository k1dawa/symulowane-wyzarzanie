from typing import Callable, Dict, Tuple, Any
import math
import random
import time

#kryterium akceptacji
def acceptance(delta_f: float, T: float, k: float, rng: random.Random):
    if delta_f >= 0:
        return True
    if T <= 0 or k <= 0:
        return False
    p = math.exp(delta_f / (k * T))  
    return rng.random() < p


def reflect(x: float, lb: float, ub: float):
    #odbicie do [lb, ub]
    while x < lb or x > ub:
        if x < lb:
            x = lb + (lb - x)
        if x > ub:
            x = ub - (x - ub)
    return x


def neighbor(x: float, T: float, lb: float, ub: float, T0: float,
                rng: random.Random):

    width = ub - lb
    s = (T / T0) * width
    #minimalny krok
    s_min = 1e-12 * width
    if s < s_min:
        s = s_min
    x_new = x + rng.uniform(-s, s)
    return reflect(x_new, lb, ub)

def annealing(eval_fn: Callable[[float], float],
                        domain: Tuple[float, float],
                        T0: float, alpha: float, M: int, k: float,
                        L: int = 1) -> Dict[str, Any]:
    rng = random.Random()

    lb, ub = domain
    x = rng.uniform(lb, ub)
    f = eval_fn(x)
    x_best, f_best = x, f
    T = T0

    n_accept = 0
    n_worse = 0
    t0 = time.time()

    for step in range(1, M + 1):
        #sąsiad
        x_c = neighbor(x, T, lb, ub, T0, rng)
        f_c = eval_fn(x_c)
        delta = f_c - f 

        #akceptacja metropolis
        accept = acceptance(delta, T, k, rng)

        if accept:
            x, f = x_c, f_c
            n_accept += 1
            if delta < 0:
                n_worse += 1
            if f > f_best:
                x_best, f_best = x, f

        #chłodzenie (co krok lub po L próbach)
        if L <= 1:
            T *= alpha
        elif step % L == 0:
            T *= alpha
        if T < 1e-12:
            break

    return {
        "x_best": x_best,
        "f_best": f_best,
        "n_accept": n_accept,
        "n_worse": n_worse,
        "time_sec": time.time() - t0,
    }
