

# graph creation
import networkx as nx, json
import matplotlib.pyplot as plt

print("poczatke wczytywania")
#H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test.gml')
# print("dir")
# print(nx.is_directed(H))
print("koniec wczytywania")
# print(H.has_node(0))
# print(H.has_node("acegisecurity-acegi-security-0.5"))
# print(H.has_node("org.jboss.jbossas-jboss-as-parent-5.0.0.CR1"))

# print("test")
# print(nx.is_connected(H))
#lista polaczonych nodow
##################################
temp = list(sorted(nx.connected_component_subgraphs(H),key=len,reverse=True))
#nx.write_gml(temp[0], 'C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\max_sklad_spoj.gml')
print("max")
print(len(temp))
print("max_kon")
count =0
for i in temp:
    if(len(i)>1):
        count +=1
        print(len(i))
print("count")
print(count)
###############################
# #liczba nodow
# print("Nodes")
# print(temp[0].number_of_nodes())
# print(temp[1].number_of_nodes())
# print(temp[2].number_of_nodes())

# #liczba edges
# print("Edges")
# print(temp[0].size())
# print(temp[1].size())
# print(temp[2].size())


# nx.draw(temp[0])
# plt.savefig("wwww.png")
# plt.show()

#nx.draw(temp[1])
#plt.show()
#nx.draw(temp[2])
#plt.show()

#max z listy polaczonych nodow
#K =max(nx.connected_component_subgraphs(H), key=len)

# nx.draw(K)
# plt.savefig("qqqq.png")
# plt.show()

#temp = nx.connected_components(H)
#ttt =temp[0]
#skrypt rysowania dziala tylko danych jest za duzo i nie wyrabia python
#nx.draw(H)
print("koniec rysowania")
#plt.savefig("ppp.png")
#plt.show()


#nx.number_attracting_components(H)
# is_attracting_component(H)