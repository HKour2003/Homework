'''rupal has a huge collection of country stamps.she decided to count the number of distinct stamps.
Pick the stamps one by one from a stack of country stamps.find total number of distinct country stamps.
Input format: first line containd integer N,total number of stamps.next N lines contain the name of country to which stamp belong.output the total stamps in a single line'''
N = int(input("Enter the total number of stamps: "))
stamps = set()

for _ in range(N):
    stamp = input("Enter the name of the country to which the stamp belongs: ")
    stamps.add(stamp)

print("Total number of distinct country stamps:", len(stamps))
