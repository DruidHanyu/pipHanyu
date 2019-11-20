#----------------------------------------------------------------------------
# utilitieshy.py
#
# Requirements:(for Python3)
#   numpy must be installed
#   pandas must be installed
#   librosa must be installed
#   soundfile must be installed
#
# Description:
#   This file contains some commonly used functions edited by Hanyu.
#
# 2017-2020 Hanyu, Beijing University of Posts and Telecommunications
# Diversion contrary to Hanyu prohibited.
#----------------------------------------------------------------------------
import os
import sys
import csv
import inspect
import shutil
import librosa
import soundfile
import numpy as np
import pandas as pd

'''
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../Toolshy'))

fullpath = .../nparent_folder/.../parent_folder/current_folder/dirs(file = filename + filesuff,..)
Functions List:
  1   current_folder = folder_cur()
  2   parent_folder  = folder_pre()
  3   nparent_folder = folder_npre(folder)
  4   dirs           = getdir_folder_cur()
  5   dirs           = getdir_folder_pre()
  6   dirs           = getdir_folder(folder)
  7   dir_suff       = getdir_folder_filesuff(folder, suff)
  8   dir_name       = getdir_folder_filename(folder, name)
  9   file_name      = filename(file)
  10  file_suff      = filesuff(file)
  11  folder         = folder_fullpath(fullpath)
  12  file           = file_fullpath(fullpath)
  13  filename       = filename_fullpath(fullpath)
  14  filesuff       = filesuff_fullpath(fullpath)
  15  fullpath       = getfullpath_file(file)
  16  output         = combine(folder, file, file2 = None, file3 = None, file4 = None, file5 = None):
  17  N/A            = file_move(fullpath, newfolder)
  18  N/A            = file_copy(fullpath, newfolder)
  19  N/A            = file_rename(fullpath, newname)
  20  N/A            = folder_creat(newfolder)
  21  N/A            = folder_cur_creat(foldername)
      N/A            = folder_pre_creat(foldername)
  22  column         = getcol_csv(file, col=0)
  23  rowlist/rowarray = getrow_csv(file, num=-1)
  24  col_datas      = getnamecol_csv(file, colname, sep)
  25  subt           = subt_array(arrayMax, arratMin)
  26  newarray       = shuffle_array(Num, array)
  27  N/A            = writerow_csv(newfile, array)
  28  subarray,len   = find_lcsubarray(s1, s2)
  29  audio, fs      = read_audio(path, target_fs = None)
  30  mean, std      = calculate_scalar(x ,axis = None)
  31  x_zmNorm       = zmNorm(x, mean, std)
  32  zmNorm_x       = REzmNorm(x, mean, std)
  33  N/A            = creatrow_csv(path, head="NoName", head2=None, head3=None, re=False)
  34  result         = path_check(path)
  35  N/A            = addrow_csv(path,row)
  36  namerow        = getnamerow_csv(file, name, sep = "\t")
  37  result         = array_to_str(array,symb=None)
  38  N/A            = var_print(var)
  39  var            = input_detect(var, alpha=False, space=False, digit=False, 
                                    other1=None, other2=None, other3=None, other4=None)
  40  alldir_suff    = getalldir_folder_filesuff(folder, suff)
  41  N/A            = folder_delete(folder)
  
'''
'''
Version history:
19.08.06.16.hy
    [ADD_Number]:   40,41

19.07.27.20.hy
    [ADD_Number]:   38,39
    
19.07.25.20.hy
    [number]: 1
    [Remarks]: Update
    
    [ADD_Number]:   33,34,35,36,37

19.07.24.16.hy
    [ADD_Function]: def zmNorm(x, mean, std)/RE
    [ADD_Number]:   31,32
    [ADD_Remarks]: None

    [ADD_Function]: def calculate_scalar(x ,axis = None)
    [ADD_Number]:   30
    [ADD_Remarks]: None

    [Number]: 23 
    [Remarks]：Rewrite.

    [Number]: 16 
    [Remarks]：Optimizer.

    [Remarks]：Added method to configure environment variables.
      
19.07.23.15.hy   
    [ADD_Function]: def read_audio(path, target_fs = None)
    [ADD_Number]:   29
    [ADD_Remarks]: None

19.07.22.23.hy
    [ADD_Function]: def find_lcsubarray(s1, s2)
    [ADD_Number]:   28
    [ADD_Remarks]: Array common subnumber.

    [ADD_Function]: def writerow_csv(newfile, array)
    [ADD_Number]:   27
    [ADD_Remarks]: None
    
earliest~
    A total of 28 functions are organized.
'''

