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

def price_bonds(series:pd.DataFrame, bonds:pd.DataFrame):
    print(series.head())
    print(bonds.head())

    bonds['start'] = pd.to_datetime(bonds['start'])
    bonds['maturity'] = pd.to_datetime(bonds['maturity'])

    bonds['cashflow_dates'] = bonds.apply(
        lambda row: [row['start'].date() + datetime.timedelta(days=180 * x) for x in range((row['maturity'].year - row['start'].year) * 2)],
        axis=1
    )

    # print(bonds.head())

    # for i in range(1, len(bonds)):
    #     start = bonds.loc[i,'start']
    #     end = bonds.loc[i,'maturity']
    #     dates = [start.date() + datetime.timedelta(days= 180) for x in range(end.year - start.year)]
    #     print(dates)

if __name__ == "__main__":

    sofr_series = pd.read_csv("sofr_series.csv")

    sofr_series['settlement_date'] = pd.to_datetime(sofr_series['settlement_date'])

    series = discount_factors(sofr_series)

    bonds = pd.read_csv("bond.csv")

    price_bonds(series, bonds)

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