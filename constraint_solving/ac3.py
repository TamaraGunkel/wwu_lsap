from ordered_set import OrderedSet


class AC3:

    def __init__(self, vars: list, domains: dict, constraints: dict):
        self.vars = vars
        self.domains = domains
        self.constraints = constraints

    def add_flipped_constraints(self):
        flipped_constraints = {}
        for constraint in self.constraints:
            if (constraint[1], constraint[0]) not in self.constraints:
                flipped_constraints[(constraint[1], constraint[0])] = [
                    (c[1], c[0]) for c in self.constraints[constraint]
                ]
        self.constraints.update(flipped_constraints)

    def ac3(self):
        # Initialize workpool with arcs from constraints and their counterparts
        workpool = OrderedSet()  # Use ordered set to get consistent result although it is a normal set in the algorithm
        iteration = 1
        for pair in self.constraints:
            workpool.add(pair)
            workpool.add((pair[1], pair[0]))

        while len(workpool) > 0:
            # Select any arc from workpool
            arc = workpool[0]
            workpool.remove(arc)
            if self.arc_reduce(arc):
                if len(self.domains[arc[0]]) == 0:
                    print("Failure")
                    break
                else:
                    # Check if other constraint exists where X is involved
                    for constraint in self.constraints:
                        if (constraint[0] == arc[0]) & (constraint[1] != arc[1]):
                            workpool.add((constraint[1], constraint[0]))
                            workpool.add(constraint)

                print("%-3d ##  %s  ##  %-50s  ##  %s: %s" % (
                    iteration, arc, workpool.items, arc[0], self.domains[arc[0]]))
            else:
                print("%-3d ##  %s  ##  %-50s  ##  -" % (iteration, arc, workpool.items))
            iteration += 1

    def arc_reduce(self, arc):
        change = False
        new_domain = self.domains[arc[0]].copy()
        # For each possible value in domain of X
        for value_x in self.domains[arc[0]]:
            found = False
            # For each possible value in domain of Y
            for value_y in self.domains[arc[1]]:
                # Check if all constraints are fulfilled
                if ((value_x, value_y) in self.constraints[arc]) & ((value_y, value_x) in self.constraints[
                    (arc[1], arc[0])]):
                    found = True
                    break
            if not found:
                new_domain.remove(value_x)
                change = True

        # Update domain of X
        self.domains[arc[0]] = new_domain
        return change


domains = {'x': [0, 1, 2, 3],
           'y': [0, 1, 2, 3],
           'z': [3]}
constraints = {('x', 'y'): [(1, 3), (2, 2), (3, 1)],
               ('x', 'z'): [(3, 3)]
               }

algo = AC3([], domains, constraints)
algo.add_flipped_constraints()
algo.ac3()

print("Arc consistent domains:")
print(algo.domains)
