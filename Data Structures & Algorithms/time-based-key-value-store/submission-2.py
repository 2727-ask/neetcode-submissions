class TimeMap:

    def __init__(self):
        self.map = defaultdict(str)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(timestamp, key)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (timestamp, key) in self.map:
            return self.map[(timestamp, key)]
        else:
            while(timestamp >= 0):
                if (timestamp, key) in self.map:
                    return self.map[(timestamp, key)]
                timestamp = timestamp - 1
            return ""
        
