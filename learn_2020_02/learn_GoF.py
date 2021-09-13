class StreamHasher():
    """哈希摘要生成器(策略模式)"""

    def __int__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()

if __name__ == '__main__':
    hasher1 = StreamHasher()
    with open('C:\\Users\\wangkep\\Downloads\\nmon_analyzer_v61.zip', 'rb') as stream:
        print(hasher1.to_digest(stream))