# 1  Get current folder path.
def folder_cur():

    current_folder = sys.path[0]

    return current_folder

# 2  Get parent folder path.
def folder_pre():

    parent_folder = os.path.dirname(folder_cur())

    return parent_folder

# 3  Get nparent folder path.
def folder_npre(folder):

    nparent_folder = os.path.dirname(folder)

    return nparent_folder

# 4  Get dirs in current path.
def getdir_folder_cur():

    dirs = os.listdir(folder_cur())

    return dirs

# 5  Get dirs in parent path.
def getdir_folder_pre():

    dirs = os.listdir(folder_pre())

    return dirs

# 6  Get dirs in designation path.
def getdir_folder(folder):

    dirs = os.listdir(folder)

    return dirs

# 7  Get designation suffix file.
def getdir_folder_filesuff(folder, suff):

    dir_suff = []
    dirs = getdir_folder(folder)
    for x in dirs:
        if os.path.splitext(x)[1] == suff:
            dir_suff.append(x)

    return dir_suff

# 8  Get designation suffix file.
def getdir_folder_filename(folder, name):
    dir_name = []
    dirs = getdir_folder(folder)
    for x in dirs:
        if name in os.path.splitext(x)[0]:
            dir_name.append(x)

    return dir_name

# 9  Get file name.
def filename(file):

    file_name = os.path.splitext(file)[0]

    return file_name

# 10 Get file suffix.
def filesuff(file):

    file_suff = os.path.splitext(file)[1]

    return file_suff

# 11 Get fullpath dirs.
def folder_fullpath(fullpath):

    (folder, _) = os.path.split(fullpath)

    return folder

# 12 Get fullpath file.
def file_fullpath(fullpath):

    (_, file) = os.path.split(fullpath)

    return file

# 12 Get fullpath filename.
def filename_fullpath(fullpath):

    (_, file) = os.path.split(fullpath)
    (filename, _) = os.path.splitext(file)

    return filename


# 14 Get fullpath filesuff.
def filesuff_fullpath(fullpath):

    (_, file) = os.path.split(fullpath)
    (_, filesuff) = os.path.splitext(file)

    return filesuff

# 15 Get file path.
def getfullpath_file(file):

    fullpath = os.path.abspath(file)

    return fullpath

# 16 Combine path and folder/file.
def combine(folder, file, file2 = None, file3 = None, file4 = None, file5 = None):

    if (file2 == None):
        output = os.path.join(folder, file)
    elif (file3 == None):
        output = os.path.join(folder, file, file2)
    elif (file4 == None):
        output = os.path.join(folder, file, file2, file3)
    elif (file5 == None):
        output = os.path.join(folder, file, file2, file3, file4)
    else:
        output = os.path.join(folder, file, file2, file3, file4, file5)

    return output

# 17 Move the file.
def file_move(fullpath, newfolder):

    filename = file_fullpath(fullpath)
    new_fullpath = combine(newfolder, filename)
    shutil.move(fullpath, new_fullpath)

    return

# 18 Copy the file.
def file_copy(fullpath, newfolder):

    filename = file_fullpath(fullpath)
    new_fullpath = combine(newfolder, filename)
    shutil.copyfile(fullpath, new_fullpath)

    return

# 19 Change file name.
def file_rename(fullpath, newname):

    filesuff = filesuff_fullpath(fullpath)
    folder = folder_fullpath(fullpath)
    new_file = newname + filesuff
    new_fullpath = combine(folder, new_file)
    os.rename(fullpath, new_fullpath)

    return

# 20 Creat folder.
def folder_creat(newfolder):

    if not os.path.exists(newfolder):
        os.makedirs(newfolder)

    return

# 21 Creat folder in current path.
def folder_cur_creat(foldername):

    path = folder_cur()
    newpath = combine(path, foldername)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    return

