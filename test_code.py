from student_code import part_1_graph, part_2_graph, part_3_graph, part_4_graph, part_5_graph

# part 1 - list of sets
result = part_1_graph()
print("Part 1:")
print(type(result))
print(all(isinstance(item, set) for item in result))
print(len(result))
print(result)
print()

# part 2 - list of lists
result = part_2_graph()
print("Part 2:")
print(type(result))
print(all(isinstance(item, list) for item in result))
print(len(result))
print(result)
print()

# part 3 - list of dicts
result = part_3_graph()
print("Part 3:")
print(type(result))
print(all(isinstance(item, dict) for item in result))
print(len(result))
print(result)
print()

# part 4 - dict of sets
result = part_4_graph()
print("Part 4:")
print(type(result))
print(all(isinstance(value, set) for value in result.values()))
print(len(result))
print(result)
print()

# part 5 - dict of dicts
result = part_5_graph()
print("Part 5:")
print(type(result))
print(all(isinstance(value, dict) for value in result.values()))
print(len(result))
print(result)