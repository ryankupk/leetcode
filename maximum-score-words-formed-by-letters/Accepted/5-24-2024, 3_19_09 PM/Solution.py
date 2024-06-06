// https://leetcode.com/problems/maximum-score-words-formed-by-letters

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def get_letter_score(letter):
            return score[ord(letter) - 97]

        def score_word(word, used_letter_indices):
            word_score = 0
            all_letters_valid = True
            for word_letter in word:
                found = False
                for idx, letters_letter in enumerate(letters):
                    if word_letter == letters_letter and idx not in used_letter_indices:
                        used_letter_indices.append(idx)
                        word_score += get_letter_score(word_letter)
                        found = True
                        break
                if not found:
                    all_letters_valid = False
                    break
            if all_letters_valid:
                return word_score
            else:
                return 0


        def generate_subsets(words, index, cur_subset, subsets):
            if index == len(words):
                subsets.append(cur_subset[:])
                return

            cur_subset.append(words[index])
            generate_subsets(words, index + 1, cur_subset, subsets)
            cur_subset.pop()
            generate_subsets(words, index + 1, cur_subset, subsets)

        subsets = []
        generate_subsets(words, 0, [], subsets)

        highest = 0
        for subset in subsets:
            current_score = 0
            used_letter_indices = []
            for word in subset:
                current_score += score_word(word, used_letter_indices)
            highest = max(highest, current_score)

        return highest