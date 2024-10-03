'''Problem 1:
Using a pseudo random number generation function (e.g., rand() in C or other
equivalent functions in other languages) that generates uniformly distributed random
numbers, generate a workload for a system that is composed of 1000 processes. You
can assume that processes arrive with an expected average arrival rate of 2 processes
per second that follows a Poisson Distribution and the service time (i.e., requested
duration on the CPU) for each process follows an Exponential Distribution with an
expected average service time of 1 second. Your outcome would be printing out a list
of tuples in the format of <process ID, arrival time, requested service time>.
You can assume that process IDs are assigned incrementally when processes arrive
and that they start at 1.
Based on your actual experiment outcome, also answer the following question: what
are the actual average arrival rate and actual average service time that were generated.

To solve this problem, you need to generate a workload of 1000 processes, with each 
process having an arrival time following a Poisson distribution and a service time 
following an Exponential distribution. Here's how you can break it down:

Approach:

Arrival Time:
Processes arrive following a Poisson distribution with an expected average arrival rate 
of 2 processes per second.
The inter-arrival time between two processes follows an exponential distribution with 
parameter λ = 2 (arrival rate of 2 processes per second).
Service Time:
The service time for each process is exponentially distributed with an expected average 
service time of 1 second (i.e., mean 1/μ=1).
Steps:
Generate 1000 processes with randomly distributed arrival times and service times.
The arrival time for process n is the sum of the inter-arrival times of the previous 
processes.
The process ID is assigned incrementally starting from 1.
Calculation of Actual Rates:
After generating the data, compute the actual average arrival rate and actual average 
service time based on the generated data.'''

import random
import math

# Number of processes
num_processes = 1000

# Arrival rate (lambda)
arrival_rate = 2  # 2 processes per second

# Service rate (mu)
service_rate = 1  # mean service time of 1 second

# Poisson random generator
def poisson_random(lmbda):
    L = math.exp(-lmbda)
    p = 1.0
    k = 0
    while p > L:
        k += 1
        p *= random.random()  # Generate a uniform random number
    return k - 1

# Exponential random generator
def exponential_random(lmbda):
    U = random.random()  # Generate a uniform random number
    return -math.log(1 - U) / lmbda

# List to store (process_id, arrival_time, service_time)
workload = []

# Generate arrival times and service times
arrival_times = []
service_times = []
current_time = 0

for i in range(1, num_processes + 1):
    # Generate inter-arrival time using exponential distribution
    inter_arrival_time = exponential_random(arrival_rate)
    current_time += inter_arrival_time  # Arrival time for the current process
    arrival_times.append(current_time)

    # Generate service time using exponential distribution
    service_time = exponential_random(service_rate)
    service_times.append(service_time)

    workload.append((i, current_time, service_time))

# Print the workload
for process in workload:
    print(f"Process ID: {process[0]}, Arrival Time: {process[1]:.4f}, Service Time: {process[2]:.4f}")

# Calculate actual average arrival rate
actual_avg_arrival_rate = num_processes / arrival_times[-1]  # Arrival rate = total processes / time of last process arrival

# Calculate actual average service time
actual_avg_service_time = sum(service_times) / num_processes  # Mean of all service times

# Print actual average arrival rate and service time
print(f"\nActual Average Arrival Rate: {actual_avg_arrival_rate:.4f} processes per second")
print(f"Actual Average Service Time: {actual_avg_service_time:.4f} seconds")

'''In this problem, we simulated a workload for a system with 1000 processes, where the arrival 
times of the processes followed a Poisson distribution with an expected average arrival rate of 
2 processes per second, and the service times followed an exponential distribution with an average 
service time of 1 second. Each process was assigned a unique ID upon arrival, and both the arrival 
times and service times were generated using a pseudo-random number generator.'''