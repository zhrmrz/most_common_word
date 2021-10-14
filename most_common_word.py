from collections import Counter
class Sol:
    def most_common_word(self, paragraph,banned):
        l=paragraph.lower().split()
        for i,word in enumerate(l):
            if ord(word[-1])<ord('a') or ord(word[-1])>ord('z'):
                l[i],word=word[:-1],word[:-1]
            if word in banned:
                l.remove(word)
        return list(Counter(l).most_common(1)[0])[0]
if __name__ == '__main__':
    p = Sol()
    print(p.most_common_word(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
