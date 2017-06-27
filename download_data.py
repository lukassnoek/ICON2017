""" This script downloads the data for the ICON2017 MVPA workshop
from Surfdrive (a data storage repository/drive from the
Dutch institute for IT in science/academia) using cURL,
which should be cross-platform. """

import subprocess
import os
import zipfile
import os.path as op


this_dir = op.dirname(op.realpath(__file__))
dst_dir = op.join(this_dir, 'data')

if not op.isdir(dst_dir):
    os.makedirs(dst_dir)

data_file = 'https://surfdrive.surf.nl/files/index.php/s/tosBy0KNb9BFUTC/download'
dst_file = op.join(dst_dir, 'firstlevel.zip')

if not op.isfile(dst_file):
    print("Downloading the data ...\n")
    cmd = "curl -o %s %s" % (dst_file, data_file)
    return_code = subprocess.call(cmd, shell=True)
    print("\nDone!")
    print("Unzipping ...", end='')
    zip_ref = zipfile.ZipFile(dst_file, 'r')
    zip_ref.extractall(dst_dir)
    zip_ref.close()
    print(" done!")
    os.remove(dst_file)
else:
    print("Data is already downloaded and located at %s" % dst_file)
