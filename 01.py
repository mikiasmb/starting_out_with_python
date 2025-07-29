moon_radius = {"Io": 1821.6, "Europa": 1560.8, "Ganymede": 2634.1, "Callisto": 2410.3}
moon_surface_gravity = {"Io": 1.796, "Europa": 1.314, "Ganymede": 1.428, "Callisto": 1.235}
moon_orbital_period = {"Io": 1.769, "Europa": 3.551, "Ganymede": 7.154, "Callisto": 16.689}

moon_name = input("Enter a moon name: ")
while moon_name not in moon_radius:
	print("Moon is not found.")
	moon_name = input("Enter a moon name: ")

print()
print(f"{moon_name} Moon radius: {moon_radius.get(moon_name, "Error")}")
print(f"{moon_name} Moon surface gravity: {moon_surface_gravity.get(moon_name, "Error")}")
print(f"{moon_name} Moon orbital period: {moon_orbital_period.get(moon_name, "Error")}")
