# Method-1
N, M = map(int,input().split())
for i in range(1,N,2):
    print((i * ".|.").center(M, "-"))

print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))

    
# Method-2 
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# Method-3
N, M = map(int, input().split(" "))
    for i in range(N):
        pattern = ".|."
            if i < (N-1)/2:
                print((pattern * (2*i+1)).center(M, "-"))
            elif i == (N-1)/2:
                print("WELCOME".center(M, "-"))
            else:
                print((pattern * (2*(N-1-i)+1)).center(M, "-"))
# Method -4 
def mat(x,y):
    if x>5 and x<101 and y>15 and y<303:

# Printing of the upper design before WELCOME
        #for i in range(x//2):
        q=1
        for j in range(y//2-1,0,-3): #printing of triangle
            print("-"*j,end="")
            print(".|."*q,end="") 
            q=q+2
            print("-"*j)
                
                

        print("-"*((y-7)//2),end="")
        print("WELCOME",end="")
        print("-"*((y-7)//2)) #Print the middle line first



#Printing of the lower design after WELCOME
        w=x-2
        for k in range(3,y//2,3):
            print("-"*k, end="")
            print(".|."*w , end="")
            w=w-2
            print("-"*k)
        


x, y = [int(x) for x in input().split()] 
mat(x,y)


# Method-5 
N,M= map(int,input().split())
display_string="WELCOME"

#upper half
for j in range(1,N,2):
    print("-"*int((M-(j*3))/2)+".|."*j+"-"*int((M-(j*3))/2))
    
#center
print("-"*int((M-len(display_string))/2)+display_string+"-"*int((M-len(display_string))/2))

#lower half
for j in range(N-2,0,-2):
    print("-"*int((M-(j*3))/2)+".|."*j+"-"*int((M-(j*3))/2))
