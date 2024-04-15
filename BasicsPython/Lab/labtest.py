def calculate_waiting_time(processes):
    n = len(processes)
    total_waiting_time = 0
    waiting_time = [0] * n

    # Sort processes based on arrival time
    processes.sort(key=lambda x: x[1])

    # Initialize current time
    current_time = 0

    for i in range(n):
        waiting_time[i] = current_time - processes[i][1]
        total_waiting_time += waiting_time[i]
        current_time += processes[i][2]  # Add burst time to current time

    return total_waiting_time / n  # Return average waiting time


# List of processes: (Process ID, Arrival Time, Burst Time, Priority)
processes = [("P1", 0, 4, 2),
             ("P2", 1, 3, 3),
             ("P3", 2, 1, 4),
             ("P4", 3, 5, 5),
             ("P5", 4, 2, 5)]

# Calculate average waiting time
average_waiting_time = calculate_waiting_time(processes)

# Print the result
print("Average Waiting Time:", average_waiting_time)