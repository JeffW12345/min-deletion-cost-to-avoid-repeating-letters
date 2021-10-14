def get_cost_this_cluster(indexes_with_repetition, deletion_costs):
    costs_this_repetition = []
    for index in indexes_with_repetition:
        costs_this_repetition.append(deletion_costs[index])
    # Appends the cost of all the letters in the cluster, minus the most expensive one.
    return sum(costs_this_repetition) - max(costs_this_repetition)


def get_costs(string_as_array, deletion_costs):
    index = 0
    indexes_with_repetition = set()
    costs = []
    while index < len(string_as_array) - 1:
        curr_elem = string_as_array[index]
        next_elem = string_as_array[index + 1]
        if curr_elem == next_elem:
            indexes_with_repetition.add(index)
            indexes_with_repetition.add(index + 1)
            index += 1
            # If 'next_elem' is the final element of the array
            if index == len(string_as_array) - 1:
                cost = get_cost_this_cluster(indexes_with_repetition, deletion_costs)
                costs.append(cost)
            continue
        else:
            index += 1
            if len(indexes_with_repetition) > 0:
                cost = get_cost_this_cluster(indexes_with_repetition, deletion_costs)
                costs.append(cost)
                indexes_with_repetition.clear()
    return costs


def solution(S, C):
    string = S
    deletion_costs = C
    string_as_array = list(string)
    if len(string_as_array) <= 2:
        return 0
    costs = get_costs(string_as_array, deletion_costs)  # returns an array of the cheapest cost for each cluster
    return sum(costs)


S = "aabbcc"
C = [1, 2, 1, 2, 1, 2]
print(solution(S, C)) # Expected: 3

S = "abccbd"
C = [0, 1, 2, 3, 4, 5]
print(solution(S, C)) # Expected: 2

S = "aaaa"
C = [3, 4, 5, 6]
print(solution(S, C)) # Expected: 12

S = "ababa"
C = [10, 5, 10, 5, 10]
print(solution(S, C))  # Expected: 0
