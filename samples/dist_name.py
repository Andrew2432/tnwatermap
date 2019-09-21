import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

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

print(df)

df.to_csv('sample.csv')