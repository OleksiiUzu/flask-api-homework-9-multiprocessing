# Flask - creating API part 8

## About

This repository is my eighth homework assignment from the Python Pro course. 

## Task:
Write a program that counts the number of lucky tickets.

A ticket consists of 6 digits (or 8 or 10 for a longer counting process).

A ticket is considered lucky when the sum of the first three digits equals the sum of the second group of three digits.

For example:

101020 - lucky because

1 + 0 + 1 == 0 + 2 + 0

546021 - not lucky because

5 + 4 + 6 != 0 + 2 + 1

Consider that ticket numbers can also be like:

000012

001099

The function must support parallelization, limited to 4 threads/processes.

## Solution:
New.py
