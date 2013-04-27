import copy

class EnumException(Exception):
    pass

class enum(object):
    def __init__(self):
        self.name_map  = {}
        self.enums = []
        if self.def_enums:
            self.name_map = copy.deepcopy(self.def_enums)
            self.enums = self.name_map.values()
            self.enums.sort()
        else:
            raise EnumException("Enums cann't be empty. Please set def_enum in the class")
    def __getattr__(self, attr):
        if self.name_map.has_key(attr):
            return self.enums[attr]
        else:
            return super(enum, self).__getattr__(attr)
    def __len__(self):
        return len(self.enums)
    def next(self):
        for e in self.enums:
            yield e
    def human(self, value):
        return self.name_map[value]