def folder_pre_creat(foldername):

    path = folder_pre()
    newpath = combine(path, foldername)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    return

# 22 Get csv col.
def getcol_csv(file, col=0):

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        column = [row[col]for row in reader]

    return column

# 23 Get csv row.
def getrow_csv(file, num=-1):

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        rowlist = list(reader)
        if num == -1:
            return rowlist
        else:
            rowarray = rowlist[num]

            return rowarray

# 24 Get csv col from colname.
def getnamecol_csv(file, colname, sep = '\t'):

    df = pd.read_csv(file, sep=sep)
    df = pd.DataFrame(df)
    col_datas = []
    for row in df.iterrows():
        col_data = row[1][colname]

        col_datas.append(col_data)
    return col_datas

# 25 Array subtract.
def subt_array(arrayMax,arratMin):

    subt = np.array([x-y for x, y in zip(arrayMax, arratMin)])

    return subt

# 26 Shuffle the array order and take N of them.
def shuffle_array(Num, array):
    random_state = np.random.RandomState(0)
    indexes = np.arange(len(array))
    random_state.shuffle(indexes)
    indexes = indexes[0: Num]
    newarray = [array[idx] for idx in indexes]

    return newarray

# 27 Write csv row.
def writerow_csv(newfile,array):

    with open(newfile, 'a') as f:
        row = array
        write = csv.writer(f)
        write.writerow(row)

    return

# 28 Array common subnumber.
def find_lcsubarray(s1, s2):

    m = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    mmax = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1] = m[i][j]+1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p = i+1
    return s1[p-mmax:p], mmax

# 29 Read audio.
def read_audio(path, target_fs=None):

    (audio, fs) = soundfile.read(path)

    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)
    if target_fs is not None and fs != target_fs:
        audio = librosa.resample(audio, orig_sr=fs, target_sr=target_fs)
        fs = target_fs

    return audio, fs

# 30 Calculate mean/std
def calculate_scalar(x ,axis = None):

    if (axis == None):
        mean = np.mean(x)
        std = np.std(x)
    elif (axis == "row"):
        mean = np.mean(x, axis=1)
        std = np.std(x, axis=1)
    elif (axis == "col"):
        mean = np.mean(x, axis=0)
        std = np.std(x, axis=0)

    return mean, std

# 31 Zero-mean normalization.
def zmNorm(x, mean, std):

    x_zmNorm = (x - mean) / std

    return x_zmNorm

# 32 Inverse Zero-mean normalization.
def RezmNorm(x, mean, std):

    zmNorm_x = x*std + mean

    return zmNorm_x

# 33 Create csv and write in rows.
def creatrow_csv(path, head="NoName", head2=None, head3=None, re=False):
    if not path_check(path):
        if (head2 == None):
            with open(path, "w") as f:
                csv_write = csv.writer(f)
                csv_head = [head]
                csv_write.writerow(csv_head)
        elif (head3 == None):
            with open(path, "w") as f:
                csv_write = csv.writer(f)
                csv_head = [head, head2]
                csv_write.writerow(csv_head)
        else:
            with open(path, "w") as f:
                csv_write = csv.writer(f)
                csv_head = [head, head2, head3]
                csv_write.writerow(csv_head)
        return
    elif re:
        if (head2 == None):
            with open(path, "w") as f:
                csv_write = csv.writer(f)
                csv_head = [head]
                csv_write.writerow(csv_head)
        elif (head3 == None):
            with open(path, "w") as f:
                csv_write = csv.writer(f)
                csv_head = [head, head2]
                csv_write.writerow(csv_head)
        else:
            with open(path, "w") as f:
                csv_write = csv.writer(f)
                csv_head = [head, head2, head3]
                csv_write.writerow(csv_head)
        return
    else:
        return

# 34 Check the folder/file exist.
def path_check(path):

    result = os.path.exists(path)

    return result

# 35 Add row in csv.
def addrow_csv(path,row):

    with open(path, 'a+') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(row)
    return

# 36 Get name csv row.
def getnamerow_csv(file, name, sep = "\t"):

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=sep)
        rowlist = list(reader)
        for i in range(len(rowlist)):
            if rowlist[i][0] == name:
                namerow = rowlist[i][1:]
                return namerow
        rowarray = rowlist

        return rowarray

