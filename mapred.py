file = "fdfd dfdfd dfdfd dfdfdfdfdf dfdf dfdfd dfdfdfdfd dfd df dfd dfdfdfd"

def iterated_group(queue):
    prev_key = None
    bufferList = []

    for value in queue:
        curr_key, curr_val = value
        if curr_key == prev_key or prev_key is None:
            bufferList.append(curr_val)
        else:
            yield prev_key, bufferList
            bufferList = []
            bufferList.append(curr_val)
        prev_key = curr_key

    if bufferList:
        yield curr_key, bufferList

class MapReduce:
    def __init__(self):
        self.queue = []

    def send(self, wordOne, wordTwo):
        self.queue.append((wordOne, wordTwo))

    def count(self):
        return len(self.queue)    

    def __iter__(self):
        return iterated_group(sorted(self.queue))

mapExample = MapReduce()
for word in file.split(" "):
    mapExample.send(word, 1)

for word, ones in mapExample:
    print(word, sum(ones))