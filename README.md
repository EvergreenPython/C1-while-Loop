## while loop

Repeats a set of statements as long as a condition is True.

### Formula
``` python
while (Condition):
	Body

else:			<----- Optional
	Body
```

*Ex.*
```python
while (True):
	print ("This statement prints forever.")
```

### Rule
A loop becomes infinite loop if a condition never becomes FALSE. 
An infinite loop might be useful in client/server programming where the server needs to run continuously.

However, you must use caution when using while loops because of the possibility that this condition never resolves to a FALSE value.
To avoid a infinite loop, make sure to use a variable and keep track of its value.

*Ex.*
```python
counter = 0

while counter < 3:
    print("Inside loop")
    counter += 1	# Equivalent to counter = count + 1
else:
    print("Inside else")
```
> Inside loop
> Inside loop
> Inside loop
> Inside else