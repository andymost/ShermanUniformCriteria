def get_d(n):
    d_l_top = 2 * (n ** (n + 2)) + n * (n - 1) ** (n + 2)
    d_l_bottom = (n + 2) * (n + 1) ** (n + 2)
    d_r = (n / (n + 1)) ** (2 * n + 2)
    d = d_l_top / d_l_bottom - d_r
    return d


def get_m(n):
    return  (n / (n + 1)) ** (n + 1)