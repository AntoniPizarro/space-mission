import os
from shutil import rmtree

def get_file_content(file_path, encoding="utf-8"):
    '''
    Devuelve el contenido de un archivo
    '''
    res = open(file_path, "r", encoding=encoding).read()
    
    return res

def create_file(content, file_name, extension="txt", file_path="", mode="w", encoding="utf-8"):
    '''
    Crea un archivo con contenido
    '''
    if extension[0] != ".":
        extension = "." + extension
    
    final_file = os.path.join(file_path, file_name + extension)

    with open(final_file, mode, encoding=encoding) as f:
        f.write(content)
        f.close()

def create_empty_directory(dir_name, dir_path=""):
    '''
    Crea un directorio vacío
    '''
    if dir_path and dir_path[-1] != "/":
        dir_path += "/"

    final_path = dir_path + dir_name
    if not check_file_dir_exist(final_path):
        os.mkdir(final_path)

def remove_empty_directory(dir_name, dir_path=""):
    '''
    Elimina un directorio vacío
    '''
    if dir_path and dir_path[-1] != "/":
        dir_path += "/"

    final_path = dir_path + dir_name
    if check_file_dir_exist(final_path):
        os.rmdir(final_path)

def remove_directory(dir_name, dir_path=""):
    '''
    Elimina un directorio y todo su contenido
    '''
    if dir_path and dir_path[-1] != "/":
        dir_path += "/"

    final_path = dir_path + dir_name
    if check_file_dir_exist(final_path):
        rmtree(final_path)

def check_file_dir_exist(file_dir_path):
    '''
    Comprueba si existe un archivo o directorio
    '''
    return os.path.exists(file_dir_path)

def sort_treeview(tree, col, descending):
    '''
    Ordena las filas de un componente de tipo lista en función de una cierta columna.
    '''
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    data.sort(reverse=descending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)
    tree.heading(col, command=lambda: sort_treeview(tree, col, not descending))