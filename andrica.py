def andrica(p,q):
    ans = q**(1/2)-p**(1/2)
    return True if ans<1 else False
    
print(andrica(9967,9973))