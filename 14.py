def main():
    print("Enter values for mass and velocity.")
    mass = float(input("Mass in kg: "))
    velocity = float(input("Velocity in m/s: "))
    print(f"Kinetic Energy - {kinetic_energy(mass, velocity):,,.2f}J")


def kinetic_energy(mass, velocity):
    ke = (.5 * mass) * (velocity ** 2)
    return ke


main()
