import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import random
import json
import time
from IPython import display
from matplotlib.collections import PatchCollection
import numpy as np

def plot():
    plt.figure(figsize=(18,12))
    # create the map
    map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

    # load the shapefile, use the name 'states'
    map.readshapefile('/Users/amitshetty/Downloads/basemap-1.1.0/examples/st99_d00', name='states', drawbounds=True)

    # collect the state names from the shapefile attributes so we can
    # look up the shape obect for a state by it's name
    state_names = []
    for shape_dict in map.states_info:
        state_names.append(shape_dict['NAME'])

    ax = plt.gca() # get current axes instance
    #print(state_names)
    # get Texas and draw the filled polygon
    #seg = map.states[state_names.index('Wisconsin')]
    #poly = Polygon(seg, facecolor='red',edgecolor='red')
    #ax.add_patch(poly)

    #seg = map.states[state_names.index('Minnesota')]
    #poly = Polygon(seg, facecolor='green',edgecolor='green')
    #ax.add_patch(poly)

    colors = ['red','green','blue','yellow']

    for state_name in sorted(set(state_names)):
        color_for_state = random.choice(colors)
        seg = map.states[state_names.index(state_name)]
        poly = Polygon(seg, facecolor=color_for_state,edgecolor=color_for_state)
        ax.add_patch(poly)
        display.display(plt.gcf())
        display.clear_output(wait=True)
        time.sleep(1)

def main():
    plot()

if __name__ == '__main__':
    main()