def Br(expr): 
    stack = [] 
 
    for cr in expr: 
        if cr in ["(", "{", "["]: 
  
            stack.append(cr) 
        else:  
            if not stack: 
                return False
            current_cr = stack.pop() 
            if current_cr == '(': 
                if cr != ")": 
                    return False
            if current_cr == '{': 
                if cr != "}": 
                    return False
            if current_cr == '[': 
                if cr != "]": 
                    return False
  
    if stack: 
        return False
    return True
  
  
if __name__ == "__main__": 
    value = input()
  
    if Br(value): 
        print("Balanced") 
    else: 
        print("Not Balanced")