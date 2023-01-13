table_commands = []
table_name=None
with open('tablebases.txt', 'r') as f:
    for line in f:
        if line.startswith('CREATE TABLE'):
            parts = line.split()
            table_name = parts[2]
            #print(line)
        elif line.startswith('('):
                table_name = parts[2]
                column_str = line
                column_str = column_str.replace('(', '')
                column_str = column_str.replace(')', '')
                column_str = column_str.replace('`', '')
                column_str = column_str.replace(';', '')
                column_str = column_str.replace('\n', '')
                columns = column_str.split(',')
                print('DROP TABLE '+table_name+'; ', end='')
                #print('CREATE TABLE '+table_name+' (', end='')
                columns=columns[::-1]
                #print(','.join(columns), end='')
                #print(');')

                    
print('\n'.join(table_commands))
