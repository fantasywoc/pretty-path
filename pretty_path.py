#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os

def build_directory_structure(folder_path):
    directory_structure = {}

    for root, dirs, files in os.walk(folder_path):

        current_dir = directory_structure
        for dir_name in root.split(os.sep):
            if dir_name:
                current_dir = current_dir.setdefault(dir_name, {})

        print(directory_structure)
        for file_name in files:
            current_dir[file_name] = None
        print(directory_structure)

    return directory_structure



def print_directory_structure(directory, indent=''):
    for key, value in directory.items():
        if isinstance(value, dict):
            print(f'{indent}└──·{key}')
            print_directory_structure(value, indent + '    ')
        else:
            print(f'{indent}└── {key}')

# 示例目录结构字典
directory_structure = {
    'documents': {
        'work': {
            'report.docx': None,
            'presentation.pptx': None
        },
        'personal': {
            'photos': {
                'summer.jpg':None,
                'winter.png':None
            },
            'diary.txt':None,
            'Path': {}
        }
    }
}



if __name__ == '__main__':
    path='/home/yb/图片/file_update/pretty-path/'
    print_directory_structure(directory_structure)

