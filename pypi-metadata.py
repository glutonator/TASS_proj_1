

# graph creation
import networkx as nx, json
from base64 import b64decode

data = []
G=nx.Graph()
with open('C:\\Users\Filip\\Documents\GitHub\\TASS_proj\\pypi-deps.csv', 'r') as file:
    for line in file:   
        name, version, deps = line.split('\t')
        deps = json.loads(b64decode(deps))
        data+= [(name, version, deps)]

for ex in data:
    name, version, deps = ex
    print(ex)
    G.add_node("%s-%s" % (name, version))
    for dep in deps:
        print(dep)
        print(type(dep))
        if not '#' in dep: G.add_edge("%s-%s" % (name, version), dep.replace("\"", ""))
print(G.number_of_nodes())
print(G.number_of_edges())
#G.node.
#nx.draw(G)
nx.write_gml(G, 'C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test.gml')


