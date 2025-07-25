import timeit
big_list = list(range(50000))
big_set = set(big_list)
big_list.insert(24033, "target")
big_set.add("target")

list_time = timeit.timeit(lambda: "target" in big_list, number=1000)
set_time = timeit.timeit(lambda: "target" in big_set, number=1000)

print(f"List membership: {list_time*1000:.2f} ms")
print(f"Set membership: {set_time*1000:.2f} ms")