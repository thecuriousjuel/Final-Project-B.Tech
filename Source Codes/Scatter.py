import matplotlib.pyplot as plt
import random
import time
import leach

def Trilateration(tri_x, tri_y, tri_x1, tri_y1, num_of_anchors, num_of_dumb, r):

    print("Trilateration len(tri_x) is ",len(tri_x))
    print("Trilateration len(tri_x1) is ",len(tri_x1))

    a_tri_x = tri_x[:]
    a_tri_y = tri_y[:]
    a3 = 0

    dena_tri_x = tri_x[:]
    dena_tri_y = tri_y[:]

    c = 0
    f = plt.figure(c)
    a1 = plt.scatter(tri_x, tri_y, marker = '.', color = 'red')
    a2 = plt.scatter(tri_x1, tri_y1, marker = '.', color = 'cyan')

    #plt.title('Localization')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.grid(True)
    plt.figlegend((a1,a2),('Anchor Nodes', 'Dumb Nodes'),'upper right')
    f.show()

    actual_tri_x = []
    actual_tri_y = []

    predict_tri_x = []
    predict_tri_y = []

    num_of_pesudo = 0
    start_time = time.time()

    while(True):
        print('Iteration Number : ', c)
        print('No. of anchor nodes : ', num_of_anchors)
        print('No. of pesudo anchor nodes ', num_of_pesudo)
        print('No. of dumb nodes : ', len(tri_x1))


        #print('Anchor Nodes')
        #for i in range(len(x)):
            #print(f'{i}. ({x[i]}, {y[i]})')

        #print('Dumb Nodes')
        #for i in range(len(x1)):
            #print(f'{i}. ({x1[i]}, {y1[i]})')

        d = []

        for i in range(len(tri_x)):
            temp = []
            for j in range(len(tri_x1)):
                temp.append(((
                    (tri_x[i] - tri_x1[j]) ** 2 + (tri_y[i] - tri_y1[j]) ** 2) ** 0.5)
                            + random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1))

            d.append(temp)


        #for i in range(len(x1)):
            #print(i, end='\t')
            #for j in range(len(x)):
                #print('{0:.2f}'.format(d[j][i]), end='\t')
            #print()


        pseudo_anchor_nodes = []
        for i in range(len(tri_x1)):
            count = 0
            for j in range(len(tri_x)):
                if d[j][i] <= r:
                    count += 1

            if count >= 3:
                dena_tri_x.append(tri_x1[i])
                dena_tri_y.append(tri_y1[i])

                pseudo_anchor_nodes.append(i)

        #print('No. of Pseudo Anchor Nodes : ', len(pseudo_anchor_nodes))
        num_of_pesudo += len(pseudo_anchor_nodes)
        #print('Pseudo Anchor Nodes ', pseudo_anchor_nodes)
        #for i in pseudo_anchor_nodes:
            #print(f'{i}. ({x1[i]}, {y1[i]})')


        for i in pseudo_anchor_nodes:
            r_tri_x = random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1)
            r_tri_y = random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1)

            estimated_tri_x = tri_x1[i] + r_tri_x
            estimated_tri_y = tri_y1[i]+ r_tri_y

            tri_x.append(estimated_tri_x)
            tri_y.append(estimated_tri_y)

            actual_tri_x.append(tri_x1[i])
            actual_tri_y.append(tri_y1[i])

            predict_tri_x.append(estimated_tri_x)
            predict_tri_y.append(estimated_tri_y)

        temp_tri_x = []
        temp_tri_y = []

        for i in range(len(tri_x1)):
            if i in pseudo_anchor_nodes:
                continue

            temp_tri_x.append(tri_x1[i])
            temp_tri_y.append(tri_y1[i])

        tri_x1 = temp_tri_x
        tri_y1 = temp_tri_y

        c += 1

        if len(pseudo_anchor_nodes) == 0:
            break

        a3 = plt.scatter(tri_x[num_of_anchors:len(tri_x)+1], tri_y[num_of_anchors:len(tri_y)+1], marker = '.', color = 'green')
        plt.pause(1)
        print("------------------------------------------------------------------------------------")
    plt.figlegend((a1,a2,a3),('Anchor Nodes', 'Dumb Nodes','Pseudo-anchor Nodes'),'upper right')
    f.show()
    print('No. of iterations : ', c)


    #for i in range(len(actual_x)):
        #print(actual_x[i], "\t", predict_x[i])

    #print("------------------------------------------------------------------------------------")

    #for i in range(len(actual_y)):
        #print(actual_y[i], "\t", predict_y[i])

    error = 0
    for i in range(len(predict_tri_x)):
        error =  error + ((actual_tri_x[i] - predict_tri_x[i]) ** 2 + (actual_tri_y[i] - predict_tri_y[i]) ** 2) ** 0.5
    if len(predict_tri_x) != 0:
        error = error / len(predict_tri_x)
    end_time = time.time()

    print("------------------------------------------------------------------------------------")
    print('Error : ', error)
    
    time_taken = (end_time - start_time) * 1000
    print('Time taken : ', time_taken)    

    plt.show()
    print("Trilateration ",len(dena_tri_x))
    #leach.my_leach(dena_tri_x,dena_tri_y,len(dena_tri_x))
    
    return dena_tri_x, dena_tri_y, len(dena_tri_x), error, time
