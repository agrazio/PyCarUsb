import os

FILE_EXT = ".mp3"

cwd = os.getcwd()
order = 0
norder = 0

mp3_files = [x for x in os.listdir() if x.endswith(FILE_EXT)]

# check for missing numbers (e.g. deleted files) and restore
mp3_files.sort()
for i, f in enumerate(mp3_files, start=1):
    if f[:3].isdigit():
        if int(f[:3]) != i:
            newf = '{:03}'.format(i)+f[3:]
            os.rename('{}\{}'.format(cwd, f), '{}\{}'.format(cwd, newf))
            f = newf
        order += 1
    else:
        norder += 1

new_counter = norder

# reload updated files names
mp3_files = [x for x in os.listdir() if x.endswith(FILE_EXT)]

# reverse to avoid already existing file when renaming
mp3_files.sort(reverse=True)

for f in mp3_files:
    if f[:3].isdigit():
        newf = f.replace(f[:3], '{:03}'.format(int(f[:3])+norder))
    else:
        newf = '{:03}'.format(new_counter)+'_'+f
        new_counter -= 1

    os.rename('{}\{}'.format(cwd, f), '{}\{}'.format(cwd, newf))
