# Represent each clause as a dictionary of variable and integer values.
# Positive = 1, Negative = 0, Unassigned = 2.
# literals = "~xi" where i is a positive integer and ~ represents NOT.

# Example input (for 3-CNF): x1 ~x2 ~x4

def initialiseProblem():
    clauses = []
    literals = input("Enter a clause in the form xi xj xk with ~ infront for negation: ")
    while literals.lower() != "quit":
        literals = literals.split(" ")
        clause = {}
        for literal in literals:
            clause[literal] = 2
        clauses.append(clause)
        literals = input("Enter another clause (Type quit to finish): ")
    return clauses


clauses = initialiseProblem()
print(clauses)