import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

xl = pd.read_csv('./saham/EXCL.JK.csv', parse_dates = ['Date'])
xl4 = xl[(xl['Date'] > '2019-03-29') & (xl['Date'] < '2019-05-01')]

smart = pd.read_csv('./saham/FREN.JK.csv', parse_dates = ['Date'])
smart4 = smart[(smart['Date'] > '2019-03-29') & (smart['Date'] < '2019-05-01')]

indo = pd.read_csv('./saham/ISAT.JK.csv', parse_dates = ['Date'])
indo4 = indo[(indo['Date'] > '2019-03-29') & (indo['Date'] < '2019-05-01')]

tel = pd.read_csv('./saham/TLKM.JK.csv', parse_dates = ['Date'])
tel4 = tel[(xl['Date'] > '2019-03-29') & (tel['Date'] < '2019-05-01')]

plt.figure('Harga Historis Saham Provider Telco Indonesia (April 2019)', figsize = (12,8))
plt.plot(xl4['Date'], xl4['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(smart4['Date'], smart4['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(indo4['Date'], indo4['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(tel4['Date'], tel4['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')

plt.suptitle('Harga Historis Saham Provider Telco Indonesia (April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 45)

z = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(z, loc = 'upper center', bbox_to_anchor = (0.5, 1.05), ncol = 4, frameon = False)

plt.savefig('2.png')
plt.show()
