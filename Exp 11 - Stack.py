def pop(stack):
    stack.pop()
    
def push(value,stack,top,limit):
    if top>=limit:
        print("Stack overflow!")
    else:
        stack.append(value)

def peak(stack,top):
    return stack[top]

def display(stack,limit,top):
    for i in range(limit):
        print(stack[top])
        top=top-1
        if top<0:
            break

stack=[]
top=-1
limit=int(input("Please enter size of stack"))
for i in range(limit):
        a=input()
        stack.append(a)
        top+=1
print("Please select the command you want to execute:")
print("1: Adding value to stack")
print("2: Poping a value")
print("3: Displaying stack")
print("4: To print the last value")
b=int(input())
if b==1:
    print("Enter of elements you want to add")
    limit1=int(input())
    print("Before adding value:",stack)

    for i in range(limit1):
        value=input()
        push(value,stack,top,limit)
    print("After adding values:",stack)

elif b==2:
    print("Enter how many elements you want to remove")
    limit2=int(input())
    for i in range(limit2):
        print("Before Pop:",stack)
        pop(stack)
        print("After pop:",stack)

elif b==4:
    print("Last value is:",peak(stack,top))

elif b==3:
    print("The Current Stack elements are:")
    display(stack,limit,top)
