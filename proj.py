
import sys, traceback
# graph creation
import networkx as nx, json
from base64 import b64decode

data = []
G=nx.Graph()
with open('C:\\Users\Filip\\Documents\GitHub\\TASS_pliki\\mvn-deps-edit.csv', 'r') as file:
    count =1
    for line in file:
        if count <250:
            artifactId, groupId, version, deps = line.split('\t')
            deps = json.loads(b64decode(deps))
            data+= [(artifactId, groupId, version, deps)]
        count+=1
print("Nowa czesc")

for ex in data:
    artifactId, groupId, version, deps = ex
    G.add_node("%s-%s-%s" % (artifactId, groupId, version))
    for dep in deps:
        if not '#' in dep: 
            G.add_edge("%s-%s-%s" % (artifactId, groupId, version),"%s-%s-%s" % (dep['artifactid'], dep['groupid']
            , dep['version']))
print(G.number_of_nodes())
print(G.number_of_edges())
#G.node.
#nx.draw(G)

nx.write_gml(G, 'C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
print(G.has_node("org.jboss.jbossas-jboss-as-parent-5.0.0.CR1"))


