'''Calculate the total size of all files ending with .txt that aren't symlinks. (Using os and pathlib)
Move all .txt files to a new backup subdirectory
'''

import os, pathlib


def size_txt_pathlib(directory):
    size = 0
    found_txt_files = 0
    files = []
    path_obj = pathlib.Path(directory)
    print('Looking for .txt files in {0} directory'.format(directory))
    if path_obj.exists():
        for i in path_obj.iterdir():
            extension = i.suffix
            if not i.is_symlink() and extension == '.txt':
                size += i.stat().st_size
                found_txt_files += 1
                files.append(i.as_posix())
    else:
        print('Could not find {0} directory'.format(directory))
        return -1
    print('Found {0} files'.format(found_txt_files))
    print('\n'.join(files))
    return size


def size_txt_os(directory):
    size = 0
    found_txt_files = 0
    files = []
    print('Looking for .txt files in {0} directory'.format(directory))
    if os.path.exists(directory):
        for i in os.listdir(directory):
            file_path = os.path.join(directory, i)
            extension = os.path.splitext(file_path)
            if not os.path.islink(file_path) and extension[-1] == '.txt':
                size += os.path.getsize(file_path)
                found_txt_files += 1
                files.append(file_path)
    else:
        print('Could not find {0} directory'.format(directory))
        return -1
    print('Found {0} files'.format(found_txt_files))
    print('\n'.join(files))
    return size


def create_txt_backup(directory):
    # using pathlib
    files = []
    path_obj = pathlib.Path(directory)
    print('Looking for .txt files in {0} directory'.format(directory))
    if path_obj.exists():
        for i in path_obj.iterdir():
            extension = i.suffix
            if not i.is_symlink() and extension == '.txt':
                files.append(i)
        if files:
            new_path = pathlib.Path()
            new_path = new_path.joinpath(directory, 'backup')
            new_path.mkdir(exist_ok=True)
            for f in files:
                new_file = new_path.joinpath(f.name)
                print('Moving {0} to {1}'.format(f, new_file))
                f.rename(new_file)

    else:
        print('Could not find {0} directory'.format(directory))


def main():
    test_path = os.getcwd()
    print(test_path)
    print(size_txt_os(test_path))
    print(size_txt_pathlib(test_path))
    create_txt_backup(test_path)


if __name__ == '__main__':
    main()