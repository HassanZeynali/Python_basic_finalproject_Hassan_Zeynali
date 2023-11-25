import os
import datetime
import argparse
import sys
import shutil

def setup():
    parser = argparse.ArgumentParser(description="Python CLI Tool for File Manipulation")
    parser.add_argument("-path", type= str, help="Get path for command")
    parser.add_argument("-file", type= str, help="Get file for command")
    parser.add_argument("-dirc", type= str, help="Get directory for command")
    parser.add_argument("-sour", type= str, help="Get source for command")
    parser.add_argument("-dest", type= str, help="Get destination for command")
    parser.add_argument("-name", type= str, help="Get name of files or directories for find command")
    parser.add_argument("-typ", type= str, help="Get type of a file for command")
    parser.add_argument("-l","--ls", action="store_true", help="List directory contents at `path`, or the current directory if no path is given.")
    parser.add_argument("-cd","--cd", action="store_true", help="Change the working directory to path.")
    parser.add_argument("--mkdir", action="store_true", help="Create a new directory at path.")
    parser.add_argument("--rmdir", action="store_true", help="Remove the directory at path if it is empty.")
    parser.add_argument("--rm", action="store_true", help="Remove the file specified by file.")
    parser.add_argument("--rm-r", action="store_true", help="Remove the directory at directory and its contents recursively.")
    parser.add_argument("--cp", action="store_true", help="Copy a file or directory from source to destination.")
    parser.add_argument("--mv", action="store_true", help="Move a file or directory from source to destination.")
    parser.add_argument("--find-type","-t", action="store_true", help="Search for type of files matching pattern starting from path.")
    parser.add_argument("--find", action="store_true", help="Search for files or directories matching pattern starting from path.")
    parser.add_argument("--cat", action="store_true", help="Output the contents of the file.")
    parser.add_argument("--pwd", action="store_true", help="Display Current directory")
    return parser

def display_ls (path):
    for p, d, f in os.walk(path):
        for file in f:
            print(file , end = " ,")
        for direc in d:
            print (direc , end = " ,")

def display_cd (path):
    try:
        os.chdir(path)
        print ("Current directory now:" , os.getcwd())
    except OSError as e:
        print (e)

def display_mkdir (path):
    try:
        os.mkdir(path)
        print (f"Create a new directory at {path}")
    except OSError as e:
        print (e)

def display_rmdir (path):
    try:
        os.rmdir(path)
        print (f"Remove the directory at {path}")
    except OSError as e:
        print (e)

def display_rm (file):
    try:
        os.remove(file)
        print (f"Remove the file at {file}")
    except OSError as e:
        print (e)

def display_rm_r(dirc):
    try:
        shutil.rmtree(dirc)
        print (f"Remove the directory at {dirc}")
    except OSError as e:
        print (e)

#def display_cp(sour, dest):
#    name = os.path.basename(sour)
#    if name.find(".") == -1:
#       try:
#            dest = shutil.copytree(sour, dest)
#            print (f"Copy a directory from {sour} to {dest}")
#        except OSError as e:
#            print (e)
#    else:
#        try:
#            dest = shutil.copyfile(sour, dest)
#            print (f"Copy a file from {sour} to {dest}")
#        except OSError as e:
#            print (e)
def cp_file (sour, dest):
    with open (sour, "r") as f_read:
        data = f_read.read()
    with open (dest, "w") as f_write:
        f_write.write(data)
    print (f"Copy a file from {sour} to {dest}")

def find_files (sour):
    file_with_path = []
    for pa, dirs, files in os.walk(sour):
        for f in files:
            f_path = os.path.join(pa, f)
            file_with_path.append(f_path)
    return file_with_path

# def find_files_type (sour):
#     file_type_with_path = []
#     for pa, dirs, files in os.walk(sour):
#         for type in files.split('.')[1]:
#             f_path = os.path.join(pa, type)
#             file_type_with_path.append(f_path)
#     return file_type_with_path


