males = int(input("Enter the number of males registered in the class: "))
females = int(input("Enter the number of females registered in the class: "))
# calculating
total = males + females
pMales = format((males / total), '.0%')
pFemales = format((females / total), '.0%')
# displaying
print(f"Total = {total}")
print(f"Males = {pMales}")
print(f"Females = {pFemales}")