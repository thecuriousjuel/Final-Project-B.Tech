import matplotlib.pyplot as plt
import random
import math

############################################################################################################
###########----------------------------------PARAMETERS------------------------------------------###########
############################################################################################################

def my_leach(x_o, y_o, n):

    print("N in leach is ",n)
    #Field Dimensions of WSN in
    xm = 100
    ym = 100

    p = 0.05 #probability of getting a node selcted as cluster head
    dead_nodes = 0  #Number of Dead Nodes in the beginning

    #coordinates for base station
    sinkx = 100
    sinky = 200

    Eo = 2 #Initial Energy of a Node (in Joules)

    #Energy required to run circuity (both for transmitter and receiver)
    Eelec = 50* math.pow(10,-9)  #units in Joules/bit
    ETx = 50*math.pow(10,-9) #units in Joules/bit
    ERx = 50*math.pow(10,-9) #units in Joules/bit

    Eamp = 100*math.pow(10,-12) #amount of energy spent by the amplifier to transmit the bits in Joules/bit/m^2

    #Data Aggregation Energy
    EDA = 5*math.pow(10,-9) #units in Joules/bit

    k = 4000 #size of data package in bits

    No = p*n #Number of Clusters
    rnd = 0 #Round of Operation

    #Current Number of operating Nodes
    operating_nodes = n
    transmissions = 0
    temp_val = 0
    flag1stdead = 0

    ############################################################################################################
    ###########-------------------------------END OFPARAMETERS---------------------------------------###########
    ############################################################################################################


    ############################################################################################################
    ###########----------------------CREATION OF WIRELESS SENSOR NETWORK-----------------------------###########
    ############################################################################################################

    SN = [[]] #Sensor Node
    CL = [[]] #Cluster head
    tr = []
    op = []
    nrg = []
    avg_node = []
    p_rounds = []
    p_transmissions = []

    for i in range(n*300):
        tr.append(0)
        op.append(0)
        nrg.append(0)
        avg_node.append(0)

    f1 = plt.figure(1)
    bs = plt.scatter(sinkx, sinky, marker = '*', color = "blue") #Plotting base station
    for i in range(1,n+1):
        id = i #sensor's ID number
        x = x_o[i-1]
        y = y_o[i-1]
        #x = random.randint(0,xm) #X-axis coordinates of sensor node
        #y = random.randint(0,ym) #Y-axis coordinates of sensor node
        E = Eo #nodes energy levels, initially set to be equal to "Eo"
        role = 0 #node acts as normal if the value is '0', if elected as a cluster head it  gets the value '1' (initially all nodes are normal)
        cluster = 0 #the cluster which a node belongs to
        cond = 1 #States the current condition of the node. when the node is operational its value is =1 and when dead =0
        rop = 0 #number of rounds node was operational
        rleft = 0 #rounds left for node to become available for Cluster Head election
        dtch = 0 #nodes distance from the cluster head of the cluster in which he belongs
        dts = 0 #nodes distance from the sink
        tel = 0 #states how many times the node was elected as a Cluster Head
        rn = 0 #round node got elected as cluster head
        chid = 0 #node ID of the cluster head which the "i" normal node belongs to
        SN.append([id, x, y, E, role, cluster, cond, rop, rleft, dtch, dts, tel, rn, chid])

        #Plotting
        an = plt.scatter(SN[i][1], SN[i][2], marker = '.', color = "green")
        plt.pause(0.05)

    plt.figlegend((bs,an),('Base Station','Alive Nodes'),'upper center')
    f1.show()

    ############################################################################################################
    ###########------------------------------END OF WSN CREATION-------------------------------------###########
    ############################################################################################################


    ############################################################################################################
    ###########----------------------------------SET UP PHASE----------------------------------------###########
    ############################################################################################################

    while operating_nodes > 0:
        t = (p/(1-p*(rnd % (1/p))))  #Threshold Value
        tleft = rnd % (1/p) #Re-election Value
        CLheads = 0 #Reseting Previous Amount Of Cluster Heads In the Network
        energy = 0 #Reseting Previous Amount Of Energy Consumed In the Network on the Previous Round

        #Cluster Heads Election
        for i in range(1,n+1):
            SN[i][5] = 0 #reseting cluster in which the node belongs to
            SN[i][4] = 0 #reseting node role
            SN[i][13] = 0 #reseting cluster head id
            if(SN[i][8] > 0):
                SN[i][8] -= 1
            if((SN[i][3] > 0) and (SN[i][8] == 0)):
                generate = random.random()
                if (generate < t):
                    SN[i][4] = 1 #assigns the node role of a cluster head
                    SN[i][12] = rnd #Assigns the round that the cluster head was elected to the data table
                    SN[i][11] += 1
                    SN[i][8] = 1/p - tleft #rounds for which the node will be unable to become a CH
                    SN[i][10] = math.sqrt(math.pow((sinkx - SN[i][1]),2) + math.pow((sinky - SN[i][2]),2)) #calculates the distance between the sink and the cluster head
                    CLheads += 1 #sum of cluster heads that have been elected
                    SN[i][5] = CLheads #cluster of which the node got elected to be cluster head
                    CLx = SN[i][1] #X-axis coordinates of elected cluster head
                    CLy = SN[i][2] #Y-axis coordinates of elected cluster head
                    CLi = i #Assigns the node ID of the newly elected cluster head to an array
                    CL.append([CLi, CLx, CLy])

        #CL=CL(1:CLheads) #Fixing the size of "CL" array

        #Grouping the Nodes into Clusters & caclulating the distance between node and cluster head
        for i in range(1,n+1):
            if (SN[i][4] == 0  and SN[i][3] > 0 and CLheads > 0):
                d = []
                for m in range(1,CLheads+1):
                    dist = math.sqrt(math.pow((CL[m][1]-SN[i][1]),2) + math.pow((CL[m][2]-SN[i][2]),2))
                    d.append(dist)
                    #we calculate the distance 'd' between the sensor node that is transmitting and the cluster head that is receiving with the following equation
                    #d=sqrt((x2-x1)^2 + (y2-y1)^2) where x2 and y2 the coordinates of the cluster head and x1 and y1 the coordinates of the transmitting node

                I = min(d) #finds the minimum distance of node to CH
                col = (d.index(I))+1 #getting Cluster Number in which this node belongs too
                SN[i][5] = col #assigns node to the cluster
                SN[i][9] = I #assigns the distance of node to CH
                SN[i][13] = CL[col][0]

        #Energy Dissipation for normal nodes
        for i in range(1,n+1):
            if (SN[i][6] == 1 and SN[i][4] == 0 and CLheads > 0):
                if (SN[i][3] > 0):
                    ETx = Eelec * k + Eamp * k * math.pow(SN[i][9],2)
                    SN[i][3] -= ETx
                    energy += ETx

                    #Dissipation for cluster head during reception
                    if (SN[SN[i][13]][3] > 0 and SN[SN[i][13]][6] == 1 and SN[SN[i][13]][4] == 1):
                        ERx = (Eelec+EDA) * k
                        energy = energy + ERx
                        SN[SN[i][13]][3] -= ERx
                        if (SN[SN[i][13]][3] <= 0): #if cluster heads energy depletes with reception
                            SN[SN[i][13]][6] = 0
                            SN[SN[i][13]][7] = rnd
                            dead_nodes += 1
                            operating_nodes -= 1
                            dn = plt.scatter(SN[i][1], SN[i][2], marker = '4', color = "red")
                            plt.pause(0.05)

                if (SN[i][3] <= 0): #if nodes energy depletes with transmission
                    dead_nodes += 1
                    operating_nodes -= 1
                    dn = plt.scatter(SN[i][1], SN[i][2], marker = '4', color = "red")
                    plt.pause(0.05)
                    SN[i][6] = 0
                    SN[i][13] = 0
                    SN[i][7] = rnd

        #Energy Dissipation for cluster head nodes
        for i in range(1, n+1):
            if(SN[i][6] == 1 and SN[i][4] == 1):
                if (SN[i][3] > 0):
                    ETx = (Eelec + EDA) * k + Eamp * k * math.pow(SN[i][10],2);
                    SN[i][3] -= ETx
                    energy += ETx

                if (SN[i][3] <= 0): #if cluster heads energy depletes with transmission
                    dead_nodes += 1
                    operating_nodes -= 1
                    dn = plt.scatter(SN[i][1], SN[i][2], marker = '4', color = "red")
                    plt.pause(0.05)
                    SN[i][6] = 0
                    SN[i][7] = rnd

        if (operating_nodes < n and temp_val == 0):
            temp_val = 1
            flag1stdead = rnd

        transmissions += 1
        if (CLheads == 0):
            transmissions -= 1
        if(transmissions not in p_transmissions):
            p_transmissions.append(transmissions)

        p_rounds.append(rnd)
        rnd += 1 #Next round

        tr[transmissions-1] = operating_nodes
        op[rnd-1] = operating_nodes

        if (energy > 0):
            nrg[transmissions-1] = energy

        #print("Operating Nodes in round ",rnd," = ",operating_nodes) #print operating nodes in every round
        #print("transmissions = ",transmissions)
        #print("rounds = ",rnd)

    plt.figlegend((bs,an,dn),('Base Station','Alive Nodes','Dead Nodes'),'upper center')
    f1.show()

    sum = 0
    for i in range(0,flag1stdead):
        sum += nrg[i]

    temp1 = sum/flag1stdead
    temp2 = temp1/n

    for i in range(0,flag1stdead):
        avg_node[i] = temp2


    ############################################################################################################
    ###########------------------------------END OF SET UP PHASE-------------------------------------###########
    ############################################################################################################


    ############################################################################################################
    ###########---------------------------PLOTTING SIMULATION RESULT---------------------------------###########
    ############################################################################################################

    #Plotting Operating Nodes per Round
    f2 = plt.figure(2)
    p_op = op[0:rnd] #list with number of operational nodes per round
    #print (p_op)
    plt.plot(p_rounds, p_op)
    plt.xlabel("Number of rounds")
    plt.ylabel("Operational Nodes")
    plt.title("Operating Nodes per Round")
    plt.suptitle("LEACH")
    f2.show()

    #Plotting Operating Nodes per transmissions
    f3 = plt.figure(3)
    p_tr = tr[0:transmissions] #list with number of operational nodes per transmission
    plt.plot(p_transmissions, p_tr)
    #print(p_tr[500],p_tr[750],p_tr[1000],p_tr[1250],p_tr[1500])
    plt.xlabel("Transmissions")
    plt.ylabel("Operational Nodes")
    plt.title("Operating Nodes per Transmission")
    plt.suptitle("LEACH")
    f3.show()

    #Plotting Energy Consumed per Transmission
    f4 = plt.figure(4)
    p_flag1stdead = range(1,flag1stdead+1)
    p_nrg = nrg[0:flag1stdead]
    plt.plot(p_flag1stdead, p_nrg)
    plt.xlabel("Transmissions")
    plt.ylabel("Energy in Joules")
    plt.title("Energy Consumed per Transmission")
    plt.suptitle("LEACH")
    f4.show()

    #Plotting Average Energy consumed by a Node per Transmission
    f5 = plt.figure(5)
    p_avg_node = avg_node[0:flag1stdead]
    plt.plot(p_flag1stdead, p_avg_node)
    plt.xlabel("Transmissions")
    plt.ylabel("Energy in Joules")
    plt.title("Average Energy consumed by a Node per Transmission")
    plt.suptitle("LEACH")
    f5.show()

    plt.show()
    return p_transmissions, p_tr