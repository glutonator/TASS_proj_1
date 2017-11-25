# graph creation
import networkx as nx, json
import matplotlib.pyplot as plt

print("poczatke wczytywania")
#H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
H = nx.read_gml('C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test.gml')
print("koniec wczytywania")

nx.write_pajek(H,'C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\plik_do_pajek.net')
#nx.write_gml(H, 'C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\max_sklad_spoj.gml')
print("koniec zapisywania")