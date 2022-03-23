# My PYTHON Programs

This repository contains my **PYTHON** single file
programs that I made just for fun. Fear not, it wouldn't
hurt to check them out


* ## **`encryption.py`** module
***
This module has an `Encryption` that accepts an integer
value - `seed` which is used for the encryption algorithm.
The `seed` could be different for each object but to decrypt
any message, the `seed` value used for the encryption has to
be provided. 

It's like some James Bond thing. Each agent can have an
ID like - *007/A9CD348029*; which contains the `seed` value
(e.g 48). So, whenever the agency receives a message from
and agent, only the agency will be able to decrypt it into meaningful
information since no other individual knows the agent ID.

The methods are `encrypt` and `decrypt`
```buildoutcfg
>>> jb_007 = Encryption(48)
>>> encrypted_msg = jb_007.encrypt("Hi M, it's 007. Just informing you that I will not tell you what I found.")
>>> # James Bond then sends the encrypted message to M over the Taliban network
>>> its_m_asin_MI6 = Encryption(99)

>>> decrypted_message = its_m_asin_MI6.decrypt(encrypted_msg, 48)
>>> print(decrypted_message)
Hi M, it's 007. Just informing you that I will not tell you what I found.
```

* ## `complex_numbers.py` module
***
This module has a class `Complex` which represents the
complex number system in Mathematics. It can perform
common complex number operations such as ***division,
multiplication, addition, subtraction and conjugates***.
```buildoutcfg
>>> a = Complex(3, 5)
>>> a0 = a.conjugate
>>> print(a)
<Complex `3 + 5j`>
>>> print(a0)
<Complex `3 - 5j`>
>>> b = Complex(2, 3)
>>> print(b)
<Complex `2 + 3j`>
>>> print(a + b)
<Complex `5 + 8j`>
>>> print(a - b)
<Complex `1 + 2j`>
>>> print(a * b)
<Complex `-9 + 19j`>
>>> print(a / b)
<Complex `1.6154 + 0.0769j`>
>>> print(a * a0)
<Complex `34`>
```


* ## `decimal_binary.py` module
***
This module has only 2 functions: `dec_to_bin` and
`bin_to_dec` which takes in a decimal number or binary
number and converts it to binary number or decimal
number respectively

```buildoutcfg
>>> dec_to_bin(10)
1010
>>> bin_to_dec(1010)
10
```