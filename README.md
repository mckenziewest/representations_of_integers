# Integers as Sums of Products of Prime Powers
An Exploration of Integers as Sums of Products of Prime Powers

In our paper, we study integers that can be represented as $p^aq^b+p^c+q^d$.

Our paper explicitly proves a limiting result on integers that can be written as
more than one disjoint representation of this form.  That is, given primes $p$ and $q$,
there are two representations of the form $p^aq^b+p^c+q^d$ that share no common summands.

The content of this repository is
* `utilities.py` - This includes utility functions and objects.  Including
    * `is_prime` - A function that returns a boolean value depending on the primality of the input.
    * `fermat_primes` - A list of the known Fermat primes.
    * `mersenne_exponents` - A list of the known values $p$ such that $2^p-1$ is prime.