# XREP - Extended Regular Expression for POSIX, Python

## What is XREP

XREP is not for replacing your regex skills. Infact the purpose is so narrow. It CANNOT do most things. But very specific things with it's own limitations. XREP can help you to generate patterns for given string. It can generate POSIX-ERE patterns and Python patterns. With the ease of selecting the desired text.

## How XREP works

XREP does not use any libs for generating patterns. Infact it uses built-in lib like `itertools` for solving some problems. It uses `python re`while using Run-Test feature to run those patterns under the hood. But it does not help in anyways to generate the patterns. XREP is written in Python and Js. Making use of efficient conditioning, it takes any text and generate patterns using that. Later, we dive into a term (concept) we use through out called 'boundaries' to achieve better results. Overall, if you know how to regex, you can say some program to generate the same on given situations. But, XREP is very limited and for very specific things. Because, regex can get complex. We will how how XREP works behind in detail in next section.

