# -*- coding:utf-8 -*- 


import math
import sys

class RanckedList:

    def __init__(self, size):
        self.size = size
        self.mylist = []
        for i in range(size):
            self.mylist.append(None)

    def insert(self, distance, obj):
        found = None
        for i in range(self.size):
            if self.mylist[i]:
                d = self.mylist[i][0]
                if d < distance:
                    found = i
                    break
            else:
                self.mylist[i] = (distance, obj)
                break
        if found != None:
            for i in range(self.size-1, found, -1):
                self.mylist[i] = self.mylist[i-1]
            self.mylist[found] = (distance, obj)

    def printList(self):
        print '[',
        for item in self.mylist:
            if item:
                w, d = item
                print w, d, ", "
            else:
                print None,
        print '] '


class WordDictionary:
    words = 0
    size = 0
    dic = {}
    rank = {}

    def __init__(self, datapath):
        self.readData(datapath)

    def readData(self, datapath):
        fin = open(datapath, 'r')
        line = fin.readline()
        meta = line.split()
        self.words = int(meta[0])
        self.size = int(meta[1])
        for i in range(self.words):
            line = fin.readline()
            wordVec = line.split()
            word  = wordVec[0]
            wordVec.remove(word)
            vec = [float(x) for x in wordVec]
            self.dic[word] = vec
            self.rank[word] = i

    def searchWordForUser(self):
        print "Search words then show rank an vector"
        while True:
            print "Enter word or sentence (EXIT to break): "
            word = raw_input()
            if word == 'EXIT':
                break
            print word, 
            if word in wordDic.dic.keys(): 
                print wordDic.rank[word]
                print wordDic.dic[word]
            else:
                print '-1'

    def cosineDistance(self, word1, word2):
        v1 = self.dic[word1]
        v2 = self.dic[word2]
        sq1 = math.sqrt(sum([x*x for x in v1]))
        sq2 = math.sqrt(sum([x*x for x in v2]))
        product = sum([v1[i]*v2[i] for i in range(self.size)])
        return(product/(sq1*sq2))

    def cosineDistance2(self, v1, word2):
        #v1 = self.dic[word1]
        v2 = self.dic[word2]
        sq1 = math.sqrt(sum([x*x for x in v1]))
        sq2 = math.sqrt(sum([x*x for x in v2]))
        product = sum([v1[i]*v2[i] for i in range(self.size)])
        return(product/(sq1*sq2))

    def analogyForUser(self):
        print "Input 3 words, then find 10 closest words of C+(B-A) by cosine distance"
        while True:
            print "Enter 1st word (EXIT to break): "
            word1 = raw_input()
            if word1 == 'EXIT':
                break
            if not word1 in wordDic.dic.keys(): 
                print word1, "Not in dictionary"
                continue

            print "Enter 2nd word: "
            word2 = raw_input()
            if not word2 in wordDic.dic.keys(): 
                print word2, "Not in dictionary"
                continue

            print "Enter 3nd word: "
            word3 = raw_input()
            if not word3 in wordDic.dic.keys(): 
                print word3, "Not in dictionary"
                continue

            print "Task: ", word1, ":", word2, "::", word3, ":", "?"
            v1 = self.dic[word1]
            v2 = self.dic[word2]
            v3 = self.dic[word3]
            vec = [0] * self.size
            for i in range(self.size):
                vec[i] = v3[i] + v2[i] - v1[i]

            rankedList = RanckedList(10)
            for key in self.dic.keys():
                if key != word1 and key != word2 and key != word3:
                    d = self.cosineDistance2(vec, key)
                    rankedList.insert(d, key)
            rankedList.printList()
            print '----------------------'


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: python distance.py data_path"
    else:
        datapath = sys.argv[1]
        wordDic = WordDictionary(datapath)
        wordDic.analogyForUser()





