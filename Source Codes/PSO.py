import matplotlib.pyplot as plt
import random
import time
import leach

def pso(pso_x, pso_y, pso_x1, pso_y1, num_of_anchors, num_of_dumb, r):


        print("PSO len(pso_x) is ",len(pso_x))
        print("PSO len(pso_x1) is ",len(pso_x1))

        a_pso_x = pso_x[:]
        a_pso_y = pso_y[:]

        dena1_pso_x = pso_x[:]
        dena1_pso_y = pso_y[:]

        c = 0
        f = plt.figure(c)
        a1 = plt.scatter(pso_x, pso_y, marker = '.', color = 'red')
        a2 = plt.scatter(pso_x1, pso_y1, marker = '.', color = 'cyan')
        plt.figlegend((a1,a2),('Anchor Nodes', 'Dumb Nodes'),'upper right')
        f.show()

        #plt.title('Localization')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.grid(True)
        plt.legend()
        plt.pause(0.05)
        f.show()

        actual_pso_x = []
        actual_pso_y = []

        predict_pso_x = []
        predict_pso_y = []
        num_of_pesudo = 0
        start_time = time.time()
        while(True):
                print('Iteration Number : ', c)
                print('No. of anchor nodes : ', num_of_anchors)
                print('No. of pesudo anchor nodes ', num_of_pesudo)
                print('No. of dumb nodes : ', len(pso_x1))


                #print('Anchor Nodes')
                #for i in range(len(x)):
                        #print(f'{i}. ({x[i]}, {y[i]})')

                #print('Dumb Nodes')
                #for i in range(len(x1)):
                        #print(f'{i}. ({x1[i]}, {y1[i]})')

                d = []

                for i in range(len(pso_x)):
                        temp = []
                        for j in range(len(pso_x1)):
                                temp.append(((
                            (pso_x[i] - pso_x1[j]) ** 2 + (pso_y[i] - pso_y1[j]) ** 2) ** 0.5)
                                + random.uniform(0,1) * (50/100) * (-1) ** random.randint(0,1))

                        d.append(temp)


                pseudo_anchor_nodes = []

                flag = 0
                while(True):
                        pso_x_dumb = random.randint(0, 100)
                        pso_y_dumb = random.randint(0, 100)

                        for i in range(len(pso_x1)):
                                s = 0


                                for j in range(len(pso_x)):
                                        s += (((pso_x_dumb - pso_x[j])**2 + (pso_y_dumb - pso_y[j])**2) ** 0.5 - d[j][i]) ** 2

                                s = (1/len(pso_x)) * s

                                if s <= 0.4:
                                        #print(s, x_dumb, y_dumb, x1[i], y1[i])

                                        dena1_pso_x.append(pso_x_dumb)
                                        dena1_pso_y.append(pso_y_dumb)

                                        pseudo_anchor_nodes.append(i)
                                        flag = 1
                                        break


                        if flag == 1:
                                break

                num_of_pesudo += len(pseudo_anchor_nodes)

                for i in pseudo_anchor_nodes:
                        r_pso_x = 0.01
                        r_pso_y = 0.01

                        estimated_pso_x = pso_x1[i] + r_pso_x
                        estimated_pso_y = pso_y1[i]+ r_pso_y

                        pso_x.append(estimated_pso_x)
                        pso_y.append(estimated_pso_y)

                        actual_pso_x.append(pso_x1[i])
                        actual_pso_y.append(pso_y1[i])

                        predict_pso_x.append(estimated_pso_x)
                        predict_pso_y.append(estimated_pso_y)

                temp_pso_x = []
                temp_pso_y = []

                for i in range(len(pso_x1)):
                        if i in pseudo_anchor_nodes:
                                continue

                        temp_pso_x.append(pso_x1[i])
                        temp_pso_y.append(pso_y1[i])

                pso_x1 = temp_pso_x
                pso_y1 = temp_pso_y

                c += 1

                if len(pso_x1) == 0:
                        break

                if num_of_dumb == 0:
                        break

                #f = plt.figure(c)
                #plt.scatter(x1, y1, label = "Dumb Nodes", color = 'blue')
                a3 = plt.scatter(pso_x[num_of_anchors:len(pso_x)+1], pso_y[num_of_anchors:len(pso_y)+1], marker = '.', color = 'green')
                #plt.scatter(a_x, a_y, color = 'red')
                #plt.xlabel('X axis')
                #plt.ylabel('Y axis')
                #plt.grid(True)
                #plt.legend()

                #f.show()
                print("------------------------------------------------------------------------------------")
                plt.pause(0.05)
        plt.figlegend((a1,a2,a3),('Anchor Nodes', 'Dumb Nodes','Pseudo-anchor Nodes'),'upper right')
        f.show()
        print('No. of iterations : ', c)


        #for i in range(len(actual_x)):
                #print(actual_x[i], "\t", predict_x[i])

        #print("------------------------------------------------------------------------------------")

        #for i in range(len(actual_y)):
                #print(actual_y[i], "\t", predict_y[i])

        error = 0
        for i in range(len(predict_pso_x)):
                error =  error + ((actual_pso_x[i] - predict_pso_x[i]) ** 2 + (actual_pso_y[i] - predict_pso_y[i]) ** 2) ** 0.5
        if len(predict_pso_x) != 0:
                error = error / len(predict_pso_x)
        end_time = time.time()

        print("------------------------------------------------------------------------------------")
        print('Error : ', error)
        
        my_time = (end_time - start_time) * 1000
        print('Time taken : ', my_time)

        plt.show()
        print("PSO ",len(dena1_pso_x))
        #leach.my_leach(dena1_pso_x,dena1_pso_y,len(dena1_pso_x))
        
        return dena1_pso_x,dena1_pso_y,len(dena1_pso_x), error, time
