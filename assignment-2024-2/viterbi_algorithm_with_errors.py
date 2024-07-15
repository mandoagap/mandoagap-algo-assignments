import sys
import argparse
import math

# Function to get the data from the file
def load_file(f):
    file = open(f, 'r')
    data = file.readline()
    values = data.strip().split()
    for i in range(len(values)):
        values[i] = float(values[i])
    return values

# Viterbi algorithm to identify states
def find_states_viterbi(t, rate=2, penalty=1, debug_mode=False):
    num_points = len(t) - 1
    total_time = t[-1]
    intervals = []
    for i in range(num_points):
        intervals.append(t[i+1] - t[i])

    num_states = math.ceil(1 + math.log(total_time, rate) + math.log(1 / min(intervals), rate))
    avg_interval = total_time / num_points
    lambdas = []
    for i in range(num_states):
        lambdas.append(rate**i / avg_interval)

    cost_matrix = []
    for i in range(num_points + 1):
        cost_row = []
        for j in range(num_states):
            cost_row.append(float('inf'))
        cost_matrix.append(cost_row)
    back_pointer = []
    for i in range(num_states):
        pointer_row = []
        for j in range(num_points + 1):
            pointer_row.append(0)
        back_pointer.append(pointer_row)
    cost_matrix[0][0] = 0

    if debug_mode:
        print("Initial cost matrix:")
        for row in cost_matrix:
            print([round(x, 2) for x in row])

    for t in range(1, num_points + 1):
        for j in range(num_states):
            min_cost = float('inf')
            best_state = 0
            for l in range(num_states):
                if j > l:
                    transition_cost = cost_matrix[t-1][l] + penalty * (j - l) * math.log(num_points)
                else:
                    transition_cost = cost_matrix[t-1][l]
                if transition_cost < min_cost:
                    min_cost = transition_cost
                    best_state = l
            cost_matrix[t][j] = min_cost - math.log(lambdas[j]) + lambdas[j] * intervals[t-1]
            back_pointer[j][t] = best_state

        if debug_mode:
            print(f"Cost matrix after step {t}:")
            for row in cost_matrix:
                print([round(x, 2) for x in row])

    min_cost = float('inf')
    final_state = 0
    for j in range(num_states):
        if cost_matrix[num_points][j] < min_cost:
            min_cost = cost_matrix[num_points][j]
            final_state = j

    state_sequence = []
    t = num_points
    while t >= 0:
        state_sequence.append(final_state)
        final_state = back_pointer[final_state][t]
        t -= 1

    return state_sequence, lambdas, cost_matrix

# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    timestamps = load_file(args.file)
    states, lambdas, C = find_states_viterbi(timestamps)
    print(states)

if __name__ == "__main__":
    main()