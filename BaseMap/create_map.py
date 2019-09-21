from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(resolution='c', # c, l, i, h, f or None
            projection='merc',
            lat_0=54.5, lon_0=-4.36,
            llcrnrlon=7.9, llcrnrlat= 76.0, urcrnrlon=14.0, urcrnrlat=80.7)


map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()
