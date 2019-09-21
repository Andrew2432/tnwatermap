import csv

data_file = 'avwl_Aug19.csv'

data_f = csv.DictReader(data_file)

output_file = 'temp.csv'

output_f = csv.DictWriter(output_file)

header = ['district', 'water_level']

correct_data = ['Kancheepuram', 'Tiruvannamalai', 'Vilupuram', 'Nagappattinam', 'Tiruchirappalli',
                'Tiruppur', 'The Nilgiris', 'Sivaganga', 'Thoothukkudi', 'Virudunagar', 'Kanniyakumari']

with open(data_file, 'r') as f:
