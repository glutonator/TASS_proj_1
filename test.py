
import networkx as nx, json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


print("SADsad")
print("sadasdas")

# np.random.seed(12345678)
# x = np.random.random(10)
# y = np.random.random(10)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# print("r-squared:", r_value**2)

# plt.plot(x, y, 'o', label='original data')
# plt.plot(x, intercept + slope*x, 'r', label='fitted line')
# plt.legend()
# plt.show()


x = [1,2,3,4]
y = [3,5,7,10] # 10, not 9, so the fit isn't perfect

print(np.log(x))
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
# fit_fn is now a function which takes in x and returns an estimate for y

plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
#plt.xlim(0, 5)
#plt.ylim(0, 12)

plt.show()