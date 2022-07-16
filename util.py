from argparse import ArgumentParser
from managment import FileManager, BaseFileCreator
import contents


class HTMLFileCreator(BaseFileCreator):
    content = contents.HTML
    name = 'index.html'


class JSFileCreator(BaseFileCreator):
    content = ''
    name = 'script.js'


# CSS FILES
class CSSMainFileCreator(BaseFileCreator):
    content = ''
    name = 'styles.css'
    represent_in_dir = True


class CSSResetCreator(BaseFileCreator):
    content = contents.CSS
    name = 'reset.css'
    represent_in_dir = True


# README FILE
class READMEFileCreator(BaseFileCreator):
    content = contents.README
    name = 'README.md'


def main():
    parser = ArgumentParser(description="Python HTML5 boilerplate creating util")

    parser.add_argument("dirname", type=str, help="New boilerplate's name")
    parser.add_argument("-p", "--path", type=str, help="set path to boilerplate directory")
    args = parser.parse_args()

    manager = FileManager(args.dirname, [
        HTMLFileCreator,
        CSSMainFileCreator,
        CSSResetCreator,
        JSFileCreator,
        READMEFileCreator
    ], dir_path=args.path)
    manager.dir_init()
    manager.build()


if __name__ == '__main__':
    main()
