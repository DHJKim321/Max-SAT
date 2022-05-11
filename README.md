This repository contains the 8/7 approximation algorithm for the NP complete MAX 3-SAT and MAX SAT problems. Although one can say that MAX SAT does
not belong to the NP class, we can rephrase the question from an optimisation problem of "Give an assignment of these clauses which satisfy at least 7/8 * m
(where m is the total number of clauses) clauses" to a decision problem "Is there an assignment of these clauses such that 7/8 of them are satisfied?".

The idea behind this algorithm is that we assign a variable to be true or false. Then, we see how many clauses this assignment has satisfied by taking the
expected number of satisfied clauses. From here, we choose the assignment which has the higher value, and we keep going until all clauses have been
satisfied.
