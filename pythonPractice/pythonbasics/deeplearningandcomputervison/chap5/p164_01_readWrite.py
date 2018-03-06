with open('/home/kevin/Desktop/pythonSource/name_age.txt', 'r') as fread, open(
        '/home/kevin/Desktop/pythonSource/age_name.txt', 'w') as fwrite:
    lines = fread.readlines()
    for line in lines:
        name, age = line.rstrip().split(',')
        fwrite.write('{},{}\n'.format(age, name))
