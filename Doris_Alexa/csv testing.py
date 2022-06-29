import csv
with open('carprobe.csv','rt') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\taltitude: {row[0]} direction: {row[1]} distance: {row[2]} speed:{row[82]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\taltitude: {row[0]} direction: {row[1]} distance: {row[2]} speed:{row[82]}')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')