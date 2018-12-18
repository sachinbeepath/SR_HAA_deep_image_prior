cadcUrlList.txt contains URLs for all files containing the galaxy.

get_CFHT_data.ipynb gets necessary fits files

make_soft_link creates soft link for files so we don't have to change their names

jobscript.sh creates job for making cutouts. it calls my_executable.exe which which calls make_cutouts.py

rename_with_filters.ipynb renames cutouts based on their filter
