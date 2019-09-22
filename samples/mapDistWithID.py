import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

# opening the vector map
shp_path = "D:\\MEGA\\Core CS\\Projects\\TNWaterMap\\resources\\tamilnadu_district.shp"

# reading the shape file by using reader function of the shape lib
sf = shp.Reader(shp_path)

# print(len(sf.shapes()))
# print(sf.records())
# print(sf.records()[1][5])

# reading the shapefile
def read_shapefile(sf):
    #fetching the headings from the shape file
    fields = [x[0] for x in sf.fields][1:]
#fetching the records from the shape file
    records = [list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]
#converting shapefile data into pandas dataframe
    df = pd.DataFrame(columns=fields, data=records)
#assigning the coordinates
    df = df.assign(coords=shps)
    return df

df = read_shapefile(sf)


# read operations
# df = read_shapefile(sf)
# print(df.shape)
# print(df.sample(5))

def plot_shape(id, s=None):
    plt.figure()
    #plotting the graphical axes where map ploting will be done
    ax = plt.axes()
    ax.set_aspect('equal')
#storing the id number to be worked upon
    shape_ex = sf.shape(id)
#NP.ZERO initializes an array of rows and column with 0 in place of each elements
    #an array will be generated where number of rows will be(len(shape_ex,point))and number of columns will be 1 and stored into the variable
    x_lon = np.zeros((len(shape_ex.points),1))
#an array will be generated where number of rows will be(len(shape_ex,point))and number of columns will be 1 and stored into the variable
    y_lat = np.zeros((len(shape_ex.points),1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
#plotting using the derived coordinated stored in array created by numpy
    plt.plot(x_lon,y_lat)
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)
# use bbox (bounding box) to set plot limits
    plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
    return x0, y0


# plotting the map
def plot_map(sf, x_lim=None, y_lim=None, figsize=(11, 9)):
    plt.figure(figsize=figsize)
    id = 0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')

        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id = id + 1

    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)

# displaying the map
# plot_map(sf)
# plt.show()

# filling a district with color
def plot_map_fill(id, sf, x_lim=None,y_lim=None,figsize=(11, 9),color='r'):
    plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points), 1))
    y_lat = np.zeros((len(shape_ex.points), 1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    ax.fill(x_lon, y_lat, color)

    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)


# plot_map_fill(0, sf, x_lim, y_lim, color=’y’)
# plot_map_fill(13, sf, color='y')
# plt.show()

# coloring districts by id
def plot_map_fill_multiples_ids(title, city, sf,x_lim=None,y_lim=None,figsize=(11, 9),color='r'):
    plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(title, fontsize=16)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    for id in city:
        shape_ex = sf.shape(id)
        x_lon = np.zeros((len(shape_ex.points), 1))
        y_lat = np.zeros((len(shape_ex.points), 1))
        for ip in range(len(shape_ex.points)):
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        ax.fill(x_lon, y_lat, color)

        x0 = np.mean(x_lon)
        y0 = np.mean(y_lat)
        plt.text(x0, y0, id, fontsize=10)

    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)

# naming the id numbers of the cities to be coloured
# city_id = [0, 1, 2, 3, 4, 5, 6]
#plot_map_fill_multiples_ids('Multiple Shapes', city_id, sf, color='g')
# plt.show()


def plot_cities_2(sf, title, cities, color):
    df = read_shapefile(sf)
    city_id = []
    for i in cities:
        city_id.append(df[df.district == i]
                       .index.get_values()[0])
    plot_map_fill_multiples_ids(title, city_id, sf,
                                x_lim=None,
                                y_lim=None,
                                figsize=(11, 9),
                                color=color);
# cities = ['Madurai', 'Erode']
#plot_cities_2(sf, 'DIST', cities, 'c')
# plt.show()


