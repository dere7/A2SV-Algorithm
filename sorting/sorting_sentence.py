class Solution:
    def sortSentence(self, s: str) -> str:
        words = list(map(lambda w: (w[:-1], int(w[-1:])), s.split()))
        sorted_words = sorted(words, key=lambda w: w[1])
        return ' '.join(map(lambda x: x[0], sorted_words))
