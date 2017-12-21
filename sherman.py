import numpy as np
from scipy.stats import norm
from params_by_sample_size import get_d, get_m
import  numpy.random as n_rand
from critical_points import sherman_critical_points, get_column_by_alpha


def sherman_w(sample):
    variation_series = np.sort(sample)
    n = len(variation_series)
    one_by_n = 1/(n+1)

    w = 0
    i = 0

    while i < len(sample):
        u_cur = variation_series[i]
        u_prev = 0
        if i != 0:
            u_prev = variation_series[i-1]

        w += 1/2 * np.abs(u_cur - u_prev - one_by_n)
        i = i + 1

    return w


# Normalized Sherman criteria
def sherman_w_normalized(sample):
    n = len(sample)
    m = get_m(n)
    d = get_d(n)

    return (sherman_w(sample) - m) / np.sqrt(d)


def sherman_w_normalized_p_val(w, m_carlo_count, sample_size):
    i = 0
    count = 0
    while i <= m_carlo_count:
        y = n_rand.sample(sample_size)
        w_cur = sherman_w_normalized(y)
        if w_cur > w:
            count = count + 1
        i = i + 1

    return count/len(sample_size)


def sherman_check_normalized(sample, alpha, m_carlo_count = 1000):
    w = sherman_w_normalized(sample)
    monte_carlo_p_val = sherman_w_normalized_p_val(w, m_carlo_count, len(sample))

    if len(sample) > 20:
        p_value = 1 - norm.cdf(w)
        return [w, p_value, p_value > alpha, monte_carlo_p_val, monte_carlo_p_val > alpha]

    else:
        row = len(sample) - 4
        column = get_column_by_alpha(alpha)
        critical_point = sherman_critical_points[row, column]
        return [w, None, w < critical_point, monte_carlo_p_val, monte_carlo_p_val > alpha]


# Modified Sherman criteria
def sherman_w_modified(sample):
    n = len(sample)
    u = (sherman_w(sample) - (0.3679 * (1 - (1 / (2 * n))))) / ((0.2431 / np.sqrt(n)) * (1 - (0.605 / n)))

    return u - (0.0955/np.sqrt(n)) * (u ** 2 - 1)


def sherman_w_modified_p_val(w, m_carlo_count, sample_size):
    i = 0
    count = 0
    while i <= m_carlo_count:
        y = n_rand.sample(sample_size)
        w_cur = sherman_w_modified(y)
        if w_cur > w:
            count = count + 1
        i = i + 1

    return  count/len(sample_size)


def sherman_check_modified(sample, alpha, m_carlo_count = 1000):
    w = sherman_w_modified(sample)
    monte_carlo_p_val = sherman_w_modified_p_val(w, m_carlo_count, len(sample))

    if len(sample) > 20:
        p_value = 1 - norm.cdf(w)
        return [w, p_value, p_value > alpha, monte_carlo_p_val, monte_carlo_p_val > alpha]

    else:
        row = len(sample) - 4
        column = get_column_by_alpha(alpha)
        critical_point = sherman_critical_points[row, column]
        return [w, None, w < critical_point, monte_carlo_p_val, monte_carlo_p_val > alpha]