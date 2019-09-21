import pandas as pd

data_file = 'avwl_Aug19.csv'
districts_file = 'tn_districts_dict.csv'
output_file = 'water_data.csv'

data_f = pd.read_csv(data_file, delimiter=',', names=['sno','welltype','district','prev_year',
                                                      'cur_year',
                                                      'rise','fall','remarks'])
districts_f = pd.read_csv(districts_file, delimiter=',', names=['id', 'district'])

df1 = data_f.set_index('sno', drop=False)
df2 = districts_f.set_index('district', drop=False)

output_dict = {}
print(districts_f.district)

districts = [i for i in districts_f.id]
print(districts)

# dict = {
#            'district_id' : 1,
#            'district_name': 1,
#             'prev_year' : 1,
#             'current_year' : 1
# }
for i in range(1, 32):
    print(data_f.loc[districts_f.id[2], data_f.district])