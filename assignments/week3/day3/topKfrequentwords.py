import collections
import heapq
class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        #gets frequencies of all words in the list
        count = collections.Counter(words)
        #min heap
        heap = []
        #key is word, value is frequency
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            #only want to store the k most frequent
            #don't care about others
            #will remove smallest one when popping
            if len(heap) > k:
                heapq.heappop(heap)
        #put elements from heap onto list
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        #reverse list cuz it was from min heap
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
