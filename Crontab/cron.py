import os

types = ['jpeg','png','csv','pdf','zip','rar','txt']

# pegando caminho raiz 
base_path = os.path.expanduser("~")
# caminho completo
path = os.path.join(base_path, "Downloads")

# caminho a ser executado
cmd = os.chdir(path)

full_list = os.listdir(cmd)

for type_ in types:
    if type_ not in os.listdir():
        os.mkdir(type_)


for file in full_list:
    for type_ in types:
        if ('.' + type_) in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type_, file)
            os.replace(old_path, new_path)