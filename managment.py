from abc import ABC, abstractmethod
from pathlib import Path


class AbstractFileCreator(ABC):
    @abstractmethod
    def _create(self):
        """
        Method that handles creating
        specific file in root dir
        :return: None
        """
        pass

    def _create_representation_dir(self):
        """
        Method allows creating
        nested project directory file systems
        :return: None
        """
        pass


class BaseFileCreator(AbstractFileCreator):
    content = None
    name = 'default.txt'
    represent_in_dir = False

    def __init__(self, directory: Path):
        if self.represent_in_dir:
            self.root = Path(directory, self.name.split('.')[1])
            self._create_representation_dir()
        else:
            self.root = directory

        self.file = self._create()

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_val:
            print(exc_tb, exc_type, exc_val, sep="\n")

    def _create(self):
        file_root = Path(self.root, self.name)
        file = open(file_root, 'w', encoding="UTF-8")
        return file

    def _create_representation_dir(self):
        if not self.root.is_dir():
            self.root.mkdir(parents=True, exist_ok=False)


class FileManager:
    def __init__(self,
                 dir_name: str,
                 creators_list: tuple | list,
                 dir_path: str = None
                 ):
        self.iterable = creators_list
        self.root = Path(dir_path) if dir_path else Path(Path(__file__).parent.resolve(), dir_name)

    def dir_init(self):
        if not self.root.is_dir():
            self.root.mkdir(parents=True, exist_ok=False)

    def build(self):
        for creator in self.iterable:
            instance = creator(self.root)

            with instance as file:
                file.write(instance.content)
