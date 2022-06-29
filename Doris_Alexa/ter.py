import csv
data = open('carTestData.csv',encoding='utf-8-sig')
csv_data = csv.reader(data)
data_lines = list(csv_data)
data_lines[1][3] = 0
writer = csv.writer(open('carTestData.csv','w',newline=''))
writer.writerows(data_lines)