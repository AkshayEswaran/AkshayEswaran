#%%
# Multiples of 3 and 5
# Main Function
def multiples_3_5(x):
    num=[]
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            num.append(i)
        else:
            pass
    return sum(num)        

# %%
# Asking the input from user 
n=1
while (n!=0):
    upper_bound=input('Enter a Natural Number')
    
# Ensuring if it's a number
    if upper_bound.isnumeric():
        upper_bound_final=int(upper_bound)
        print(multiples_3_5(upper_bound_final))
        break

    else:
        print("Not a Natural Number")
        continue
# %%

# %%
