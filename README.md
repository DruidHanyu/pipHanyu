# pipHanyu

## USE: pip install littlebear £¨1.0.0£©

## Description:
   This file contains some commonly used functions edited by Hanyu.

 2017-2020 Hanyu, Beijing University of Posts and Telecommunications
 Diversion contrary to Hanyu prohibited.

## Requirements:(for Python3)
   numpy must be installed

   pandas must be installed

   librosa must be installed

   soundfile must be installed

## Functions List:
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

