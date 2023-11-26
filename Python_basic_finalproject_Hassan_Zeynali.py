import os
import datetime
import argparse
import sys
import shutil

#setup function in order to explain actions and values.
def setup():
    parser = argparse.ArgumentParser(description="Python CLI Tool for File Manipulation")
    parser.add_argument("-path", type= str, help="Get path for command")
    parser.add_argument("-file", type= str, help="Get file for command")
    parser.add_argument("-dirc", type= str, help="Get directory for command")
    parser.add_argument("-sour", type= str, help="Get source for command")
    parser.add_argument("-dest", type= str, help="Get destination for command")
    parser.add_argument("-name", type= str, help="Get name of files or directories for find command")
    parser.add_argument("-typ", type= str, help="Get type of a file for command")
    parser.add_argument("--ls", action="store_true", help="List directory contents at `path`, or the current directory if no path is given.")
    parser.add_argument("--cd", action="store_true", help="Change the working directory to path.")
    parser.add_argument("--mkdir", action="store_true", help="Create a new directory at path.")
    parser.add_argument("--rmdir", action="store_true", help="Remove the directory at path if it is empty.")
    parser.add_argument("--rm", action="store_true", help="Remove the file specified by file.")
    parser.add_argument("--rm-r", action="store_true", help="Remove the directory at directory and its contents recursively.")
    parser.add_argument("--cp", action="store_true", help="Copy a file or directory from source to destination.")
    parser.add_argument("--mv", action="store_true", help="Move a file or directory from source to destination.")
    parser.add_argument("--find", action="store_true", help="Search for files or directories matching pattern starting from path.")
    parser.add_argument("--find-type", action="store_true", help="Search for type of files matching pattern starting from path.")
    parser.add_argument("--cat", action="store_true", help="Output the contents of the file.")
    parser.add_argument("--show-logs",action="store_true", help="show all logs of the program")
    parser.add_argument("--pwd", action="store_true", help="Display Current directory")
    return parser

#this function use to show files and directories.
def display_ls (path):
    for p, d, f in os.walk(path):
        for file in f:
            print(file , end = " ,")
        for direc in d:
            print (direc , end = " ,")

# this function change working directory.
def display_cd (path):
    try:
        os.chdir(path)
        print ("Current directory now:" , os.getcwd())
    except OSError as e:
        print (e)
    except:
        print("Error")

#this function make a directory
def display_mkdir (path):
    try:
        os.mkdir(path)
        print (f"Create a new directory at {path}")
    except OSError as e:
        print (e)
    except:
        print("Error")

#this function remove a empty directory.
def display_rmdir (path):
    for pa, dirs, files in os.walk(path):
        if files == [] and dirs == []:
            try:
                os.rmdir(path)
                print (f"Remove the directory at {path}")
            except OSError as e:
                print (e)
            except:
                print("Error")
        else:
            print(f"{path} is not empty")

#this function remove a file
def display_rm (file):
    try:
        os.remove(file)
        print (f"Remove the file at {file}")
    except OSError as e:
        print (e)
    except:
        print("Error")

#this function remove a directory, that is not empty.
def display_rm_r(dirc):
    try:
        shutil.rmtree(dirc)
        print (f"Remove the directory at {dirc}")
    except OSError as e:
        print (e)
    except:
        print("Error")

#this function use to copy files, we also use this function in function display_cp
def cp_file (sour, dest):
    with open (sour, "r") as f_read:
        data = f_read.read()
    with open (dest, "w") as f_write:
        f_write.write(data)
    print (f"Copy a file from {sour} to {dest}")

#this function use to finde files in source path and we use this function in cp_dir & mv_dir. output is list of finded files.
def find_files (sour):
    file_with_path = []
    for pa, dirs, files in os.walk(sour):
        for f in files:
            f_path = os.path.join(pa, f)
            file_with_path.append(f_path)
    return file_with_path

#the output of find_files function and destination are the input of this function. we copy text of files and make new file in directory of destination with the exact source basename. this fuction use in cp_dir
def cp_file_in_dir (file_in_dir, dest):
    for f in file_in_dir:    
        with open (f, "r") as f_read:
            data = f_read.read()
        name = os.path.basename(f)
        new_path = os.path.join(dest, name) 
        with open (new_path, "w") as f_write:
            f_write.write(data)

#this funcion use to copy directory from source to destination. this function used in dispaly_cp
def cp_dir (sour, dest):
    file_in_dir = find_files(sour)
    cp_file_in_dir (file_in_dir, dest)
    print (f"Copy a directory from {sour} to {dest}")

#this function use to copy file or directory.
def display_cp(sour, dest):
    name = os.path.basename(sour)
    if name.find(".") == -1:
        try:
            cp_dir (sour, dest)
            print (f"Copy a directory from {sour} to {dest}")
        except OSError as e:
            print (e)
        except:
            print("Error")
    else:
        try:
            cp_file(sour, dest)
            print (f"Copy a file from {sour} to {dest}")
        except OSError as e:
            print (e) 
        except:
            print("Error")

#this function use to cut files, we also use this function in function display_mv
def mv_file (sour, dest):
    with open (sour, "r") as f_read:
        data = f_read.read()
    with open (dest, "w") as f_write:
        f_write.write(data)
    print (f"Move a file from {sour} to {dest}")
    os.remove (sour)

#the output of find_files function and destination are the input of this function. we cut text of files and make new file in directory of destination with the exact source basename. this fuction use in mv_dir
def mv_file_in_dir (file_in_dir, dest):
    for f in file_in_dir:    
        with open (f, "r") as f_read:
            data = f_read.read()
        name = os.path.basename(f)
        new_path = os.path.join(dest, name) 
        with open (new_path, "w") as f_write:
            f_write.write(data)
        os.remove(f)

#this funcion use to cut directory from source to destination. this function used in dispaly_mv
def mv_dir (sour, dest):
    file_in_dir = find_files(sour)
    mv_file_in_dir (file_in_dir, dest)
    print (f"Move a directory from {sour} to {dest}")

#this function use to cut file or directory.
def display_mv(sour, dest):
    name = os.path.basename(sour)
    if name.find(".") == -1:
        try:
            mv_dir (sour, dest)
            print (f"Move a directory from {sour} to {dest}")
        except OSError as e:
            print (e)
        except:
            print("Error")
    else:
        try:
            mv_file(sour, dest)
            print (f"Move a file from {sour} to {dest}")
        except OSError as e:
            print (e)
        except:
            print("Error")

#the input is name and paths file or directory. and the output is name finded in the path.
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

#this functions input is type and the paths of file, and the output are all files with the same type in that path.
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

#this funtion display the given file.
def display_cat(file):
    with open (file , "r") as f:
        data = f.read()
        print (data)

#this function save date and detailes of command.
def log_command(line):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
        file.write(f"{time_now}: {line}\n")

#this function shows log commands.
def show_logs():
    with open("commands.log", "r") as file:
        print(file.read())

#this function show the current directory.
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
if args.show_logs:
    show_logs() 
if args.pwd:
    display_pwd()