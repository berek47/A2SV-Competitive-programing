class Solution:
    def maxProduct(self, words: list[str]) -> int:
        max_product = 0
        word_char_sets = {word: set(word) for word in words}
        
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                word1, word2 = words[i], words[j]
                if not word_char_sets[word1] & word_char_sets[word2]:
                    max_product = max(max_product, len(word1) * len(word2))
                    
        return max_product
