#!/usr/bin/env python3
import shutil, os

from pathlib import Path
from requests import get

HOME = Path('~/').expanduser()
DOTS = Path('./dots')
CUTTER_URL = 'https://github.com/rizinorg/cutter/releases/download/v2.1.2/Cutter-v2.1.2-Linux-x86_64.AppImage'

def install_cutter():
    r = get(CUTTER_URL)
    with open('./downloads/cutter', 'wb') as f:
        f.write(r.content)
    shutil.move('./downloads/cutter', HOME / '.local/bin/cutter')
    os.chmod(HOME / '.local/bin/cutter', 0o755)  # rwx|r-x|r-x
    return

if __name__ == '__main__':
    print('[=] Adding dotfiles')
    shutil.copytree(DOTS, HOME, dirs_exist_ok=True) # will overwrite previous files
    print('[=] Download cutter')
    install_cutter()
    print('[+] Done!')