class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return
            if len(path) >= 4 or start >= len(s):
                return

            for end in range(start + 1, len(s) + 1):
                segment = s[start:end]
                if 0 <= int(segment) <= 255 and (segment == "0" or not segment.startswith("0")):
                    backtrack(end, path + [segment])

        result = []
        backtrack(0, [])
        return result

        