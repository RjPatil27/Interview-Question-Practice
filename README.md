# * Interview-Question-Practice
This repo is for a practicing Interview Question and notes. 

# * BASIC UNDERSTANDING 

## COMPLEXITY

Complexity of code is depends upon many factors but for the interview perspective, we will check only input factors in the code. \
Calculate time for each statement in the code. \
For Arithmatic, Logical, Assignment, return statement takes one unit of time. 

## Calculate Running Time

Understanding by Example
Example,

```python
return a+b;
```
-->  above statement has two factors one is return and second is a+b, So both will execute one time each irrespective of input variables. \
     In this case, T(n) = 2 always which is constant function.

```python
Sum(list,len(list)):
     total = 0
     for i = 0 to len(list):
          total = total + list[i]
     return total
```
-->  In above code there are total 4 instruction statement \
     * First is **total = 0** which is assignment statement, it will run in 1 unit of time. \
     * Second is **for i = 0 to len(list):**, this instruction has two operation first is comparision and second is increment, it will run in 2 unit of time. \
       But here 2nd instruction needs to execute len(list) times, considering length is **n**, This instruction will execute in **n+1** times. \
     * Third is **total = total + list[i]**, this instuction also has two operation assignment and addition, it will run in 2 unit of time. \
       similarly this instruction will execute in n times because we are adding all the elements from list to total variable. \
     * Fourth is **return total**, this instruction will execute in 1 unit of time. 
     
   So, Total running time would be,
```python
T(n) = (1 + 2 * (n+1) + 2 * n + 1) = (2 + 2n + 2 + 2n) = (4n + 4)
    
```
     
     
   In this case, Runnig time depends upon Input.

## ASYMPTOTIC NOTATION
Types : Theta, Omega, Big-O Notation

## SPACE COMPLEXITY


# * DATA STRUCTURE AND ALGORITHM

## Array

Array declaration and operation you can perform on array.
```python
#Array declaration and operation you can perform on array
#List is mostly used in python bcoz it can store various type/datatype of variable.
#Array can store only single datatype of variable

NumberList = ["One","Two","Three","Four"]
```

Operation on Array :

1) To get an Index value 
```python
NumberList[0]

#OP -> 'One' 
```

2) To Concate or add value in array 
```python
NumberList.append("Five")

#OP -> ['One', 'Two', 'Three', 'Four', 'Five']

#extend() function is used to add multiple elements in array. It only takes one elements as input.
NumberList.extend(["Six","Seven"])      

#OP -> ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
```

3) To remove elements from array 
```python
NumberList.remove("Five")

#OP -> ['One', 'Two', 'Three', 'Four', 'Six', 'Seven']

NumberList.pop(3)

#OP -> 'Four'
```

4) To print length of array
```python
len(NumberList)

OP -> 5
```

5) Iteration
```python
for i in NumberList:
     print(i)
     
OP -> One
     Two
     Three
     Six
     Seven
```

6) To copy an array
```python
NumberList.copy()

OP -> ['One', 'Two', 'Three', 'Six', 'Seven']
```

7) To reverse the order list in array 
```python
NumberList.reverse()
print(NumberList)
OP -> ['Seven', 'Six', 'Three', 'Two', 'One']
```

8) To sort an array
```python
Number = [4,5,1,6,8]
Number.sort()
print(Number)

OP -> [1,4,5,6,8]
```

## List 

List is used to store multiple item in a single variable.
List can contain item with multiplt datatype too (string, int, boolean, float, etc).

```python
#List

ThisList = ["One","Two","Three","Four"]      #single datatype
ThisList2 = ["One",2,3,"Four",True]          #multiple datatype

```
Operation on List :

1) Length of List 
```python
print(len(ThisList))

#OP -> 4
```

2) Type 
list are defined as a object with datatype 'list'.

```python
print(type(ThisList))

#OP -> <class 'list'>
```

3) list() constructor

we can also use list() constructor to create list

```python
ThisList3 = list((1,2,3,"four"))
print(ThisList3)

#OP -> [1,2,3,"four"]
'''

```

4) Access item from list

```python
#Positive Indexing : start from the start
print(ThisList[2])

#OP -> Three

#Negative Indexing : start from the end
print(ThisList[-1])

#OP -> Four

#Accessing item using range of elements 
print(ThisList[1:3])          #start index item included and last index not.

#OP -> ["Two","Three"] 

print(ThisList[:3])           #[:3] will start from the start upto index 3 but not included.

#OP -> ["One","Two","Three"]

print(ThisList[1:])           #[1:] include elements from start given indec(included) upto last index element

#OP -> ["Two","Three","Four"]      

print(ThisList[-4:-2])        #[-4:-2]Negative Indexing : Includes First index element upto not including last index element

#OP -> ["One","Two"]

```

5) Check if Item Exists in list
