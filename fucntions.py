import pandas as pd
import datetime

def discount_factors(sofr_series:pd.DataFrame):

    print(sofr_series.head())
    print(sofr_series.columns)
    sofr_series['settlement_date'] = pd.to_datetime(sofr_series['settlement_date'])

    sofr_series['discount_factor'] = sofr_series.apply(
        lambda row: 1/(1+(row['sofr_rate']/100))**(row['settlement_date'].year - 2025),
        axis=1
    )

    return sofr_series

def get_pv(dicount_factor, cashflow):
    return dicount_factor*cashflow

def bond_pricer(sofr_series: pd.DataFrame, cashflow_dates: list, coupon: float):
    def get_closest_discount_factor(date):
        date = pd.Timestamp(date)  # Convert date to pd.Timestamp
        closest_date = sofr_series.iloc[(sofr_series['settlement_date'] - date).abs().argsort()[:1]]
        return closest_date['discount_factor'].values[0]

    bond_price = 0
    for i, date in enumerate(cashflow_dates):
        discount_factor = get_closest_discount_factor(date)
        if i == len(cashflow_dates) - 1:
            bond_price += get_pv(discount_factor, coupon + 100)  # Add 100 to the last payment
        else:
            bond_price += get_pv(discount_factor, coupon)

    return bond_price
def price_bonds(series:pd.DataFrame, bonds:pd.DataFrame):
    print(series.head())
    print(bonds.head())

    bonds['start'] = pd.to_datetime(bonds['start'])
    bonds['maturity'] = pd.to_datetime(bonds['maturity'])

    bonds['cashflow_dates'] = bonds.apply(
        lambda row: [row['start'].date() + datetime.timedelta(days=180 * x) for x in range((row['maturity'].year - row['start'].year) * 2)],
        axis=1
    )

    print(bonds.head())
    bonds['bond_price'] = bonds.apply(
        lambda row: bond_pricer(sofr_series, row['cashflow_dates'], row['coupon']),
        axis=1
    )

    print(bonds[['start', 'maturity', 'coupon', 'bond_price']])

    return bonds

if __name__ == "__main__":

    sofr_series = pd.read_csv("sofr_series.csv")

    sofr_series['settlement_date'] = pd.to_datetime(sofr_series['settlement_date'])

    series = discount_factors(sofr_series)

    bonds = pd.read_csv("bond.csv")

    priced = price_bonds(series, bonds)

    priced.to_csv("bonds_priced.csv")

    # print(sofr_series.head())
    # print(sofr_series['sofr_rate'])
    # bonds['start'] = pd.to_datetime(bonds['start'])
    # bonds['end'] = pd.to_datetime(bonds['maturity'])
    # dates = pd.read_excel("swap_cashflow_dates.xlsx")
    # soft_series = pd.read_excel("sofr_series.xlsx")
    # dates = bonds[['start','maturity']]
    # print(dates.head())
    # disc_factor = price_bonds(sofr_series, bonds)
    # disc_factor.get_days_between()
    # disc_factor.days_before_after_loader()
    # disc_factor.interporlate_sofrs()
    # final_discount_factors = disc_factor.get_discount_factors(1)
    # print(disc_factor.discount_factors)