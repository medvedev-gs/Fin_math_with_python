import numpy as np
from scipy.stats import norm


def d1_calc(spot, strike, sigma, T):
    return (
        (
            np.log(spot/strike)
            + (0.5 * sigma ** 2 * T)
        )
        / sigma
        / np.sqrt(T)
    )


def n_d1_calc(d1):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (d1 ** 2))


def premium(spot, strike, sigma, T, option_type):
    d1 = d1_calc(spot, strike, sigma, T)
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'Call':
        N_d2 = norm.cdf(d2)
        delta_call = norm.cdf(d1)
        return (spot * delta_call - strike * N_d2)
    if option_type == 'Put':
        N_minus_d2 = norm.cdf(-d2)
        delta_put = (norm.cdf(d1) - 1)
        return (strike * N_minus_d2 + spot * delta_put)


def delta(spot, strike, sigma, T, option_type):
    d1 = d1_calc(spot, strike, sigma, T)
    delta_call = norm.cdf(d1)
    if option_type == 'Call':
        return delta_call
    if option_type == 'Put':
        return (delta_call - 1)


def gamma(spot, strike, sigma, T):
    d1 = d1_calc(spot, strike, sigma, T)
    n_d1 = n_d1_calc(d1)
    return n_d1 / (sigma * spot * np.sqrt(T))


def theta(spot, strike, sigma, T):
    d1 = d1_calc(spot, strike, sigma, T)
    n_d1 = n_d1_calc(d1)
    return (-spot * n_d1 * sigma / (2 * np.sqrt(T))) / 365


def vega(spot, strike, sigma, T):
    d1 = d1_calc(spot, strike, sigma, T)
    n_d1 = n_d1_calc(d1)
    return spot * np.sqrt(T) * n_d1 / 100
