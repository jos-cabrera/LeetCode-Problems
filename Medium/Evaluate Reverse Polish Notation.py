# 150 - Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers = []

        for token in tokens:
            if token == "+":
                numbers.append(numbers.pop(-2) + numbers.pop(-1))
            elif token == "-":
                numbers.append(numbers.pop(-2) - numbers.pop(-1))
            elif token == "*":
                numbers.append(numbers.pop(-2) * numbers.pop(-1))
            elif token == "/":
                numbers.append(int(numbers.pop(-2) / numbers.pop(-1)))
            else:
                numbers.append(int(token))
        
        return numbers[0]