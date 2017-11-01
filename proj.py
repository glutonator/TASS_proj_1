
import sys, traceback
# graph creation
import networkx as nx, json
from base64 import b64decode

data = []
G=nx.Graph()
with open('C:\\Users\Filip\\Documents\GitHub\\TASS_pliki\\mvn-deps-edit.csv', 'r') as file:
    count =1
    for line in file:
        # if count==341132:
        #     print(line)
        # try:   
        #     artifactId, groupId, version, deps = line.split('\t')
        # print(artifactId)
        # print(groupId)
        # print(version)
        # print(deps)
        if count <250:
            artifactId, groupId, version, deps = line.split('\t')
            #print(count)
            deps = json.loads(b64decode(deps))
            data+= [(artifactId, groupId, version, deps)]
        # if(count <5):
        #     print(data)
        # except:
        #     pass
        count+=1
print("Nowa czesc")

for ex in data:
    artifactId, groupId, version, deps = ex
    #print(ex)
    G.add_node("%s-%s-%s" % (artifactId, groupId, version))
    #print("Nowa czesc")
    for dep in deps:
        #print("w petli")
        
        #print(dep)
        #print(type(dep))
        if not '#' in dep: 
            # G.add_edge("%s-%s-%s" % (artifactId, groupId, version), dep.replace("\"", ""))
            G.add_edge("%s-%s-%s" % (artifactId, groupId, version),"%s-%s-%s" % (dep['artifactid'], dep['groupid']
            , dep['version']))
print(G.number_of_nodes())
print(G.number_of_edges())
#G.node.
#nx.draw(G)

nx.write_gml(G, 'C:\\Users\\Filip\Documents\\GitHub\\TASS_proj\\test_new.gml')
print(G.has_node("org.jboss.jbossas-jboss-as-parent-5.0.0.CR1"))


