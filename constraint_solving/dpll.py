# adapted from https://gist.github.com/davefernig/e670bda722d558817f2ba0e90ebce66f

import random

dpll_result = []


def pretty_print_formula(cnf):
    result = []
    for dnf in cnf:
        sub_result = "("
        for var in dnf:
            if not var[1]:
                sub_result += "!"
            sub_result += var[0] + " V "
        result.append(sub_result[0: len(sub_result) - 3] + ")")

    print(' /\\ '.join(result))


def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]


def is_pure_literal(cnf, literal):
    exists_true = False
    exists_false = False
    for dnf in cnf:
        if (literal, True) in dnf:
            exists_true = True
        if (literal, False) in dnf:
            exists_false = True
    return (not (exists_false & exists_true), exists_true)


def dpll(cnf, assignments={}):
    if len(cnf) == 0:
        print("True")
        dpll_result.append(assignments)
        return

    l = __select_literal(cnf)

    is_pure, is_true = is_pure_literal(cnf, l)
    if is_pure:
        # Eliminate if pure
        if is_true:
            new_cnf = [c for c in cnf if (l, True) not in c]
        else:
            new_cnf = [c for c in cnf if (l, False) not in c]
        print("Eliminate pure literal " + l + " by setting it to " + str(is_true))
        if(len(new_cnf) > 0):
            pretty_print_formula(new_cnf)
        dpll(new_cnf, {**assignments, **{l: is_true}})

    else:
        # Unit-propagate
        print("Choose: " + l + ", consider true")
        new_cnf = [c.copy() for c in cnf if (l, True) not in c]
        negated_element = (l, False)
        skip = False
        for c in new_cnf:
            if negated_element in c:
                if len(c) > 1:
                    c.remove(negated_element)
                else:
                    # Only element in DNF -> CNF is false
                    print("False")
                    skip = True
        if not skip:
            pretty_print_formula(new_cnf)
            dpll(new_cnf, {**assignments, **{l: True}})

        print("Choose: " + l + ", consider false")
        skip = False
        new_cnf = [c.copy() for c in cnf if (l, False) not in c]
        negated_element = (l, True)
        for c in new_cnf:
            if negated_element in c:
                if len(c) > 1:
                    c.remove(negated_element)
                else:
                    # Only element in DNF -> CNF is false
                    print("False")
                    skip = True
        if not skip:
            pretty_print_formula(new_cnf)
            dpll(new_cnf, {**assignments, **{l: False}})


def random_kcnf(n_literals, n_conjuncts, k=3):
    result = []
    for _ in range(n_conjuncts):
        conj = set()
        for _ in range(k):
            index = random.randint(0, n_literals)
            conj.add((
                str(index).rjust(10, '0'),
                bool(random.randint(0, 2)),
            ))
        result.append(conj)
    return result


# Create forumla
x = ("x", True)
not_x = ("x", False)
y = ("y", True)
not_y = ("y", False)
z = ("z", True)
not_z = ("z", False)
w = ("w", True)
not_w = ("w", False)

# DNF subformulas
f1 = [x, y, z]
f2 = [y, not_z, w]
f3 = [not_x, not_y, z]
f4 = [not_x, not_y, not_z]
f5 = [not_w]

# Complete CNF formula
f = [f1, f2, f3, f4, f5]
pretty_print_formula(f)

dpll(f)
print(dpll_result)
