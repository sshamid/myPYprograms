
# coding: utf-8

# In[8]:

def factorial( x ):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
        
#factorial(5)

def nonRecFact(n):
    f = 1
    for i in range(1, n+1):
        f*=i
        print f
nonRecFact(5)


# In[16]:

# prime numbers calc
n = 10
numbers = range(2, n)
results = []

while numbers != []:
    results.append(numbers[0])
    print numbers, results
    numbers = [x for x in numbers if x % numbers[0] != 0]
    print numbers, results


# In[25]:

#"fibonacci numbers": each subsequent number is the sum of the previous two
x=0
y=1
print x
print y
for i in range(10):
    x, y = y, x + y
    print y


# In[55]:

result =[]
def perm(v, k, n):
    ''' this function generates the permutations of the array
#from element k to element n-1 '''
    if(k == n):
        result.append( ''.join([x for x in v[:-2]]))
       # set(result)
    else:
#recursively explore the permutations starting at index k going through index n-1
        for i in range(k, n):
            v[k], v[i] = v[i], v[k] # swap i and k
            perm(v, k+1, n);
            v[k], v[i] = v[i], v[k] 
            ''' swap them back the way they were '''
    return set(result)
str_array = ["a", "b", "c","d"]
num_array = ["1", "2", "3","4","5"]
res = perm(num_array, 0, 5)
print len(res)
print res


# In[24]:

def get_permutations(input_string):
    ''' return all permutation of a given string'''
    permutations = []

    if len(input_string) == 1:
        permutations.append(input_string)
    else:
        previous_str = input_string[:-1]
        new_char = input_string[-1]
        previous_permutations = get_permutations(previous_str)

        for permutation in previous_permutations:
            permutation_length = len(permutation)
            i = 0

            while i <= permutation_length:
                new_permutation = permutation[:i] + new_char + permutation[i:]
                permutations.append(new_permutation)
                i += 1

    return permutations
get_permutations("abc")


# In[10]:

def perm(mylist, r, str_a, perm_a):
    if len(str_a) == r:
        return [str_a] + perm_a
    else:
        new_perm_a = perm_a
        for i in mylist:
            new_perm_a = perm(mylist, r, str_a + i, new_perm_a)
        return new_perm_a
print perm(["a","b","c"], 3, "",[])


# In[1]:

# tower of hanoi recursion problem
# count should be  2^n - 1
def t(n, beg, aux, end):
    global cnt
    if n == 1:
        print "%c --> %c\n" % (beg, end)
        cnt += 1
    else:
        t(n-1, beg, end, aux)
        t(1, beg, aux, end)
        t(n-1, aux, beg, end)
    return cnt  
cnt = 0
print t(3, 'a', 'b', 'c')


# In[ ]:




# In[5]:

sum = 0
for i in range(1,10):
    print i
    if i % 2 == 0:
        continue
    sum = sum + i	
	
print sum

