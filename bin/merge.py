
cache = {}

f1 = 'C:\\Users\\Mickael\\zbxora_out\\zbxora.gpsdata.zbx'
f2 = 'C:\\Users\Mickael\\zbxora_out\\zbxora.orcl.zbx'
f3= 'C:\\Users\Mickael\\zbxora_out\\zbxora.merged.zbx'

with open(f1, 'r') as file1:
    with open(f2, 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open(f3, 'w') as file_out:
    for line in same:
        file_out.write(line)
