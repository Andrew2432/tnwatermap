import seaborn as sns
import csv

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


# with open('tn_districts_dict.csv', mode = 'w') as f:
#     fields = ['id', 'district']
#     id = 0
#     f = csv.DictWriter(f, fieldnames=fields)
#     f.writeheader()
#     with open('tn_districts.csv', mode='r') as g:
#         g = csv.DictReader(g)
#         for row in g:
#             f.writerow({'id' : id, 'district' : row["district"]})
#             id = id + 1


data_file = 'avwl_Aug19.csv'
districts_file = 'tn_districts_dict.csv'
output_file = 'water_data.csv'
fields=['district_id', 'district_name', 'prev_year', 'current_year']

with open(output_file, mode='w') as f:
    f = csv.DictWriter(f, fieldnames=fields)
    f.writeheader()
    with open(districts_file, mode='r') as g:
        g = csv.DictReader(g)
        with open(data_file, mode='r') as h:
            h = csv.DictReader(h)
            for districts_row in g:
                for data_row in h:
                    f.writerow({'district_id': districts_row["id"], 'district_name' : districts_row["district"],
                                'prev_year': data_row[""]})


