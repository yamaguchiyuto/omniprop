class Mapping:
    def __init__(self, values):
        i = 0
        self._map = {}
        for v in values:
            if v == -1: continue
            if not v in self._map:
                self._map[v] = i
                i += 1
        self._revmap = dict([(v,k) for k,v in self._map.items()])

    def __len__(self):
        return len(self._map)

    def get_id(self,v):
        if v in self._map:
            return self._map[v]
        else:
            return None

    def get_value(self, k):
        if k in self._revmap:
            return self._revmap[k]
        else:
            return None

if __name__ == '__main__':
    values = [8,4,1000,10,-500]
    m = Mapping(values)

    print m.get_id(-500)
    print m.get_value(m.get_id(10))
    print [m.get_id(v) for v in values]
