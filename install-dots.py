#!/usr/bin/env python3
import shutil, os

from pathlib import Path
from requests import get

if __name__ == '__main__':
    print('[=] Installing dot files...')
    # --[ Move files to diretories ]--
    #TODO Ask before overwriting
    shutil.copy(r'./dots/.zshrc', Path('~/.zshrc'))
    os.chmod('~/.zshrc', 0o755) # rwx|r-x|r-x
    shutil.copy(r'./dots/.pwninit-template.py', Path('~/.config/pwninit-template.py'))
    shutil.copy(r'./dots/terminator.config', Path('~/.config/terminator/config'))
    # --[ Install cutter ]--
    print('[=] Downloading "cutter"...')
    url = 'https://github.com/rizinorg/cutter/releases/download/v2.1.2/Cutter-v2.1.2-Linux-x86_64.AppImage'
    r = get(url)
    with open('./downloads/cutter', 'wb') as f:
        f.write(r.content)
    shutil.move('./downloads/cutter', Path('~/.local/bin/cutter'))
    os.chmod('~/.local/bin/cutter', 0o755) # rwx|r-x|r-x
    print('[+] Done')