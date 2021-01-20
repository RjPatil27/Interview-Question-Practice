# * Interview-Question-Practice
This repo is for practicing Interview Question and notes. 

# * BASIC UNDERSTANDING 

## COMPLEXITY

Complexity of code is depends upon many factors but for interview perspective, we will check only input factors in code. \
Calculate time for each statement in code. \
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
     ```
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

OP -> ['One', 'Two', 'Three', 'Four', 'Five']

#extend() function is used to add multiple elements in array. It only takes one elements as input.
NumberList.extend(["Six","Seven"])      

OP -> ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
```

3) 
