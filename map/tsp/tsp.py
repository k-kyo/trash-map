from itertools import product

from geopy.distance import geodesic
from mip import *


def process(points):
    if len(points) <= 1:
        return [0]

    dists = [[geodesic((a[0], a[1]), (b[0], b[1])).km for b in points[i + 1:]] for i, a in enumerate(points)]

    # number of nodes and list of vertices
    n, V = len(dists), set(range(len(dists)))

    # distances matrix
    c = [[0 if i == j
          else dists[i][j-i-1] if j > i
          else dists[j][i-j-1]
          for j in V] for i in V]

    model = Model()

    # binary variables indicating if arc (i,j) is used on the route or not
    x = [[model.add_var(var_type=BINARY) for j in V] for i in V]

    # continuous variable to prevent subtours: each city will have a
    # different sequential id in the planned route except the first one
    y = [model.add_var() for i in V]

    # objective function: minimize the distance
    model.objective = minimize(xsum(c[i][j]*x[i][j] for i in V for j in V))

    # constraint : leave each city only once
    for i in V:
        model += xsum(x[i][j] for j in V - {i}) == 1

    # constraint : enter each city only once
    for i in V:
        model += xsum(x[j][i] for j in V - {i}) == 1

    # subtour elimination
    for (i, j) in product(V - {0}, V - {0}):
        if i != j:
            model += y[i] - (n+1)*x[i][j] >= y[j]-n

    # optimizing
    model.optimize()

    # checking if a solution was found
    if model.num_solutions:
        nc = 0
        res = [nc]
        while True:
            nc = [i for i in V if x[nc][i].x >= 0.99][0]
            res.append(nc)
            if nc == 0:
                break
        return res
