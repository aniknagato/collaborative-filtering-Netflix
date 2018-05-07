import numpy as np
import collections

data = []
maxuid = 0
maxmovid  = 0

trainfile = open('train.txt', 'r')
for line in trainfile:
    # print (line)
    lin = []
    linp = line[0:len(line)-1].split(',')
    for a in linp:
        lin.append(float(a))
    if maxmovid < lin[0]:
        maxmovid = lin[0]
    if maxuid < lin[1]:
        maxuid = lin[1]

    data.append(lin)
    # print (lin)

trainfile.close()

print (data)

dd = {}
# maxmovid=6
for d1 in data:
    dd[int(d1[1])]= [0]*int(maxmovid+1)



# print (dd)

print ("*"*10)
for dp in data:

    getlist = dd[int(dp[1])]
    movid = int(dp[0])
    getlist[movid] = dp[2]
    dd[dp[1]] = getlist

# print (dd)

# filew = open('output.txt','w')

# for key in dd:
#     filew.write(str(key) + "-----" + str(dd[key]))
#
# filew.close()


print ("*"*100)
avrat = {}
subrat = {}
for key in dd:
    count = np.count_nonzero(dd[key])
    avrat[key] = sum(dd[key])/count

print (avrat)

for key in dd:
    subst=[]
    subst = np.subtract(dd[key],avrat[key])
    subrat[key] = subst.tolist()

# print (subrat)

# filew = open('outputsub.txt','w')
# for key in dd:
#     filew.write(str(key) + "-----" + str(subrat[key]))
#
# filew.close()


testfile = open('test.txt', 'r')

predictionfile = open('prediction.txt','w')
for line in testfile:
    # print (line)
    lin = []
    linp = line[0:len(line)-1].split(',')
    for a in linp:
        lin.append(float(a))
    userid = int(lin[1])
    movid = int(lin[0])
    weights = {}
    # Player = collections.namedtuple('Player', 'id coefficient')
    for key in dd:
        if key == userid:
            continue
        movlist = dd[key]
        if movlist[movid] == 0:
            continue

        coeff = np.corrcoef(subrat[key],subrat[userid])

        weights[key] = coeff[0][1]

    num_neighbour = 2

    print ("#"*100)

    print (weights)

    # sorted_weight = sorted([Player(v,k) for (k,v) in weights.items()], reverse=True)
    #
    # i = 0
    #
    # sumrating = 0
    # while i < num_neighbour:
    #     if i >= len(sorted_weight):
    #         break
    #     if i >= num_neighbour:
    #         break
    #     ratinglist = dd[Player[i].id]
    #     sumrating = sumrating + float(ratinglist[movid])
    #
    #     i += 1
    #
    i=0
    sumrating = 0

    for key in sorted(weights, key=weights.get, reverse = True):
        if i >= len(weights):
            break
        if i >= num_neighbour:
            break
        ratinglist = dd[key]
        sumrating = sumrating + float(ratinglist[movid])
        i += 1

        # print (str(key)+":" + str(pp[key]))


    predictrating = sumrating / float(i)
    predictionfile.write("'" + str(userid) + "-" + str(movid) + "' : " + str(predictrating) + "\n")









testfile.close()
predictionfile.close()









