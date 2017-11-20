# graph creation
import networkx as nx, json
import matplotlib.pyplot as plt

print("poczatke wczytywania")
H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\max_sklad_spoj.gml')
print("koniec wczytywania")

nx.draw(H)
plt.show()