def cp_file_in_dir (file_in_dir, dest):
    for f in file_in_dir:    
        with open (f, "r") as f_read:
            data = f_read.read()
        name = os.path.basename(f)
        new_path = os.path.join(dest, name) 
        with open (new_path, "w") as f_write:
            f_write.write(data)

def cp_dir (sour, dest):
    file_in_dir = find_files(sour)
    cp_file_in_dir (file_in_dir, dest)
    print (f"Copy a directory from {sour} to {dest}")

def display_cp(sour, dest):
    name = os.path.basename(sour)
    if name.find(".") == -1:
        try:
            cp_dir (sour, dest)
            print (f"Copy a directory from {sour} to {dest}")
        except OSError as e:
            print (e)
    else:
        try:
            cp_file(sour, dest)
            print (f"Copy a file from {sour} to {dest}")
        except OSError as e:
            print (e) 

#def display_mv(sour, dest):
#    try:
#        mov = shutil.move (sour, dest)
#        print (f"Move a file or directory from {sour} to {dest}")
#    except OSError as e:
#            print (e)

def mv_file (sour, dest):
    with open (sour, "r") as f_read:
        data = f_read.read()
    with open (dest, "w") as f_write:
        f_write.write(data)
    print (f"Move a file from {sour} to {dest}")
    os.remove (sour)

def mv_file_in_dir (file_in_dir, dest):
    for f in file_in_dir:    
        with open (f, "r") as f_read:
            data = f_read.read()
        name = os.path.basename(f)
        new_path = os.path.join(dest, name) 
        with open (new_path, "w") as f_write:
            f_write.write(data)
        os.remove(f)

def mv_dir (sour, dest):
    file_in_dir = find_files(sour)
    mv_file_in_dir (file_in_dir, dest)
    print (f"Move a directory from {sour} to {dest}")

def display_mv(sour, dest):
    name = os.path.basename(sour)
    if name.find(".") == -1:
        try:
            mv_dir (sour, dest)
            print (f"Move a directory from {sour} to {dest}")
        except OSError as e:
            print (e)
    else:
        try:
            mv_file(sour, dest)
            print (f"Move a file from {sour} to {dest}")
        except OSError as e:
            print (e)

def display_find (name, path):
    if name.find(".") == -1:
        result = []
        for pa, dirs, files in os.walk(path):
            if name in dirs:
                print(name)
                result.append(os.path.join(pa, name))
        print(result)
    else:
        result = []
        for pa, dirs, files in os.walk(path):
            if name in files:
                print(name)
                result.append(os.path.join(pa, name))
        print(result)

def display_find_type (typ, path):
    result = []
    for pa, dirs, files in os.walk(path):
        for file in files:
            if file.find('.') == -1:
                pass
            else:
                if typ == file.split('.')[1]:

                    result.append(os.path.join(pa, file))
                    print(result)


def display_cat(file):
    with open (file , "r") as f:
        data = f.read()
        print (data)

def log_command(line):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d")
        file.write(f"{time_now}: {line}\n")

def show_logs():
    with open("commands.log", "r") as file:
        print(file.read())

def display_pwd ():
    print ("Current directory now:" , os.getcwd())

####### main ########
parser = setup()
args = parser.parse_args()
command_line = " ".join(sys.argv)
log_command(command_line)

if args.path:
    path = args.path
else:
    path = os.getcwd()
if args.file:
    file = args.file
if args.dirc:
    dirc = args.dirc
if args.sour:
    sour = args.sour
if args.dest:
    dest = args.dest
if args.name:
    name = args.name
if  args.typ:
    typ = args.typ
if args.ls:
    display_ls(path)
if args.cd:
    display_cd(path)
if args.mkdir:
    display_mkdir (path)
if args.rmdir:
    display_rmdir (path)
if args.rm:
    display_rm (file)
if args.rm_r:
    display_rm_r(dirc)
if args.cp:
    display_cp(sour, dest)
if args.mv:
    display_mv(sour, dest)
if args.find:
    display_find (name, path)
if args.find_type:
    display_find_type(typ , path)
if args.cat:
    display_cat(file)  

if args.pwd:
    display_pwd()
