def linear_search(li,target):
    res="element not found"
    for i in range(len(li)):
        if li[i]==target:
            res=(f"element found at {i}")
    print(res)        
linear_search([12,45,23,87],80)            
