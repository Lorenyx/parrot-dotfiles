#!/usr/bin/env python3
import shutil

if __name__ == '__main__':
    print('[=] Installing dot files...')
    # --[ Move files to diretories ]--
    #TODO Ask before overwriting
    shutil.copy(r'./dots/.zshrc', r'~/.zshrc')
    shutil.copy(r'./dots/.pwninit-template.py', r'~/.config/pwninit-template.py')
    shutil.copy(r'./dots/terminator.config', r'~/.config/terminator/config')
    print('[+] Complete')