import json
import numpy as np
import cv2

class Distance:

    def fixjson(self, file, file2):
        with open(file, 'r') as fr, open(file2, 'w') as fw:
            contents = fr.read()
            fw.write(contents.replace("}", "}\n"))

    def getObj(self, jsonFile):
        o=[]
        objects = {}
        c=1
        #Getting the objects
        with open(jsonFile, 'r') as f:
            line = f.readline()
            while line:
                data = json.loads(line)
                o.append(data)
                line = f.readline()

        for i in o:
            v = []
            vec = np.array((i['xaxis'], i['yaxis']), dtype=np.float32)
            v.append(i['Category'])
            v.append(vec)
            k = "o"+str(c)
            objects[k] = v
            c+=1
        return objects



    def calculateDistance(self, dict):
        dDist={}
        for elt in dict.keys():
            d={}
            for j in dict.keys():
                if elt != j :
                    dist = np.linalg.norm(dict[elt][1] - dict[j][1])
                    d[j]=dist
            dDist[elt]=d

        return dDist

    def drawlines(self,img, dDict, oDict):
        lineThickness = 3
        for elt in oDict.keys():
            for j in oDict.keys():
                if elt != j:
                    cv2.line(img, (int(oDict[elt][1][0]), int(oDict[elt][1][1])), (int(oDict[j][1][0]), int(oDict[j][1][1])), (0, 255, 0), lineThickness)
                    x = int((oDict[elt][1][0] + oDict[j][1][0])/2)
                    y = int((oDict[elt][1][1] + oDict[j][1][1])/2)
                    cv2.putText(img, str(int(dDict[elt][j])), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
        return img

    def transformdict(self, oDict, hmatrix):
        hDict=oDict
        copy = oDict
        one = np.ones(1, dtype=np.float32)
        print(one)
        for elt in oDict.keys():
            copy[elt][1] = np.append(copy[elt][1], one)
            hDict[elt][1]=np.dot(hmatrix, copy[elt][1])
            hDict[elt][1] = np.delete(hDict[elt][1], 2)
        return hDict

