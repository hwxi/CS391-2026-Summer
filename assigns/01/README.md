# Assignment 1 for CS391X1, Summer I, 2025

## Total points: 120

## Description of the tasks

### Task 0: Setting up (20 points)

Please create a PRIVATE github repository of the name
CS391-2026-Summer-??????, where ??????  is your BU email ID.
For instance, my BU email ID is hwxi.

### Task 1: Lambda-calculus (50 points)

Please write a short report on lambda-calculus.
Your report should contain the following basics:

1: Definition of pure lambda-terms, that is, the
terms in Church's lambda-calculus, which often referred
to as the pure lambda-calculus.

2: What is a freen variable (in a lambda-term)? What is a
bound variable?

3: What is alpha-equivalence? What is alpha-renaming?
Please give some examples for the purpose of illustration.

4. What is substitution (in lambda-calculus)? What is capturing
(of free variables)? Please give an example illustrating capturing.

### Task 2: Implementation (50 points)

Please first study the following code:

- lectures/lecture-05-20: substitution in ML-like syntax
- lectures/lecture-05-20: substitution implemented in Python 3

Then implement in Python the following function:

fun
term_subst1
(tm0: term, tx1: strn, sub: term): term

Basically,

term_subst1(tm0, tx1, sub) = tm0[tx1 -> sub], which refers to
the result from substituting 'sub' for 'tx1' in 'tm0'. In this
case, 'sub' may contain free variables. Hence, you have to address
the issue of capturing of free variables.

## Summary

You are expected to have all of your submitted code in one file of the
name `assign01.py`; this file should be stored in the directory
`assigns/01/MySolution`. Please visit the following page for
information on creating a private repository of your own for this
class:

```
https://github.com/hwxi/CS391-2026-Summer/blob/main/README.md
```
