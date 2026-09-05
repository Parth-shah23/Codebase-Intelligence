from pathlib import Path

path_obj= Path('C:/Parth/Codebase-Intelligence/repos/Web-eng-mini-project/Frontend/index.html') 
file = open(path_obj,'r')
content = file.read()
print(content)


#now this not just a normal path in string but we get acces to multible methods
# print(path_obj) displays the path text so you can read it, but under the hood,
#  path_obj allows your chunker to easily extract extensions (.suffix), get filenames (.name),
#  and open files cleanly without manual string slicing.