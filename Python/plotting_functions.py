import matplotlib.pyplot as plt

def plot_graph(coords, radius=10, connected=True, embedded=False, axis=None):
    if not embedded:
        fig, axis = plt.subplots()
    
    for i in range(coords.shape[0]):
        circle = plt.Circle((coords[i,0], coords[i,1]), radius, color='blue', fill=True)
        axis.add_patch(circle)
    
        if connected:
            for j in range(i + 1, coords.shape[0]):
                x_values = [coords[i,0], coords[j,0]]
                y_values = [coords[i,1], coords[j,1]]
                axis.plot(x_values, y_values, color='black', linestyle='-')
    
    if not embedded:
        axis.set_aspect('equal', 'box')
        axis.autoscale()
        plt.grid(True)
        plt.show()


def plot_directed_graph(coords, order, radius=10, embedded=False, axis=None):
    if not embedded:
        fig, axis = plt.subplots()
    
    for i in range(coords.shape[0]):
        if i == 0:
            circle = plt.Circle((coords[i,0], coords[i,1]), radius, color='red', fill=True)
        else:
            circle = plt.Circle((coords[i,0], coords[i,1]), radius, color='blue', fill=True)
        axis.add_patch(circle)
    
    for j in range(len(order)-1):
        x_values = [coords[order[j],0], coords[order[j+1],0]]
        y_values = [coords[order[j],1], coords[order[j+1],1]]
        axis.annotate("", xytext=(coords[order[j],0], coords[order[j],1]), xy=(coords[order[j+1],0], coords[order[j+1],1]), arrowprops=dict(arrowstyle="->"))
    
    if not embedded:
        axis.set_aspect('equal', 'box')
        axis.autoscale()
        plt.grid(True)
        plt.show()