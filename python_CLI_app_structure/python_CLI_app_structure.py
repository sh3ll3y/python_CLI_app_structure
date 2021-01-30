import sys
import os


def main(name):

    os.mkdir(name)
    app_dir = name + '/' + name
    tests_dir = name + '/' + 'tests'

    os.mkdir(app_dir)
    print('Created app_dir :', app_dir)
    file_name = app_dir + '/' + name + '.py'
    open(file_name, 'w+').close()
    file_name = app_dir + '/' + '__init__.py'
    open(file_name, 'w+').close()

    os.mkdir(tests_dir)
    file_path = tests_dir + '/' + '__init__.py'
    with open(file_path, 'w+') as fp:
        lines = ['import sys \n', 'sys.path.append("../{name}/")'.format(name=name)]
        fp.writelines(lines)

    files = ['.gitignore', 'LICENSE', 'README.md', 'requirements.txt', 'setup.py']
    for _file in files:
        open(name + '/' + _file, 'w+').close()


if __name__ == "__main__":
    name = sys.argv[1]
    main(name)