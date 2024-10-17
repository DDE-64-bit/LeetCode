class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0, 0)
        
        l = len(digits)

        offSet = 1
        digits[l-offSet] += 1
        
        while True:
            if digits[l-offSet] == 10:
                digits[l-offSet] = 0
                offSet += 1
                
                digits[l-offSet] +=1
            else:
                break
        
        if digits[0] == 0:
            digits.pop(0)

        return digits