from typing import List

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        if k == 0:
            # sum 0 is always possible (empty subsequence)
            return [True] * n

        arr = sorted(nums)
        mask = (1 << (k + 1)) - 1

        # Build prefix DP bitsets:
        # pref[i] = bitset of reachable sums using arr[0..i-1]
        pref = [0] * (n + 1)
        pref[0] = 1  # only sum 0 reachable with zero items
        for i in range(n):
            v = arr[i]
            # If v > k, shifting by v would exceed all sums we care about; skip it
            if v > k:
                pref[i + 1] = pref[i]
            else:
                shifted = (pref[i] << v) & mask
                pref[i + 1] = (pref[i] | shifted) & mask

        answers = [False] * n

        # For each cap x = 1..n
        for x in range(1, n + 1):
            # Find first index where arr[index] >= x
            index = bisect_left(arr, x)
            # Items from index..n-1 will become exactly x
            ct = n - index

            # Try taking j of those x-valued items
            # j ranges from 0 up to ct, but also cannot exceed k//x or rem would go negative
            if x > 0:
                jmax = min(ct, k // x)
            else:
                jmax = 0  # not used here since x >= 1

            ok = False
            base_bits = pref[index]  # reachable sums using the uncapped prefix only
            for j in range(jmax + 1):
                rem = k - j * x
                # Check if "rem" is reachable using the prefix bitset
                # Test: is bit "rem" set in base_bits?
                if ((base_bits >> rem) & 1) == 1:
                    ok = True
                    break

            answers[x - 1] = ok

        return answers