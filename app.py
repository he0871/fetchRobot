from flask import Flask, abort, request
import MsgParse
import numpy as np

app = Flask(__name__)
scheck = np.array([0,0,0,0])#[start,goal,map,cost]
position = [[],[],[]]#[[size],[start],[goal]]
cost = []

def CompleteChec(scheck):
    #check if we get all the information we need
    x = 1
    for stu in scheck:
        x = x * stu
    if (x > 0):
        print("Let's rock")
        return True
    return False

@app.route('/api/paths/start', methods=['POST'])
def parse_start():
    data = request.data  # data is empty
    print("start position received :")
    #print(data)
    MsgParse.ProcPosition(position, 1, data)
    scheck[0] += 1
    print(scheck)
    #if(CompleteChec(scheck)):
    #   search
    return '201 Created' + str(data)

@app.route('/api/paths/goal', methods=['POST'])
def parse_goal():
    data = request.data  # data is empty
    #print("goal position received :")
    #print(data)
    MsgParse.ProcPosition(position, 2, data)
    scheck[1] += 1
    print(scheck)
    CompleteChec(scheck)
    return '201 Created' + str(data)

@app.route('/api/maps', methods=['POST'])
def parse_map():
    data = request.data  # data is empty
    print("map size received :")
    #print(data)
    MsgParse.ProcPosition(position, 0, data)
    scheck[2] += 1
    print(scheck)
    CompleteChec(scheck)
    return '201 Created' + str(data)

@app.route('/api/costs', methods=['POST'])
def parse_cost():
    data = request.data  # data is empty
    print("cost table received :")
    print(data)
    scheck[3] += 1
    cost = MsgParse.ProcCost(data)
    print("cost table is ")
    print(cost)
    print(scheck)
    CompleteChec(scheck)
    return '201 Created' + str(data)