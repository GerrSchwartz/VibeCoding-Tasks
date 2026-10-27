capsules_made = int(input('input number of capsules made '))
package_capacity = int(input('input package capacity '))

full_packages = capsules_made // package_capacity
leftover_capsules = capsules_made % package_capacity

print(f'\n--Package report---\nFull packages:\t\t{full_packages}\nLeftover capsules:\t{leftover_capsules}')