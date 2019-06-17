import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

xl = pd.read_csv('./saham/EXCL.JK.csv', parse_dates = ['Date'])
smart = pd.read_csv('./saham/FREN.JK.csv', parse_dates = ['Date'])
indo = pd.read_csv('./saham/ISAT.JK.csv', parse_dates = ['Date'])
tel = pd.read_csv('./saham/TLKM.JK.csv', parse_dates = ['Date'])

plt.figure('Harga Historis Saham Provider Telco Indonesia', figsize = (12,8))
plt.plot(xl['Date'], xl['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(smart['Date'], smart['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(indo['Date'], indo['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(tel['Date'], tel['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')

plt.suptitle('Harga Historis Saham Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 45)

z = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(z, loc = 'upper center', bbox_to_anchor = (0.5, 1.05), ncol = 4, frameon = False)

plt.savefig('1.png')
plt.show()