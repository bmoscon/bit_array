# Bit Array

[![Travis CI](https://travis-ci.org/bmoscon/bit_array.svg?branch=master)](https://travis-ci.org/bmoscon/bit_array)


A simple bit array in pure python. Sample use:

```
b = BitArray(64)
b[0] = 1
b[1] = 0
```

You can also initialize with a list:

```
b = BitArray([0,1,0,1,0,1,0,1])
print(b[1])
>>> 1
```

You can also access parts of the array with slice operations:

```
sliced = b[0:4]
print(sliced[1])
>> 1
len(sliced)
>>> 4
```


