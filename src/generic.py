import utils as u

class Generic():
    def __init__(
            self,
            path: str,
            **kwargs
        ):
        self.path: str = None
        for key, item in kwargs.items():
            setattr(self, key, item)


    def to_file(self):
        params = 
        for key, value in self.__dict__
        params = self.__dict__.copy()


    @classmethod
    def from_file(cls, file: str):
        params = u.read_yaml(file=file)
        return cls(**params)