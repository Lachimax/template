from .generic import Generic

class Container(Generic):
    def __init__(self, path = None, **kwargs):
        self._registry = {}
        super().__init__(path, **kwargs)
    
    def check_id(self, idn: str) -> bool:
        """Check object's registry for existing ID.

        Args:
            idn (str): ID

        Returns:
            bool: ID in registry?
        """
        return idn in self._registry

    def __getitem__(self, name):
        return self._registry[name]
    
    def __setitem__(self, name, value):
        return super().__setattr__(name, value)