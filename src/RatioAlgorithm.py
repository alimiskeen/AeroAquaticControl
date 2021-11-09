class RatioAlgorithm:

    def __init__(self, x_constant, y_constant):
        self.x_const = x_constant
        self.y_const = y_constant

    def get_ballast_ratio(self, desired_x: float, desired_y: float):
        rx2 = desired_x / self.x_const
        rx1 = (self.x_const - desired_x) / self.x_const

        ry2 = desired_y / self.y_const
        ry1 = (self.y_const - desired_y) / self.y_const

        rr = [[rx1 * ry1, rx2 * ry1],
              [rx1 * ry2, rx2 * ry2]]

        return rr

    def get_ballast_mass(self, ratio_matrix, mass: float):
        mm = [[0.0, 0.0],
              [0.0, 0.0]]

        for x in range(2):
            for y in range(2):
                temp = (ratio_matrix[x][y] * mass)
                mm[x][y] = temp

        return mm

    def get_ballast_volumes(self, mass_matrix):
        vv = [[0.0, 0.0],
              [0.0, 0.0]]

        for x in range(2):
            for y in range(2):
                temp = mass_matrix[x][y] / 0.9998395
                vv[x][y] = temp

        return vv

    def get_COM(self, mass_matrix):
        total_mass = 0.0
        for x in range(2):
            for y in range(2):
                total_mass = total_mass + mass_matrix[x][y]

        x_COM = ((self.x_const * mass_matrix[0][1]) + (self.x_const * mass_matrix[1][1])) / total_mass
        y_COM = ((self.y_const * mass_matrix[1][0]) + (self.y_const * mass_matrix[1][1])) / total_mass

        return x_COM, y_COM

    def get_all(self, desired_x: float, desired_y: float, mass: float):
        return self.get_ballast_volumes(self.get_ballast_mass(self.get_ballast_ratio(desired_x, desired_y), mass))

if __name__ == '__main__':
    algo = RatioAlgorithm(10.0, 20.0)

    print(algo.x_const, algo.y_const, sep='-')
    ratios = algo.get_ballast_ratio(2.5, 10.5)
    masses = algo.get_ballast_mass(ratios, 55.9)
    print(masses)
    volumes = algo.get_ballast_volumes(masses)
    print(volumes)

    print(algo.get_COM(masses))

    print("get all: ", algo.get_all(2.5, 10.5, 55.9))