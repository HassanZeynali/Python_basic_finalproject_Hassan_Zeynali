# Python_basic_finalproject
Filoger Python basic final project
# Weather Forecast CLI

This is a Python command-line interface (CLI) Tool for File Manipulation.

## Setup

Ensure Python 3.8 or higher is installed on your system.

## Usage

Run the `Python_basic_finalproject_Hassan_Zeynali.py` script using Python with the desired arguments:

```bash
python Python_basic_finalproject_Hassan_Zeynali.py --ls
python Python_basic_finalproject_Hassan_Zeynali.py --ls -path "Path"
python Python_basic_finalproject_Hassan_Zeynali.py --cd -path "Path"
python Python_basic_finalproject_Hassan_Zeynali.py --mkdir -path "Path"
python Python_basic_finalproject_Hassan_Zeynali.py --rmdir -path "Path"
python Python_basic_finalproject_Hassan_Zeynali.py --rm -file "File"
python Python_basic_finalproject_Hassan_Zeynali.py --rm-r -dirc "Directory"
python Python_basic_finalproject_Hassan_Zeynali.py --cp -sour "Source" -dest "Destination"
python Python_basic_finalproject_Hassan_Zeynali.py --mv -sour "Source" -dest "Destination"
python Python_basic_finalproject_Hassan_Zeynali.py --find -name "Name" -path "Path"
python Python_basic_finalproject_Hassan_Zeynali.py --find-type -typ "Type" -path "Path"
python Python_basic_finalproject_Hassan_Zeynali.py --cat -file "File"
python Python_basic_finalproject_Hassan_Zeynali.p --show-logs
python Python_basic_finalproject_Hassan_Zeynali.p --pwd
```

### Arguments

- `-path`: Specify the path for which to action.
- `-file`: Specify the file for which to action.
- `-dirc`: Specify the directory for remove action.
- `-sour`: Specify the source for which to action.
- `-dest`: Specify the destination for which to action.
- `-name`: Specify the name (of file or directory) for finding in the path.
- `-typ`: Specify the type of file for finding in the path.
- `--ls`: Display all file and directories at the path or current directory. (should be used with `-path`).
- `--cd`: Change the working directory to path. (must be used with `-path`).
- `--mkdir`: Create a new directory at path. (must be used with `-path`).
- `--rmdir`: Remove the directory at path if it is empty. (must be used with `-path`).
- `--rm`: Remove the file specified by file. (must be used with `-file`).
- `--rm-r`: Remove the directory specified by directory. (must be used with `-dirc`).
- `--cp`: Copy a file or directory from source to destination. (must be used with `-sour` and `-dest`).
- `--mv`: Move a file or directory from source to destination. (must be used with `-sour` and `-dest`).
- `--find`: Search for files or directories matching pattern starting from path. (must be used with `-name` and `-path`).
- `--find-type`: Search for type of files matching pattern starting from path. (must be used with `-typ` and `-path`).
- `--cat`: Output the contents of the file. (must be used with `-file`).
- `--show-logs`: Show command logs for a specified time period.
- `--pwd`: Display Current directory.

## Logs

Logs of the executed commands are stored in `command.log`, with each entry timestamped.

---

Enjoy your personalized weather forecast CLI!