import sys

class Chemistry:
    def __init__(self, cal):
        self.result = 0
        self.cal = cal
        self.sum = 0
        self.compare = ['2','3','4','5','6','7','8','9']

    def recursive(self,n):
        if n == len(self.cal):
            return self.result
        
        if 'H' in cal[n]:
            self.sum += 1
            return self.recursive(n+1)
        if 'O' in cal[n]:
            self.sum +=16
            return self.recursive(n+1)
        
        if 'C' in cal[n]:
            self.sum +=12
            return self.recursive(n+1)
        
        if '(' in cal[n]:
            return self.recursive(n+1)
        
        if cal[n] in self.compare:
            if ')' in cal[n-1]:
                self.result = self.sum * int(cal[n])
                self.sum = 0
                return self.recursive(n+1)
            else:
                self.result += self.sum
                return self.recursive(n+1)                 
        if ')' in cal[n]:
            self.result += self.sum
            return self.recursive(n+1)
        else:
            return


cal = sys.stdin.readline().rstrip()
cl = Chemistry(cal)
result = cl.recursive(0)
print(result)
