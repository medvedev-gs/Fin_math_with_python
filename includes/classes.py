import numpy as np
import includes.black_sholes_model as bs


class Option:

    def __init__(self, spot, strike, volatility, t, option_type: str) -> None:
        self.strike = strike
        self.t = t
        self.T = t / 365
        self.sigma = volatility / 100
        self.option_type = option_type
        self.prem = bs.premium(spot, strike, self.sigma, self.T, option_type)
        self.delta = bs.delta(spot, strike, self.sigma, self.T, option_type)
        self.gamma = bs.gamma(spot, strike, self.sigma, self.T)
        self.theta = bs.theta(spot, strike, self.sigma, self.T)
        self.vega = bs.vega(spot, strike, self.sigma, self.T)

    def profit_loss_profile(self, spot_range_):
        if self.option_type == 'Call':
            return np.where(
                (spot_range_ < self.strike),
                (0 - self.prem),
                (spot_range_ - self.strike - self.prem)
            )
        if self.option_type == 'Put':
            return np.where(
                (spot_range_ < self.strike),
                (self.strike - spot_range_ - self.prem),
                (0 - self.prem)
            )

    def __str__(self):
        return (
            f'Страйк: {self.strike}.\n'
            f'Дней до экспирации: {self.t}.\n'
            f'Тип опциона: {self.option_type}.\n'
            f'Премия опциона: {self.prem:.2f}.\n'
            f'Дельта опциона: {self.delta:.4f}.\n'
            f'Гамма опциона: {self.gamma:.8f}.\n'
            f'1 / Гамма опциона: {1/self.gamma:.2f}.\n'
            f'Тета опциона: {self.theta:.2f}.\n'
            f'Вега опциона: {self.vega:.2f}.\n'
        )


class Future:

    def __init__(self, spot) -> None:
        self.option_type = 'Fut'
        self.prem = spot
        self.delta = 1
        self.gamma = 0
        self.theta = 0
        self.vega = 0

    def profit_loss_profile(self, spot_range_):
        return (
            spot_range_ - self.prem
        )

    def __str__(self):
        return (
            f'Тип: {self.option_type}.\n'
            f'Цена открытия позиции: {self.prem:.2f}.\n'
            f'Дельта: {self.delta:.0f}.\n'
        )
