import csv
import os

cwd = os.getcwd()
demo_file_path_csv = os.path.join(cwd, '../trainer_demo_files/demo_files/data.csv')

with open(demo_file_path_csv) as csv_file:
    read_csv = csv.reader(csv_file)
    for row in read_csv:
        print(row)
        for cell in row:
            pass



# new_file_path = os.path.join(cwd, '../trainer_demo_files/demo_files/')

#writerows allows for new dictionary instead of writerow which just takes a list (?)

# '''
# TSV FILES
# '''

# tsv_file_path = os.path.join(cwd, )

# csv = comma separated variable(s)
# tsv = comma separated variable(s)