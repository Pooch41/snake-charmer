website_visitors = [524, 335, 306, 28, 42, 181, 463, 45, 45, 524, 28, 42]

unique_visitors = set(website_visitors) # change this line

print(unique_visitors)

print("-" * 100)

main_person = {"football", "wine", "reading", "travel", "swimming", "golf", "fashion", "long term dating"}
option_1 = {"movies", "math", "netflix", "short term dating", "fashion", "wine", "golf", }
option_2 = {"travel", "long term dating", "golf", "fashion"}

shared_interests_with_option_1 = main_person.intersection(option_1) # change this line
print(shared_interests_with_option_1)

shared_interests_with_option_2 = main_person.intersection(option_2) # change this line
print(shared_interests_with_option_2)

if len(shared_interests_with_option_1) > len(shared_interests_with_option_2):
   print ("Option 1 is the best match")
elif len(shared_interests_with_option_1) < len(shared_interests_with_option_2):
   print ("Option 2 is the best match")
else:
   print ("Both options are equally good")

print("-" * 100)

poll_a = ["Maxwell Sterling", "Maxwell Sterling", "Harriet Vane", "Leonora Quint", "Harriet Vane", "Maxwell Sterling"]
poll_b = ["Harriet Vane", "Vincent Thorne", "Harriet Vane", "Selina Morrow", "Harriet Vane", "Harriet Vane"]
poll_c = ["Selina Morrow", "Jasper Creed", "Selina Morrow", "Jasper Creed", "Selina Morrow", "Maxwell Sterling"]

unique_nominations = set(poll_a) | set(poll_b) | set(poll_c) # change this line

print(unique_nominations)


