

# graph creation
import networkx as nx, json
import matplotlib.pyplot as plt

H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
print("koniec wczytywania")
print(H.has_node(0))
print(H.has_node("org.jboss.jbossas-jboss-as-parent-5.0.0.CR1"))

#skrypt rysowania działa tylko danych jest za dużo i nie wyrabia python
#nx.draw(H)
#print("koniec rysowania")
#plt.savefig("ppp.png")
#plt.show()


nx.number_attracting_components(H)
# is_attracting_component(H)