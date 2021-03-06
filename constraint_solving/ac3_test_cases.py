# Input for Exercise 14 from WS 2018/19
domains = {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9],
           'y': [1, 2, 3, 4],
           'z': [2, 4, 6]}
constraints = {('x', 'y'): [(1, 4), (2, 3), (3, 2), (4, 1)],
               ('z', 'x'): [(2, 1), (2, 2), (4, 1), (4, 2), (4, 4), (6, 1), (6, 2), (6, 3), (6, 6)],
               ('z', 'y'): [(4, 1), (6, 1), (6, 2)]
               }

# Input for Example from Lecture
domains = {'x': [0, 1, 2],
           'y': [0, 1, 2],
           'z': [0, 1, 2]}
constraints = {('x', 'y'): [(0, 1), (0, 2), (1, 2)],
               ('y', 'z'): [(0, 1), (0, 2), (1, 2)]
               }

# Input for Exercise 13 from WS 2019/20
domains = {'x': [1, 2, 3, 4, 5],
           'y': [2, 4, 6, 8, 10],
           'z': [1, 3, 5, 7, 9]}
constraints = {('x', 'y'): [(1, 8), (3, 6), (5, 4)],
               ('z', 'x'): [(1, 2), (1, 3), (1, 4), (1, 5), (3, 2),
                            (5, 2), (5, 4), (7, 2), (7, 3), (9, 2), (9, 4)],
               ('z', 'y'): [(3, 2), (5, 2), (5, 4), (7, 2), (7, 4), (7, 6), (9, 2), (9, 4), (9, 6), (9, 8)]
               }

# Input for Exam 2014/15
domains = {'x': [0, 1, 2, 3, 4],
           'y': [0, 1, 2, 3, 4],
           'z': [0, 1, 2, 3, 4]}
constraints = {('x', 'y'): [(0, 1), (0, 4), (1, 2), (3, 1), (3, 4), (4, 2)],
               ('x', 'z'): [(1, 1), (1, 4), (2, 0), (2, 3), (4, 1), (4, 4)]
               }

# Input for Exam 2015/16
domains = {'x': [-3, -2, -1, 0, 1, 2, 3],
           'y': [-3, -2, -1, 0, 1, 2, 3],
           'z': [-3, -2, -1, 0, 1, 2, 3]}
constraints = {('x', 'y'): [(-3, 2), (-2, 3)],
               ('y', 'z'): [(-3, -2), (-2, -1), (-1, 0), (0, 1), (1, 2), (2, 3)]
               }

# Input for Exam 2016/17
domains = {'x': [0, 1, 2, 3, 4],
           'y': [0, 1, 2, 3, 4],
           'z': [0, 1, 2, 3, 4]}
constraints = {('x', 'y'): [(2, 4), (3, 3), (4, 2)],
               ('y', 'z'): [(1, 2), (2, 1)]
               }

# Input for Exam 2018/19
domains = {'x': [0, 1, 2, 3],
           'y': [0, 1, 2, 3],
           'z': [3]}
constraints = {('x', 'y'): [(1,3), (2,2), (3,1)],
               ('x', 'z'): [(3,3)]
               }
