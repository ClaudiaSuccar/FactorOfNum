# FactorOfNum
Checks the factors of any number between 1 and 100.

1. User is prompted to enter any number between 1 and 100.
```python
x = input('Enter a number 1-100: ')
```

2. The program iterates through the range 1-100 and checks if the modulo operator returns a 0.
```python
for num in range(1, 101):
  r = int(x) % int(num)
  if r == 0:
    print('[',num,']')
  else:
    print(num)
```    
    
3. Numbers that return 0 are factors of the input. The program returns a list of numbers between 1 and 100 and higlights factors of the the input.

_Example:_

```bash
Enter a number 1-100: 24
[ 1 ]
[ 2 ]
[ 3 ]
[ 4 ]
5
[ 6 ]
7
[ 8 ]
9
10
```
And so on...
