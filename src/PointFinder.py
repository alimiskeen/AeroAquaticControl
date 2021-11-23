from RatioAlgorithm import RatioAlgorithm


def get_line_equation(p1, p2):
    """
    takes 2 points and generating a vector equation of a line.
    shown as (x, y, z) + t*(x_diff, y_diff, z_diff)
    :param p1: a tuple of point 1 (x, y, z)
    :param p2: a tuple of point 2 (x, y, z)
    :return: a tuple of two tuples, a point tuple and a direction tuple
    """

    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    z_diff = p2[2] - p1[2]

    #   <p2(0), p2(1), p3(2)> + t*<x_diff, y_diff, z_diff>
    return p1, (x_diff, y_diff, z_diff)


def plane_inersection(equation, plane):
    """
    finds the point where a line intersects with a plane
    :param equation: tuple of two tuples, a point tuple and a direction tuple => (x, y, z) + t*(x_diff, y_diff, z_diff)
    :param plane: a tuple representing a plane equation (l, m, n, A) => xl + my + nz = A
    :return: a tuple (x, y, z) represents a point of intersection
    """

    t_num = (plane[3] - ((plane[0] * equation[0][0]) + (plane[1] * equation[0][1]) + (plane[2] * equation[0][2])))
    t_den = ((plane[0] * equation[1][0]) + (plane[1] * equation[1][1]) + (plane[2] * equation[1][2]))
    t = t_num / t_den

    return (equation[0][0] + (equation[1][0] * t)), (equation[0][1] + (equation[1][1] * t)), \
           (equation[0][2] + (equation[1][2] * t))


if __name__ == '__main__':
    p, v = get_line_equation((1, 2, 3), (4, 5, 6))
    # print(f'({p[0]}, {p[1]}, {p[2]}) + t*({v[0]}, {v[1]}, {v[2]})')

    eq = p, v
    pl = 0, 0, 1, 0

    point = plane_inersection(eq, pl)
    # print(point)

    true_COM = 50.0, 50.0, 10.0
    wanted_COM = 40.0, 30.0, 5.0
    input_mass = 50.0  # TODO: need an algorithm to figure out how much water to add.

    p, v = get_line_equation(true_COM, wanted_COM)
    print(f'({p[0]}, {p[1]}, {p[2]}) + t*({v[0]}, {v[1]}, {v[2]})')

    int_point = plane_inersection((p, v), pl)
    print(int_point)

    algo = RatioAlgorithm(100.0, 200.0)
    mass_distribution = algo.get_ballast_mass(algo.get_ballast_ratio(int_point[0], int_point[1]), input_mass)
    print(mass_distribution[0])
    print(mass_distribution[1])


