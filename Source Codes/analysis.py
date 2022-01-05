import matplotlib.pyplot as plt


def myanalysis(t_x_p, t_y_p, p_x_p, p_y_p):
    
    f = plt.figure(1)
    plt.plot(t_x_p, t_y_p, color = 'red', label = "Trilateration")    
    plt.plot(p_x_p, p_y_p, color = 'blue', label = "PSO")
    
    plt.xlabel("Transmissions")
    plt.ylabel("Operational Nodes")
    
    plt.title("Operating Nodes per Transmission")
    plt.legend()
    
    #plt.figlegend((tr, pso), ('Trilateration', 'PSO'), 'upper right')
    f.show()