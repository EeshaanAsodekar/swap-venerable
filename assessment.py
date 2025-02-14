import pandas as pd
# treasury curve zero rates
tsy_curve = [('2/7/2025', 3.964513),
 ('2/7/2026', 4.209512),
 ('2/7/2027', 4.217946),
 ('2/7/2028', 4.236730),
 ('2/7/2029', 4.277885),
 ('2/7/2030', 4.298729),
 ('2/7/2031', 4.328451),
 ('2/7/2032', 4.367472),
 ('2/7/2033', 4.391345),
 ('2/7/2034', 4.432777),
 ('2/7/2035', 4.384383),
 ('2/7/2036', 4.342130),
 ('2/7/2037', 4.399693),
 ('2/7/2038', 4.492695),
 ('2/7/2039', 4.551263),
 ('2/7/2040', 4.633381),
 ('2/7/2041', 4.673640),
 ('2/7/2042', 4.717552),
 ('2/7/2043', 4.759463),
 ('2/7/2044', 4.784641),
 ('2/7/2045', 4.804596),
 ('2/7/2046', 4.806995),
 ('2/7/2047', 4.830164),
 ('2/7/2048', 4.843827),
 ('2/7/2049', 4.850165),
 ('2/7/2050', 4.790444),
 ('2/7/2051', 4.771485),
 ('2/7/2052', 4.763848),
 ('2/7/2053', 4.726552),
 ('2/7/2054', 4.673738),
 ('2/7/2055', 4.634572)]

# treasury bonds

tsy_bonds = [
    {'par': 100, 'coupon': 4.0, 'start': '8/15/2024', 'maturity': '8/15/2034', 'payment_frequency': 'semi-annual'},
    {'par': 100, 'coupon': 5.0, 'start': '8/15/2024', 'maturity': '8/15/2034', 'payment_frequency': 'semi-annual'},
    {'par': 100, 'coupon': 3.5, 'start': '8/15/2024', 'maturity': '8/15/2044', 'payment_frequency': 'semi-annual'},
    {'par': 100, 'coupon': 2.5, 'start': '8/15/2024', 'maturity': '8/15/2054', 'payment_frequency': 'semi-annual'},
]

# saving the treasureis
sofr_series = pd.DataFrame(tsy_curve, columns=['settlement_date', 'sofr_rate'])
print(sofr_series.head())
print(sofr_series.tail())
sofr_series.to_csv("sofr_series.csv")


# saving the bond infos
bonds = pd.DataFrame.from_dict(tsy_bonds)
print(bonds.head())
print(bonds.tail())
bonds.to_csv("bond.csv")