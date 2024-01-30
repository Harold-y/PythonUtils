from pypdf import PdfWriter
from os import listdir
from os.path import isfile, join
import os


def merge_pdf(files, merged_name="merged-pdf.pdf"):
    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

    merger.write(merged_name)
    merger.close()

def list_files(mypath: str):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def get_curr_folder_files(print_f_name = True):
    cwd = os.getcwd()
    files = list_files(cwd)
    print(files) if print_f_name else None
    return files

if __name__ == "__main__":
    # files = []
    files = get_curr_folder_files()
    merge_pdf(files=files)