# 37 Array to str.
def array_to_str(array,symb=None):

    if symb ==None:

        result = ''.join(array)
        return  result

    else:
        result = symb.join(array)
        return result

# 38 Print.
def retrieve_name_ex(var):
    stacks = inspect.stack()
    try:
        callFunc = stacks[1].function
        code = stacks[2].code_context[0]
        startIndex = code.index(callFunc)
        startIndex = code.index("(", startIndex + len(callFunc)) + 1
        endIndex = code.index(")", startIndex)
        return code[startIndex:endIndex].strip()
    except:
        return ""

def var_print(var):

    print("【{}】: {}".format(retrieve_name_ex(var), var))
    try:
        print("【{}】(shape): {}".format(retrieve_name_ex(var), var.shape))
        print("【{}】(type): {}".format(retrieve_name_ex(var), type(var)))
    except Exception:
        print("【{}】(len) : {}".format(retrieve_name_ex(var), len(var)))
        print("【{}】(type): {}".format(retrieve_name_ex(var), type(var)))

    return

# 39 Detect the input is/not legal.
def input_detect(var, alpha=False, space=False, digit=False, other1=None, other2=None, other3=None, other4=None):
    length = len(var)
    detect = 0
    letters = 0
    space_len = 0
    digit_len = 0
    others_len = 0
    other1_len = 0
    other2_len = 0
    other3_len = 0
    other4_len = 0
    list_legal = []
    list_illegal = []

    for c in var:
        if c.isalpha():
            letters += 1
            if not alpha:
                list_illegal.append(c)
        elif c.isspace():
            space_len += 1
            if not space:
                list_illegal.append(c)
        elif c.isdigit():
            digit_len += 1
            if not digit:
                list_illegal.append(c)
        elif not (other1 is None):
            if c == other1:
                other1_len += 1
            else:
                list_illegal.append(c)
        elif not (other2 is None):
            if c == other2:
                other2_len += 1
            else:
                list_illegal.append(c)
        elif not (other3 is None):
            if c == other3:
                other3_len += 1
            else:
                list_illegal.append(c)
        elif not (other4 is None):
            if c == other4:
                other4_len += 1
            else:
                list_illegal.append(c)
        else:
            others_len += 1
            list_illegal.append(c)

    if alpha:
        detect += letters
        list_legal.append("Alpha")
    if space:
        detect += space_len
        list_legal.append("Space")
    if digit:
        detect += digit_len
        list_legal.append("Digit")
    if not (other1 is None):
        detect += other1_len
        list_legal.append("{}".format(other1))
    if not (other2 is None):
        detect += other2_len
        list_legal.append(other2)
    if not (other3 is None):
        detect += other3_len
        list_legal.append(other3)
    if not (other4 is None):
        detect += other4_len
        list_legal.append(other4)

    if length == detect:
        return var
    else:
        print(list_illegal, "are NOT in", list_legal, end="\n")
        newvar = input('Please enter again: ')
        input_detect(newvar, alpha, space, digit, other1, other2, other3, other4)
        return newvar

# 40  Get ALL designation suffix file.
def getalldir_folder_filesuff(folder, suff):

    alldir_suff = []

    for fpathe,dirs,fs in os.walk(folder):
        for f in fs:
            fullpaths = os.path.join(fpathe, f)
            if fullpaths.endswith(suff):
                alldir_suff.append(fullpaths)

    return alldir_suff

# 41 Delete all dirs in the folder.
def folder_delete(folder):

    dirslist = os.listdir(folder)

    for d in dirslist:
        dirpath = os.path.join(folder, d)
        if os.path.isfile(dirpath):
            os.remove(dirpath)
        elif os.path.isdir(dirpath):
            shutil.rmtree(dirpath, True)
    shutil.rmtree(folder, True)

    return











# import time
# import eventlet
# eventlet.monkey_patch()#必须加这条代码
# with eventlet.Timeout(5,False):
#    time.sleep(4)
#    print('没有跳过这条输出')
# print('跳过了输出')

# with tqdm(total=20) as pbar:
#     for i in range(5):
#         pbar.update(10)
#list(map(float, array))


