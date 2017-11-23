# graph creation
import networkx as nx, json
import matplotlib.pyplot as plt
import numpy as np

print("poczatke wczytywania")
H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\max_sklad_spoj.gml')
#H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
print("koniec wczytywania")

#assortatywnośc 1
#temp = nx.degree_assortativity_coefficient(H)

#print("drugie")
#assortatywnośc peraosna w sumie to samo
#temp2 = nx.degree_pearson_correlation_coefficient(H)

#ppp = list(H.nodes())

#Generate node degree-degree pairs for edges in G.
uuuu = list(nx.node_degree_xy(H))

#avrage neighbor degree - to jest do tego pierwszego

xxx= list()
yyy=list()
# ttt=list(H.edges())
# for i in ttt:
#     xxx.append(i[0])
#     yyy.append(i[1])

for i in uuuu:
    xxx.append(i[0])
    yyy.append(i[1])

fig = plt
#fig = plt.figure()


plt.plot(xxx,yyy,"ro")
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

#ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

#data1, data2, data3, data4 = np.random.randn(4, 100)
#fig = plt.subplots(1, 1)
#ax = plt.subplots(1, 1)

#fig.show()
#ax.show()
plt.show()

#nx.draw(H)
#nx.
#plt.show()

#print(temp)
#print(temp2)

#nx.draw(temp)
#plt.show()
print("koniec")

