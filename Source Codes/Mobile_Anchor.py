import matplotlib.pyplot as plt
import random
import time


def mobile(x1, y1, r):
        x = []
        y = []

        x2 = []
        y2 = []


        temp_x = []
        temp_y = []

        temp = 20
        val = (40 ** 2 - 20 ** 2) ** 0.5

        x.append(0);
        y.append(val);

        for i in range(3):
                x.append(temp)
                temp += 40

                y.append(val)


        temp = 0
        for i in range(4):
                x2.append(temp)
                temp += 40
                y2.append(0)


        f_x = []
        f_y = []
        for i in range(4):
                f_x.append(x[i])
                f_x.append(x2[i])

                f_y.append(y[i])
                f_y.append(y2[i])

        #plt.plot(f_x,f_y)
        #plt.scatter(f_x,f_y)
        #plt.show()

        # correct till here

        temp_x.extend(f_x)
        temp_y.extend(f_y)

        for i in range(4):
                y[i] += 50
                y2[i] += 50

        f_x = []
        f_y = []

        for i in range(4):
                f_x.append(x[i])
                f_x.append(x2[i])

                f_y.append(y[i])
                f_y.append(y2[i])

        #plt.plot(f_x,f_y)
        #plt.scatter(f_x,f_y)
        #plt.show()

        # correct till here

        temp_x.extend(f_x)
        temp_y.extend(f_y)

        #plt.scatter(temp_x, temp_y)

        #plt.scatter(x,y)
        #plt.scatter(x1,y1)
        #plt.show()

        x = temp_x[:]
        y = temp_y[:]

        # plt.scatter(x, y)
        # plt.show()

        a_x = x[:]
        a_y = y[:]

        c = 0
        f = plt.figure(c)


        plt.plot(x[0:8],y[0:8])
        plt.plot(x[8:],y[8:])

        a1 = plt.scatter(x, y, marker = '.', color = 'red')
        a2 = plt.scatter(x1, y1, marker = '.', color = 'cyan')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.grid(True)
        plt.figlegend((a1,a2),('Anchor Nodes', 'Dumb Nodes'),'upper right')
        f.show()

        actual_x = []
        actual_y = []

        predict_x = []
        predict_y = []
        num_of_pesudo = 0
        start_time = time.time()
        while(True):
                print('Iteration Number : ', c)
                print('No. of anchor nodes : ', len(a_x))
                print('No. of pesudo anchor nodes ', num_of_pesudo)
                print('No. of dumb nodes : ', len(x1))


                d = []

                for i in range(len(x)):
                        temp = []
                        for j in range(len(x1)):
                                temp.append(((
                                        (x[i] - x1[j]) ** 2 + (y[i] - y1[j]) ** 2) ** 0.5)
                                            + random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1))

                        d.append(temp)


                pseudo_anchor_nodes = []
                for i in range(len(x1)):
                        count = 0
                        for j in range(len(x)):
                                if d[j][i] <= r:
                                        count += 1

                        if count >= 3:
                                pseudo_anchor_nodes.append(i)

                num_of_pesudo += len(pseudo_anchor_nodes)


                for i in pseudo_anchor_nodes:
                        r_x = random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1)
                        r_y = random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1)

                        estimated_x = x1[i] + r_x
                        estimated_y = y1[i]+ r_y

                        x.append(estimated_x)
                        y.append(estimated_y)

                        actual_x.append(x1[i])
                        actual_y.append(y1[i])

                        predict_x.append(estimated_x)
                        predict_y.append(estimated_y)

                temp_x = []
                temp_y = []

                for i in range(len(x1)):
                        if i in pseudo_anchor_nodes:
                                continue

                        temp_x.append(x1[i])
                        temp_y.append(y1[i])

                x1 = temp_x
                y1 = temp_y

                c += 1

                if len(pseudo_anchor_nodes) == 0:
                        break

                a3 = plt.scatter(x[len(a_x):len(x)+1], y[len(a_x):len(y)+1], marker = '.', color = 'green')
                print("------------------------------------------------------------------------------------")
                plt.pause(2)
        plt.figlegend((a1,a2,a3),('Anchor Nodes', 'Dumb Nodes','Pseudo-anchor Nodes'),'upper right')
        f.show()
        print('No. of iterations : ', c)

        error = 0
        for i in range(len(predict_x)):
                error =  error + ((actual_x[i] - predict_x[i]) ** 2 + (actual_y[i] - predict_y[i]) ** 2) ** 0.5
        if len(predict_x) != 0:
                error = error / len(predict_x)
        end_time = time.time()

        print("------------------------------------------------------------------------------------")
        print('Error : ', error)
        print('Time taken : ', (end_time - start_time) * 1000)

        plt.show()
