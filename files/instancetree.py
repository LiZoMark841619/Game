class InstanceTree:
    
    def __str__(self):
        return f'Object created from {self.__class__.__name__} class with attributes: {self.attrs_()}'
    
    def attrs_(self):
        for attr in self.__dict__:
            print(attr, '->', self.__dict__[attr])
        