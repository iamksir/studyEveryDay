class SetOnceMappingMixin:
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""

my_dict = SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError as e:
    print(e)
print(my_dict)