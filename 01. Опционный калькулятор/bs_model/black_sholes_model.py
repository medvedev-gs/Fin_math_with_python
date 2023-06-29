import numpy as np
from scipy.stats import norm

def d1_calc(spot, strike, sigma, T):
    result = (np.log(spot/strike) + 0.5 * (sigma ** 2) * (T)) / (sigma * np.sqrt(T))
    return result
def n_d1_calc(d1):
    result = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (d1 ** 2))
    return result
def premium(spot, strike, sigma, T, option_type):
    d1 = d1_calc(spot, strike, sigma, T)
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'Call':
        N_d2 = norm.cdf(d2)
        delta_call = norm.cdf(d1)
        result = (spot * delta_call - strike * N_d2)
    if option_type == 'Put':
        N_minus_d2 = norm.cdf(-d2)
        delta_put = (norm.cdf(d1) - 1)
        result = (strike * N_minus_d2 + spot * delta_put)
    return result
def delta(spot, strike, sigma, T, option_type):
    d1 = d1_calc(spot, strike, sigma, T)
    delta_call = norm.cdf(d1)
    if option_type == 'Call':
        result = delta_call
    if option_type == 'Put':
        result = (delta_call - 1)
    return result
def gamma(spot, strike, sigma, T):
    d1 = d1_calc(spot, strike, sigma, T)
    n_d1 = n_d1_calc(d1)
    result = n_d1 / (sigma * spot * np.sqrt(T))
    return result
def theta(spot, strike, sigma, T):
    d1 = d1_calc(spot, strike, sigma, T)
    n_d1 = n_d1_calc(d1)
    result = (-spot * n_d1 * sigma / (2 * np.sqrt(T))) / 365
    return result
def vega(spot, strike, sigma, T):
    d1 = d1_calc(spot, strike, sigma, T)
    n_d1 = n_d1_calc(d1)
    result = spot * np.sqrt(T) * n_d1 / 100
    return result