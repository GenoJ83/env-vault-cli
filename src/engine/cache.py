class KeyCache:
    _cached_key = None
    @classmethod
    def get(cls): return cls._cached_key
    @classmethod
    def set(cls, key): cls._cached_key = key