def calc_color(data, color=None):
    if color == 1:
        color_sq = ['#dadaebFF', '#bcbddcF0', '#9e9ac8F0', '#807dbaF0', '#6a51a3F0', '#54278fF0'];
        colors = 'Purples';
    elif color == 2:
        color_sq = ['#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8', '#253494'];
        colors = 'YlGnBu';
    elif color == 3:
        color_sq = ['#f7f7f7', '#d9d9d9', '#bdbdbd', '#969696', '#636363', '#252525'];
        colors = 'Greys';
    elif color == 9:
        color_sq = ['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000'];

    else:
        color_sq = ['#ffffd4', '#fee391', '#fec44f', '#fe9929', '#d95f0e', '#993404'];
        colors = 'YlOrBr';
    new_data, bins = pd.qcut(data, 6, retbins=True,
                             labels=list(range(6)))
    color_ton = []
    for val in new_data:
        color_ton.append(color_sq[val])
    if color != 9:
        colors = sns.color_palette(colors, n_colors=6)
        sns.palplot(colors, 0.6);
        for i in range(6):
            print("\n" + str(i + 1) + ': ' + str(int(bins[i])) +
                  " => " + str(int(bins[i + 1]) - 1))
        print("\n\n   1   2   3   4   5   6")
    return color_ton, bins;


def plot_cities_data(sf, title, cities, data=None, color=None, print_id=False):
    color_ton, bins = calc_color(data, color)
    df = read_shapefile(sf)
    city_id = cities
    # for i in cities:
    #     city_id.append(df[df.district == i].index.get_values()[0])
    plot_map_fill_multiples_ids_tone(sf, title, city_id,
                                     print_id,
                                     color_ton,
                                     bins,
                                     x_lim=None,
                                     y_lim=None,
                                     figsize=(11, 9));


def plot_map_fill_multiples_ids_tone(sf, title, city,
                                     print_id, color_ton,
                                     bins,
                                     x_lim=None,
                                     y_lim=None,
                                     figsize=(11, 9)):
    #plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    fig.suptitle(title, fontsize=16)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    for id in city:
        shape_ex = sf.shape(id)
        x_lon = np.zeros((len(shape_ex.points), 1))
        y_lat = np.zeros((len(shape_ex.points), 1))
        for ip in range(len(shape_ex.points)):
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        ax.fill(x_lon, y_lat, color_ton[city.index(id)])
        if print_id != False:
            x0 = np.mean(x_lon)
            y0 = np.mean(y_lat)
            plt.text(x0, y0, id, fontsize=10)
    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)


data_file_path = Path('D:\MEGA\Core CS\Projects\TNWaterMap\water_data\csv')
data_year = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
data_files = ['avwl_Jan', 'avwl_Feb', 'avwl_Mar', 'avwl_Apr', 'avwl_May', 'avwl_June', 'avwl_July', 'avwl_Aug', 'avwl_Sep',
               'avwl_Oct', 'avwl_Nov', 'avwl_Dec']
data_files_year = ['11', '12', '13', '14', '15', '16', '17', '18', '19']
images_path = Path('D:\MEGA\Core CS\Projects\TNWaterMap\water_data\img')


# data_file_path_year = data_file_path / data_year[0]
# penultimate_data_file_name = data_files[3] + data_files_year[0]
# the_data_file_name = penultimate_data_file_name + '.csv'
# final_data_file_name = os.path.join(data_file_path_year, the_data_file_name)
# print(final_data_file_name)
city_ids = []

districts_dict = {
    'Chennai': 18,
    'Thiruvallur': 4,
    'Kancheepuram': 20,
    'Thiruvannamalai': 10,
    'Vellore': 11,
    'Dharmapuri': 25,
    'Krishnagiri': 21,
    'Cuddalore': 16,
    'Villupuram': 12,
    'Thanjavur': 3,
    'Tiruvarur': 5,
    'Nagapattinam': 14,
    'Tiruchirappalli': 7,
    'Karur': 17,
    'Perambalur': 29,
    'Pudukkottai': 1,
    'Salem': 23,
    'Namakkal': 28,
    'Erode': 0,
    'Coimbatore': 15,
    'The Nilgiris': 30,
    'Dindigul': 19,
    'Madurai': 27,
    'Ramanathapuram': 22,
    'Sivagangai': 2,
    'Theni': 31,
    'Thoothukudi': 6,
    'Thirunelveli': 8,
    'Virudhunagar': 13,
    'Kanniyakumari': 26,
    'Tiruppur': 9
}

