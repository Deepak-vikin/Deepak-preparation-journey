"""
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.



Example 1:


Input: hour = 12, minutes = 30
Output: 165
Example 2:


Input: hour = 3, minutes = 30
Output: 75
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_hand=(hour*60)*0.5
        hour_hand+=minutes*0.5
        min_hand=minutes*6
        diff=abs(min_hand-hour_hand)
        return min(diff,360-diff)
obj=Solution()
print(obj.angleClock(12,15))
