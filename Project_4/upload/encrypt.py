# Small program to encrypt/decrypt file with promply password
# install 7-zip as dependency

import os, sys

def get_params():
    
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python %s encryptfile password \n " % sys.argv[0])
        raise SystemExit(1)
    encryptfile = sys.argv[1]
    password    = sys.argv[2]
    return encryptfile, password


# Use 7-zip to encrypt file
# Run 7-zip from subprocess

import zipfile
import subprocess

def encrypt_file(encryptfile, password):
    # import zlib to use
    
    archive_file = encryptfile + '.zip'
    password_params = '-p' + password
    # create archive
    rc = subprocess.call(['7z', 'a', password_params, '-y', archive_file] + [encryptfile])
    
    return archive_file

def decrypt_file(encryptedfile, encryptfile, password):
    z = zipfile.ZipFile(encryptedfile)
    #f = z.open('out.txt', 'r', pwd=password)    
        
    try:
        f = z.open(encryptfile, 'r', pwd=password)
        for line in f:
            print line
    except KeyError:
        print 'Error: Did not find %s in zip file' % encryptfile
    finally:
        z.close()
        
if __name__ == '__main__':
    fname, pwd = get_params()
    print fname, pwd
    archivefile = encrypt_file(fname, pwd)
    decrypt_file(archivefile, fname, pwd)

