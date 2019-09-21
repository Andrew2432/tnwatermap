import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import csv

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

# opening the vector map
shp_path = "D:\\MEGA\\Core CS\\Projects\\TNWaterMap\\resources\\tamilnadu_district.shp"

# reading the shape file by using reader function of the shape lib
sf = shp.Reader(shp_path)

# print(len(sf.shapes()))
# print(sf.records())
# print(sf.records()[1][5])

# with open('tn_districts.csv', mode='w') as f:
#     f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for record in sf.records():
#         f.writerow(record)

# with open('tn_districts.csv', mode='r') as f:
#     f = csv.DictReader(f)
#     line_count = 0
#     for row in f:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["district"]}')
#         line_count += 1
#     print(f'Processed {line_count} lines.')


with open('tn_districts_dict.csv', mode = 'w') as f:
    fields = ['id', 'district']
    id = 0
    f = csv.DictWriter(f, fieldnames=fields)
    f.writeheader()
    with open('tn_districts.csv', mode='r') as g:
        g = csv.DictReader(g)
        for row in g:
            f.writerow({'id' : id, 'district' : row["district"]})
            id = id + 1


data_file = 'avwl_Aug19.csv'
districts_file = 'tn_districts_dict.csv'

