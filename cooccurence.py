import json
import numpy as np
import ast
import plotly 
plotly.tools.set_credentials_file(username='sarab1', api_key='Jr0mBnvRDYNtAeXjKU3q')


import plotly.plotly as py
import plotly.graph_objs as go

s=[]

#Getting the scenes
with open('places365/labels.json', 'r') as f:
    line = f.readline()
    while line:
        data = json.loads(line)
        s.append(data)
        line = f.readline()

o=[]
#Getting the objects
with open('darknet/labels1.json', 'r') as f:
    line = f.readline()
    while line:
        data = json.loads(line)
        o.append(data)
        line = f.readline()

scenes=[]
for i in s:
    x=ast.literal_eval(i['category'])
    scenes.append(x[0])
    
cols=set(scenes)
cols=list(cols)
cols

details=[]
for i in range(len(cols)):
    l=[]
    frames=[]
    c=0
    for j in s:
        
        y=ast.literal_eval(j['category'])
        if y[0]==cols[i] :
            id=j["id"]
            frames.append(id)
            c=c+1
    l.append(c)
    l.append(frames)
    details.append(l)

objects=[]

for i in o:
    objects.append(i['Category'])
    
rows=set(objects)
rows=list(rows)

co=np.zeros((len(rows),len(cols)))



for i in range(len(cols)):
    scene=cols[i]
    frames=details[i][1]
    for j in range(len(rows)):
        cpt=0
        for x in frames:
            for ob in o:
                if ob["Frame"]==x and ob["Category"]==rows[j]:
                    cpt=cpt+1
        co[j][i]=cpt

probc=co
'''for i in range(len(cols)):
    probc[:,i]=probc[:,i]/details[i][0]'''

probc=probc/len(o)

data=[]
for t in range(len(rows)):
    trace = go.Scatter(
    x = cols,
    y = probc[t],
    mode = 'lines',
    name = rows[t])
    data.append(trace)
    
py.iplot(data, filename='line-mode')


o1=[]
with open("darknet/soft.txt","r") as f:
    line = f.readline()
    while line:
        data = line.split("|")
        o1.append(data)
        line = f.readline()

rows1=[]
for n in o1:
    rows1.append(n[1])
print(len(rows1))
rows1=set(rows1)
rows1=list(rows1)

co1=np.zeros((len(rows1),len(cols)))

for i in range(len(cols)):
    scene=cols[i]
    frames=details[i][1]
    for j in range(len(rows1)):
        for x in frames:
            for ob in o1:
                if ob[0]==x and ob[1]==rows1[j]:
                    co1[j][i]=co1[j][i]+float(ob[2])
