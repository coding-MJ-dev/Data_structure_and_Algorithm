# 460. LFU Cache

# class LFUCache:

#     def __init__(self, capacity: int):


#     def get(self, key: int) -> int:


#     def put(self, key: int, value: int) -> None:
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = defaultdict(list)  # key : val, freq
        self.freq2key = defaultdict(list)  # freq :
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        freq = self.key2val[key][1]
        self.freq2key[freq].remove(key)
        if self.freq2key[freq] == []:
            if self.minfreq == freq:
                self.minfreq += 1
            del self.freq2key[freq]

        freq += 1
        self.key2val[key][1] = freq
        self.freq2key[freq].append(key)

        return self.key2val[key][0]

    def put(self, key: int, value: int) -> None:
        # print(self.key2val)
        # print(self.freq2key)
        if key in self.key2val:
            self.key2val[key][0] = value
            self.get(key)
        else:
            if len(self.key2val) == self.cap:
                # print(self.minfreq)
                del_key = self.freq2key[self.minfreq][0]
                # print(del_key)
                del self.key2val[del_key]
                self.freq2key[self.minfreq].pop(0)

            self.key2val[key] = [value, 1]
            if self.minfreq != 1:
                self.minfreq = 1
            self.freq2key[1].append(key)
