import sys
import math

def load_result(filename):
    data = {}
    for line in open(filename):
        entry = line.rstrip().split(' ')
        nid = int(entry[0])
        label = int(entry[1])
        conf = float(entry[2])
        data[nid] = (label,conf)
    return data

def load_test(filename):
    data = {}
    for line in open(filename):
        nid,label= map(int,line.rstrip().split(' '))
        data[nid] = label
    return data


def match(result,test,n):
    correct = 0
    incorrect = 0
    c = 0
    i = 0
    while i < len(result) and c < n:
        nid = result[i][0]
        label = result[i][1][0]
        conf = result[i][1][1]
        if not nid in test:
            i += 1
            continue
        test_label = test[nid]
        if label == test_label:
            correct += 1
        else:
            incorrect += 1
        c += 1
        i += 1
    p = correct / float(correct + incorrect)
    r = (correct+incorrect) / float(len(test))
    print p,r

def load_points(filename):
    points = {}
    for line in open(filename):
        entry = line.rstrip().split(' ')
        pid = int(entry[0])
        lat = float(entry[1])
        lng = float(entry[2])
        points[pid] = (lat,lng)
    return points

resultfile = sys.argv[1]
testfile = sys.argv[2]

result = load_result(resultfile)
test = load_test(testfile)
sorted_results = sorted(result.items(), key=lambda x:x[1][1], reverse=True)

for i in range(20):
    desired_recall = 0.05 + i/20.0
    match(sorted_results, test, int(len(test)*desired_recall))
