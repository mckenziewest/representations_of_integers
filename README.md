# Integers as Sums of Products of Prime Powers
An Exploration of Integers as Sums of Products of Prime Powers

In our paper, we study integers that can be represented as $p^aq^b+p^c+q^d$.

Our paper explicitly proves a limiting result on integers that can be written as
more than one disjoint representation of this form.  That is, given primes $p$ and $q$,
there are two representations of the form $p^aq^b+p^c+q^d$ that share no common summands.
We prove that if $X$ has two such representation, then either $X<M$ for some 
fixed $M$, or $M$ is in one of the following infinite families:

| p | q | X |
| :-: | :-: | :-: |
| 2 | 3 | 2<sup>a</sup>3<sup>2</sup> + 3<sup>2</sup>|
|2|3| 2<sup>a</sup>3+3<sup>2</sup>|
| 2 | 3 | 2<sup>a</sup>3<sup>2</sup> + 3|
|2|2<sup>c</sup>+1|2<sup>a</sup>+q<sup>b</sup>|
|2|2<sup>c</sup>+1| 2<sup>a</sup>q+q|
|2|2<sup>b</sup>-1|q<sup>a</sup>2<sup>b</sup>+2|
|2|2<sup>b</sup>-1|2q<sup>a</sup>+2<sup>b</sup>|
|2|2<sup>b</sup>-1|2<sup>b</sup>q<sup>a</sup>+2<sup>b</sup>|
|2|odd|2q<sup>a</sup>+2|

The content of this repository is
* `utilities.py` - This includes utility functions and objects.  Including
    * `is_prime` - A function that returns a Boolean value depending on the primality of the input.
    * `fermat_primes` - A list of the known Fermat primes.
    * `mersenne_exponents` - A list of the known values $p$ such that $2^p-1$ is prime.
* `infinite_families_with_disjoint.py` - This file is used to study the proportion of
  integers that lie in one of the families in the table above.  This includes functions
  * `all_ints_less_than` - Finds all positive integers less than the input value that are of
    one of the forms in the table above.
  * `ratio_of_ints_in_F_less_than` - Uses the above function to compute the proportion of integers 
    less than the input value that can be represented in this way.
  * `generate_plot` - Uses `ratio_of_ints_in_F_less_than` to generate a plot depicting the ratio of   integers less than `X` of the form in the table above.