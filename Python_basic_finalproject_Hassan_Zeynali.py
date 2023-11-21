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
    parser.add_argument("--ls", action="store_true", help="List directory contents at `path`, or the current directory if no path is given.")
    parser.add_argument("--cd", action="store_true", help="Change the working directory to path.")
    parser.add_argument("--mkdir", action="store_true", help="Create a new directory at path.")
    parser.add_argument("--rmdir", action="store_true", help="Remove the directory at path if it is empty.")
    parser.add_argument("--rm", action="store_true", help="Remove the file specified by file.")
    parser.add_argument("--rm-r", action="store_true", help="Remove the directory at directory and its contents recursively.")
    parser.add_argument("--cp", action="store_true", help="Copy a file or directory from source to destination.")
    parser.add_argument("--mv", action="store_true", help="Move a file or directory from source to destination.")
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

def display_cp(sour, dest):
    s = os.path.basename(sour)
    if s.find(".") == -1:
        try:
            dest = shutil.copytree(sour, dest)
            print (f"Copy a directory from {sour} to {dest}")
        except OSError as e:
            print (e)
    else:
        try:
            dest = shutil.copyfile(sour, dest)
            print (f"Copy a file from {sour} to {dest}")
        except OSError as e:
            print (e) 

def display_mv(sour, dest):
    try:
        mov = shutil.move (sour, dest)
        print (f"Move a file or directory from {sour} to {dest}")
    except OSError as e:
            print (e)

def display_find (name, path):
    if name.find(".") == -1:
        result = []
        for pa, dirs, files in os.walk(path):
            if name in dirs:
                result.append(os.path.join(pa, name))
        print(result)
    else:
        result = []
        for pa, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(pa, name))
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
if args.cat:
    display_cat(file)  

if args.pwd:
    display_pwd()
