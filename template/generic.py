import os
import template.utils as u

class Generic():
    params = {
        "name": None
    }
    def __init__(
            self,
            path: str = None,
            **kwargs
        ):
        self.path: str = path
        for key, item in self.params.items():
            setattr(self, key, item)
        for key, item in kwargs.items():
            setattr(self, key, item)
        if self.id is None:
            self.set_id()
        # Default to name of object as filename if a directory is provided as path
        if self.path is not None and os.path.isdir(self.path) and self.name is not None:
            self.path = os.path.join(self.path, self.name + ".yaml")

    def to_file(self, path: str = None, set_path=True):
        """Writes object properties to a YAML file.

        Args:
            path (str, optional): Path to write to file. If None, uses the object's `self.path`. Defaults to None.
            set_path (bool, optional): If True, sets the object's `self.path` using the provided `path`. Defaults to True.

        Raises:
            ValueError: If no `path` is provided, either as a parameter or as the object's `self.path`.
        """
        if path is None:
            if self.path is None:
                raise ValueError(f"Either {self.__class__}.path must be set or path provided to method.")
            else:
                path = self.path
        elif set_path:
            self.path = path
        dictionary=self.__dict__.copy()
        dictionary.pop("path")
        u.write_yaml(
            file=path,
            dictionary=dictionary
        )

    def set_id(self, idn: str = None, **kwargs) -> str:
        """Set ID of object.

        Args:
            idn (str, optional): _description_. Defaults to None.

        Returns:
            str: ID as set.
        """
        if idn is None:
            idn = self.generate_id(**kwargs)
        self.id = idn
        return idn

    def generate_id(self, **kwargs):
        return u.generate_id(**kwargs)

    @classmethod
    def from_file(cls, file: str):
        """Reads in an object from a YAML file.

        Args:
            file (str): Path to file.

        Returns:
            Generic: object created from the file.
        """
        params = u.read_yaml(file=file)
        return cls(path=file, **params)
    
    @classmethod
    def template_yaml(cls, path: str = "./template.yaml"):
        """Saves a template YAML file in the format for creating this object.

        Args:
            path (str): Path to save to. Defaults to './template.yaml'
        """
        u.write_yaml(path, cls.params)
