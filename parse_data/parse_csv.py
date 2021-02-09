import csv


def read_print_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            print(line['email'])


def dict_write_csv(writefile, readfile):
    with open(readfile, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(writefile, 'w') as new_file:
            fieldnames = ['first_name', 'last_name']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            csv_writer.writeheader()

            for line in csv_reader:
                del line['email']
                csv_writer.writerow(line)


if __name__ == '__main__':
    read_print_csv('../data/names.csv')
    dict_write_csv('../data/dict_write_name.csv', '../data/names.csv')
