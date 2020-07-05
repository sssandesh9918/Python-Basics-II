# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
class py_solution:
   def valid_brackets(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for brack in str1:
            if brack in pchar:
                stack.append(brack)
            elif len(stack) == 0 or pchar[stack.pop()] != brack:
                return False
        return len(stack) == 0

print(py_solution().valid_brackets("(){}[]"))
print(py_solution().valid_brackets("()[{)}"))
print(py_solution().valid_brackets("()"))
print(py_solution().valid_brackets("[})({}"))
print(py_solution().valid_brackets("({[]})"))