# Original Thiruppur new Tiruppur
# Old Trichy new Tiruchirappalli
# Old Thiruvarur new Tiruvarur
# Old Tirunelveli new Thirunelveli
# Old Nilgiris new The Nilgiris
# Old Kanyakumari new Kanniyakumari
# print(sorted([i for i in districts_dict.values()]))

for i in [11]:
    try:
        data_file_path_year = data_file_path / data_year[2]
        penultimate_data_file_name = data_files[i] + data_files_year[2]
        the_data_file_name = penultimate_data_file_name + '.csv'
        final_data_file_name = os.path.join(data_file_path_year, the_data_file_name)
        # print(final_data_file_name)
        if os.path.exists(final_data_file_name):
            if os.path.isfile(final_data_file_name):
                #print(final_data_file_name)

                data_f = pd.read_csv(final_data_file_name, delimiter=',',
                                     names=['sno', 'welltype', 'district', 'prev_year','cur_year'])

                # Checking if all districts in file is correct
                # names = [i for i in data_f.district]
                # for name in names:
                #     if name not in districts_dict.keys():
                #         print(name)

                data = [i for i in data_f.cur_year]
                data.pop(0)
                water_data = [float(i) for i in data]

                print_id = False # The shape id will be printed
                color_pallete = 3 # ‘Purple’

                try:
                    for j in data_f.district:
                        if j == 'Name of the District':
                            continue
                        elif j == 'Previous Year(January 2013)':
                            continue
                        elif j == 'Ariyalur':
                            continue
                        city_ids.append(districts_dict[j])
                except KeyError:
                    # print(KeyError.with_traceback())
                    continue

                plot_cities_data(sf, 'map', city_ids, water_data, color_pallete, print_id)
                final_images_path = images_path / data_year[2]
                image_name = penultimate_data_file_name + '.png'
                final_image_file_name = final_images_path / image_name
                # print(final_image_file_name)
                plt.savefig(final_image_file_name)
                plt.show()
            else:
                continue
    except TypeError:
        # print(TypeError.with_traceback())
        continue
    except ValueError:
        # print(ValueError.with_traceback())
        continue

# data_f = pd.read_csv(final_data_file_name, delimiter=',',
#                              names=['sno', 'welltype', 'district', 'prev_year','cur_year'])
# districts_dict = {
#     'Chennai': 18,
#     'Thiruvallur': 4,
#     'Kanchipuram': 20,
#     'Thiruvannamalai': 10,
#     'Vellore': 11,
#     'Dharmapuri': 25,
#     'Krishnagiri': 21,
#     'Cuddalore': 16,
#     'Villupuram': 12,
#     'Thanjavur': 3,
#     'Thiruvarur': 5,
#     'Nagapattinam': 14,
#     'Trichy': 7,
#     'Karur': 17,
#     'Perambalur': 29,
#     'Pudukkottai': 1,
#     'Salem': 23,
#     'Namakkal': 28,
#     'Erode': 0,
#     'Coimbatore': 15,
#     'Nilgiris': 30,
#     'Dindigul': 19,
#     'Madurai': 27,
#     'Ramanathapuram': 22,
#     'Sivagangai': 2,
#     'Theni': 31,
#     'Thoothukudi': 6,
#     'Tirunelveli': 8,
#     'Virudhunagar': 13,
#     'Kanyakumari': 26
# }
#
# city_ids = []
# for i in data_f.district:
#     if i == 'Name of the District':
#         continue
#     city_ids.append(districts_dict[i])
# print(city_ids)
#

