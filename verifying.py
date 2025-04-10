# isAlienSorted:
# - Map each character to its rank using the given alien order.
# - Compare adjacent words character by character.
# - Return False if order is violated or prefix issue found.

# TC: O(N * M), N = number of words, M = avg word length
# SC: O(1) for order_map


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        order_map = {}

        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break

        return True