"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []

        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    ans.append(".".join(parts))
                return
            for i in range(1, 4):
                if index + i > len(s):
                    break
                part = s[index:index + i]
                if len(part) > 1 and part[0] == "0":
                    continue
                if int(part) > 255:
                    continue
                parts.append(part)
                backtrack(index + i, parts)
                parts.pop()

        backtrack(0, [])
        return ans
obj=Solution()
print(obj.restoreIpAddresses("25525511135"))
