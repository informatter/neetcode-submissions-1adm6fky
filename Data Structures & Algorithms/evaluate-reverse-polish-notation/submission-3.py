
class Solution:

    def __init__(self):

        self._ops = {'*':self._mul,'-':self._sub,'+':self._add,'/':self._div}
    def _add(self,a:int,b:int)->int:
        return a+b
    def _sub(self,a:int,b:int)-> int:
        return a-b
    def _mul(self,a:int,b:int)-> int:
        return a*b
    def _div(self,a:int,b:int)-> int:
        return int(a/b)
    def evalRPN(self, tokens: List[str]) -> int:
        # tokens contains integers as strings
        # stack will be used to store numbers up to operand and intermediate results. Similar logic to how a 
        # stack based VM (Virtual Machine) works for interpreted programming languages.

        # iterate tokens with outer forloop, add to stack if tokens[i] is not an operand
        # when an operand is encountered, we pop the last 2 items, do the arithmetic operation and push back to stack
        stack = [] 
        for token in tokens:

            if token in self._ops:
                func = self._ops[token]
                b = stack.pop()
                a= stack.pop()
                result = func(int(a),int(b))
                stack.append(result)
                continue

            stack.append(token)
    
        return int(stack[0])


        