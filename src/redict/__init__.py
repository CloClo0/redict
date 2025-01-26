class redict(dict):
    """
    Redict class provides additional functionalities for dict
    :param object: object which is a valid value for dict(object), see dict() documentation for details
    """
    class Get:
        """
        Get is the class that permit to use redict.get as an attribute or as a method
        """
        def __str__(self):
            return f"{self.__class__.__name__} object for redict.get"

        def __init__(self, _redict):
            # save redict object
            self.redict = _redict

        def __getattr__(self, key):
            # Return a callable that accepts the default value
            return lambda default=None: self._get(key, default)

        def __call__(self, key, default=None):
            return self._get(key, default)

        def _get(self, key, default):
            if key in self.redict:
                return self.redict[key]
            return default


    def __init__(self, object=None, **kargs):
        object = object or dict()
        super().__init__(object, **kargs)

    def __setattr__(self, key: str, value):
        if key.startswith('__'):
            raise ValueError(f"Invalid key name '{key}'")

        if key in dir(self):
            raise AttributeError(f'the name \'{key}\' is a reserved name')
        self[str(key)] = value

    def __getattr__(self, key):
        # this method is called if the previous-level method __get__ has failed to retrived attribute

        # If the key doesn't exist in dict, raise an Error
        if not key in self:
            raise AttributeError(f"Key '{key}' doesn't exist")

        return self[key]

    def __call__(self, key: str, default):
        return self.get(key, default)

    def __delattr__(self, key):
        if not key in self:
            raise AttributeError(f"Key '{key}' doesn't exist")

        if key in self:
            del self[key]

    def set(self, key: str, value):
        """
        Set value for a key
        Same as redict[key] = value
        :param key: key
        :param value: value
        """
        self[key] = value

    @property
    def get(self):
        """
        Obtain value with a key, return a default value if key doesn't exist, you can use redict.get as method redict.get(key, default) or as an attribute: redict.get.key(default)
        :return: key or default value
        """
        return self.Get(self)

def new(object=None, **kwargs) -> redict:
    """
    Generate a new redict instance
    :param object: object which is a valid value for dict(object), see dict() documentation for details
    :return: New redict
    """
    return redict(object, **kwargs)
