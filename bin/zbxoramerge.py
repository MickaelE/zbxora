import glob
cache = {}

f1 = 'C:\\Users\\Mickael\\zbxora_out\\*.zbx'
f3 = 'C:\\Users\\Mickael\\zbxora_out\\out.zbx'

filelist = glob.glob(f1)
for file_orig in filelist
    with open(file_orig, 'r') as file1:
        with open(f3, 'r') as file2:
            same = set(file1).intersection(file2)

        same.discard('\n')

    with open(f3, 'w') as file_out:
        for line in same:
            file_out.write(line)
