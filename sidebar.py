import os
import re

home = os.getcwd()
# path = os.path.join(home, r'textbook\dd.md')

def file_types(path):
    files = os.listdir(path)
    output = {}
    for f in files:
        split_names = f.split(".")
        if len(split_names) == 1: # this is a foler
            if output.get('folder'):
                output['folder'].append(f)
            else:
                output['folder'] = [f]
        else:
            extension = split_names[-1]
            if output.get(extension):
                output[extension].append(f)
            else:
                output[extension] = [f]
    return output

# get all the folders that should be updated from the main sidebar
path = os.path.join(home, '_sidebar.md')
with open(path, 'r') as f:
    content = f.read()
    p = re.compile('/(\w*?)/')
    foler_list = re.findall(p, content)

# update the sidebar within each sub foler
for i in foler_list:
    sub_path = os.path.join(home, i)
    with open(os.path.join(sub_path, "_sidebar.md"), 'w') as f:
        f.write('<!-- docs/_sidebar.md -->')
        f.write('\n\n')
        f.write('* [Home](/README.md)\n')
        for j in foler_list:
            f.write(f'* [{j}](/{j}/)\n')
            if i == j:
                md_files = file_types(sub_path)['md']
                for k in md_files:
                    name_only = k.split(".")[0]
                    if name_only in ["README", "_sidebar"]: # skip README.md
                        continue
                    modified_name = name_only.replace(" ", '%20')
                    f.write(f'\t* [{name_only}](/{i}/{modified_name}.md)\n')


