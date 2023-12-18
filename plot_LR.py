# This code is the machine learning part for work { Nano Lett. 2023, 23, 16, 7733–7742 }
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import random
import csv


worksheet = xlrd.open_workbook("CuPdRuPt.xlsx")
sheet = worksheet.sheet_by_name("NH_hcp")
x = []
y = []
y_per_fu = []
for i in range(1, 11): # 10 data points, and eash data point includes 8 features (4 first neighboring + 4 second neighboring) and 1 label (adsorption energy)
    values = []
    row = sheet.row_values(i)
    for j in range(1, 9):
        values.append(row[j])
    x.append(values) # 8 features
    y.append(row[9]) # 1 label 
    # y_per_fu.append(row[23]/8)


model1 = linear_model.LinearRegression(fit_intercept=True)
model1.fit(x, y)
print(model1.score(x, y))
score = model1.score(x, y)
coef = model1.coef_
print(coef)
intercept = model1.intercept_
print(intercept)
predicted1 = model1.predict(x)


error1 = []
e1 = []
for i in range(len(y)):
    e1.append(y[i] - predicted1[i])
    error1.append(np.square(y[i] - predicted1[i]))
rmse1 = np.sqrt(sum(error1) / len(x))
# rmse_per_atom1 = rmse1/56
print(rmse1)


font2 = {'family': 'Arial',
# 'style':'italic',
'weight': 'normal',
'size': 20,
}
font1 = {'family': 'Arial',
# 'style':'italic',
'weight': 'normal',
'size': 20,
}


plt.scatter(y, predicted1, c="k")
plt.xlabel("DFT Prediction (eV)", font1)
plt.ylabel("Linear Regression Prediction (eV)", font1)
plt.text(min(y), max(predicted1)-0.1, "score = {}, RMSE = {} eV".format('%.3f' % score, '%.3f' % rmse1), font2)
plt.plot([min(y), max(y)], [min(y), max(y)], c="k")
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tick_params(labelsize=16)
#plt.title("NH Adsorption", font2)
# plt.savefig('NH adsorption at hcp LR.png', bbox_inches='tight', dpi=1500)
# plt.show()
# nn_list = []
from matplotlib.colors import ListedColormap, Normalize
from matplotlib.cm import get_cmap
cmap = get_cmap('YlOrRd')
norm = Normalize()
print(norm(error1))
print(cmap(np.array(1-norm(error1))))
clrs = cmap(np.array(1-norm(error1))/2+0.5)[:, 0:3]
# colors = LinearSegmentedColormap.from_list('blue', ['#0022ff', '#000055'], gamma=.2)
plt.scatter(y, predicted1, s=14**2, c=clrs, edgecolors='#888888', alpha=0.99, linewidths=1.5) # tune the color of the scatter point according to their error. 
plt.savefig('NH adsorption at hcp LR new.png', bbox_inches='tight', dpi=1500)
plt.show()
