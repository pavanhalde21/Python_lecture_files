# “Text file manager” program.

# importing the required modules
import os
import argparse

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."

def validate_file(file_name):
    """validate file name and path"""
    if not valid_path(file_name):   ### see how "if not" is used
        print(INVALID_PATH_MSG%(file_name)) # here file_name is passed into %s of the variable INVALID_PATH_MSG
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG%(file_name))
        quit()
    
    return

def valid_filetype(file_name):
    # validate file path
    return file_name.endswith('.txt')

def valid_path(path):
    # validate file path
    return os.path.exists(path)

def read(args):
    # get the file name/path
    file_name = args.read[0]  ############################

    # validate the file name/path
    validate_file(file_name)                       # both path and file_type validation done 

    # read and print the file content
    with open(file_name, 'r') as f:
        print(f.read())

def show(args):   
    # get path to directory
    dir_path = args.show[0] ##############################

    # validate path
    if not valid_path(dir_path):                   # only path validation done
        print("Error: No such directory found")
        exit()

    # os.listdir(path) method in python is used to get the list of all files and directories in the specified directory. 
    # If we don’t specify any directory, then list of files and directories in the current working directory will be returned.

    # get text files in directory 
    files = [f for f in os.listdir(dir_path) if valid_filetype(f)]  # this gives error if there are spaces in the file name of which path we are giving
    print("{} text files found.".format(len(files)))
    print('\n'.join(f for f in files))

def delete(args):
    # get the files name/path
    file_name = args.delete[0]

    # validate the file name/path
    validate_file(file_name)                      # both path and file_type validation done

    # delete the file
    os.remove(file_name)
    print("Successfully deleted {}.".format(file_name))

def copy(args):
    # file to be copied 
    file1 = args.copy[0]
    # file to copy upon
    file2 = args.copy[1]

    # validate the type of file 2 
    if not valid_filetype(file2):       # only path validation done
        print(INVALID_FILETYPE_MSG%(file2))
        exit()
    
    # copy file1 to file2
    with open(file1, 'r') as f1:
        with open(file2,'w') as f2:
            f2.write(f1.read())

    print("Successfully copied {} to {}.".format(file1, file2))

def rename(args):
    # old file name
    old_filename = args.rename[0]
    # new file name
    new_filename = args.rename[1]

    # validate the file to be renamed
    validate_file(old_filename)

    # validate the type of new file name
    if not valid_filetype(new_filename):                    # only file_type validation done
        print(INVALID_FILETYPE_MSG%(new_filename))
        exit()

    # renaming
    os.rename(old_filename, new_filename)
    print("Successfully renamed {} to {}.".format(old_filename, new_filename))

def main():
    # create parser object 
    parser = argparse.ArgumentParser(description = "A text file manager!")

    # defining arguments for parser object 
    parser.add_argument("-r","--read", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Open and reads the specified text file.")
    
    parser.add_argument("-s", "--show", type = str, nargs = 1,
                        metavar = "path", default = None,
                        help = "Shows all the text files on specified directioy path.\
                              Type '.' for current directory.")
    
    parser.add_argument("-d", "--delete", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Deletes the specified text file")
    
    parser.add_argument("-c", "--copy", type = str, nargs = 2,
                        metavar = ('file1','file2'), 
                        help = "Copy file1 content to file2 Warning: file2 will get overwritten")
    
    parser.add_argument("--rename", type = str, nargs = 2,
                        metavar = ('old_name','new_name'),
                        help = "Renames the specified file to a new name")
    
    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.read != None:
        read(args)

    elif args.show != None:
        show(args)
    
    elif args.delete != None:
        delete(args)
    
    elif args.copy != None:
        copy(args)
    
    elif args.rename != None:
        rename(args)

if __name__ == "__main__":
    # calling the main function
    main()



# args.show[0] 
# args.read[0]
# args.copy[0]
# args.rename[0]
# args.rename[1]
# may we this is used to define variables
# ??????

# D:\02 CS\02 PYTHON\Lecture Files>python argparse_2.py -h
# D:\02 CS\02 PYTHON\Lecture Files>python argparse_2.py -r myfile.txt
# D:\02 CS\02 PYTHON\Lecture Files>python argparse_2.py -s D:\
# D:\02 CS\02 PYTHON\Lecture Files>python argparse_2.py -d zzz.txt
# D:\02 CS\02 PYTHON\Lecture Files>python argparse_2.py -c myfile.txt myfile_copy.txt
# D:\02 CS\02 PYTHON\Lecture Files>python argparse_2.py --rename myfile_copy.txt myfile_c.txt
