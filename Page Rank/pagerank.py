import networkx as nx
G = nx.DiGraph()
G.add_weighted_edges_from([(0,1,2.3),(0,2,2.1),(0,3,1.3),(1,0,1.3),(1,2,1.1),(2,0,1.1), (3,0,2.3)])
import matplotlib.pyplot as plt

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.savefig("shell.png")

from PIL import Image as im
im.open('shell.png').show()

for n, nbrs in G.adj.items():
    for nbr, eattr in nbrs.items():
        wt = eattr['weight']
        print(f"({n}, {nbr}, {wt:.3})")

print(list(G.successors(0)))
print(list(G.predecessors(2)))
print(G.edges(0))
a=list(G.predecessors(1))
print(a)
print(G[0][1]['weight'])
print("List of all nodes from which we can go to node 2 in a single step: ",list(G.predecessors(2)))

# Z values
z_lst={}
for i in range(0,4):
    sum=0
    a=list(G.successors(i))
    for j in a:
        values=str(G[i][j]['weight']).split(".")
        sum=sum+(int(values[0])*int(values[1]))
    z_lst[i]=sum
print(z_lst)

# L Values
l_lst={}
for i in range(0,4):
    sum=0
    a=list(G.successors(i))
    for j in a:
        values=str(G[i][j]['weight']).split(".")
        sum=(int(values[0])*int(values[1]))/z_lst[i]
        l_lst[str(i)+str(j)]=sum
print(l_lst)

d=0.5
for i in range(0,4):
    tr=""
    a=list(G.predecessors(i))
    #print(a)
    for j in a:
           tr=tr+str(j)+ "*"+str(l_lst[str(j)+str(i)])+"+"
    print("\nEquation for PR of",i," =",d,"+","1-",d,"(",tr,")")

# Iterative Approach
ans=[1,1,1,1]
abc=[]
while ans!=abc:
    for i in range(0,4):
        a=list(G.predecessors(i))
        su=0
        for j in a:
            su=su+(ans[i]*l_lst[str(j)+str(i)])
        ans[i]=d+((1-d)*su)
        abc=ans
        for h in range(0,len(ans)):
            ans[h]=round(ans[h],3)
    print(ans)
    print(abc)
    
pgrank={}
for i in range(0,len(ans)):
    s="file"+str(i)+".txt"
    pgrank[s]=ans[i]

pgrank["file5.txt"]=1.2
print(pgrank)



