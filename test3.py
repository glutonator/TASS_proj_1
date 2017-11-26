import networkx as nx, json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import scipy as sc

print("poczatke wczytywania")
H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\max_sklad_spoj.gml')
#H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
print("koniec wczytywania")

#uuuu = list(nx.node_degree_xy(H))

average_degree_dict = dict(nx.average_degree_connectivity(H))

# xxx= list()
# yyy=list()


# for i in uuuu:
#     xxx.append(i[0])
#     yyy.append(i[1])

# fig=plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlabel('xlabel')
# ax.set_ylabel('ylabel')
# plt.plot(xxx,yyy,"ro",ms=1)

average_degree_xxx = list(average_degree_dict.keys())
average_degree_yyy=list(average_degree_dict.values())

fig6 = plt.figure()
ax = fig6.add_subplot(111)
ax.set_title('Assortativity Average')
ax.set_xlabel('node degree (k)')
ax.set_ylabel('average degree of nearest neighbors of nodes with degree k')

logA = np.log(average_degree_xxx)
logB = np.log(average_degree_yyy)
coefficients = np.polyfit(logA, logB, 1)
print("coefficients  ")
print(coefficients)
polynomial = np.poly1d(coefficients)
print("polynomial   ")
print(polynomial)

ys = polynomial(logA)
plt.plot(logA, logB, 'yo', logA, ys, '--k',ms=1)
plt.ylim([0,7])
plt.xlim([0,10])

plt.show()