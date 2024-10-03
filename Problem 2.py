'''Problem 2:
A computing system is composed of two servers that are mirrors of each other (for
redundancy, so if one fails, it can be restored from the other). Assume that each server
has an expected MTBF of 500 hours and its continuous uptimes (the average of which
is MTBF) follow an Exponential Distribution. Furthermore, assume that when a server
fails, it takes exactly 10 hours to restore the data from the mirror.
(a) Write a program that generates synthetic data showing the failure and restoration
times for each server over 20 years. You can assume it is always exact 24 hours per day
and exact 365 days per year. [20 pts]
(b) Find out how long it would take until the whole computing system fails (that is
when both servers happen to fail within the 10 hours restoration time; in other words,
when the two servers have any restoration time durations overlapped). You would
need to simulate this multiple times with different seeds for the rand() function (or,
equivalent uniform (pseudo)random number generating function in the programming
langue of your choice) and compute the average. [20 pts]

Part (a): Generate Synthetic Data for Failure and Restoration Times

We are tasked with generating failure and restoration times for two servers over a period 
of 20 years. The Mean Time Between Failures (MTBF) for each server is 500 hours, and the 
time between failures follows an exponential distribution. Each restoration takes exactly 
10 hours.

The total number of hours in 20 years can be calculated as:
Total hours in 20 years = 20 x 365 x 24 = 175,200 hours.
 
Steps to Implement:

For each server, generate a series of failure times based on the exponential distribution
with a mean of 500 hours.
For each failure, calculate the restoration time by adding 10 hours to the failure time.
Simulate for both servers over 20 years and print out the failure and restoration times.'''

import random
import math

# Constants
mtbf = 500  # Mean Time Between Failures (hours)
restore_time = 10  # Restoration time (hours)
years = 20
hours_per_year = 365 * 24  # Exact hours per year
total_hours = years * hours_per_year  # Total simulation time in hours

# Exponential random generator for MTBF
def exponential_random(lmbda):
    U = random.random()  # Generate a uniform random number
    return -math.log(1 - U) / lmbda

# Number of failure events to simulate (approximation)
num_failures = int(total_hours / mtbf) * 2  # Approximate number of failures per server

# Generate failure times for each server based on exponential distribution
server1_failures = []
server2_failures = []
current_time_server1 = 0
current_time_server2 = 0

for _ in range(num_failures):
    # Server 1 failure time
    current_time_server1 += exponential_random(1/mtbf)
    if current_time_server1 < total_hours:
        server1_failures.append(current_time_server1)
    
    # Server 2 failure time
    current_time_server2 += exponential_random(1/mtbf)
    if current_time_server2 < total_hours:
        server2_failures.append(current_time_server2)

# Calculate restoration times (failure time + 10 hours)
server1_restorations = [failure + restore_time for failure in server1_failures]
server2_restorations = [failure + restore_time for failure in server2_failures]

# Print failure and restoration times
print("Server 1 failures and restorations:")
for i in range(len(server1_failures)):
    print(f"Failure at {server1_failures[i]:.2f} hours, restored at {server1_restorations[i]:.2f} hours")

print("\nServer 2 failures and restorations:")
for i in range(len(server2_failures)):
    print(f"Failure at {server2_failures[i]:.2f} hours, restored at {server2_restorations[i]:.2f} hours")

'''Part (b): Simulate and Find Time Until the System Fails

We are now tasked with simulating when the entire system fails. This happens when both servers fail 
within the 10-hour restoration window.

Approach:

For each failure event of Server 1, check if any failure event from Server 2 falls within its 
restoration window, and vice versa.
If the failures overlap, the system fails. Simulate this over multiple runs to compute the average 
time until system failure.
Steps to Implement:

For each failure of Server 1, check if it overlaps with any of the restorations of Server 2.
Simulate this scenario multiple times (with different random seeds) to calculate the average time 
until the system fails.'''

# Function to simulate failure and restoration for a server
def simulate_server_failures(mtbf, total_hours):
    failures = []
    restorations = []
    current_time = 0

    while current_time < total_hours:
        # Generate the time until the next failure
        current_time += exponential_random(1/mtbf)

        if current_time < total_hours:
            failures.append(current_time)
            restorations.append(current_time + restore_time)

    return failures, restorations

# Function to check if there is an overlap between two restoration periods
def check_system_failure(server1_failures, server1_restorations, server2_failures, server2_restorations):
    for i in range(len(server1_failures)):
        for j in range(len(server2_failures)):
            # Check if server 1 fails during server 2's restoration or vice versa
            if (server1_failures[i] >= server2_failures[j] and server1_failures[i] <= server2_restorations[j]) or \
               (server2_failures[j] >= server1_failures[i] and server2_failures[j] <= server1_restorations[i]):
                return server1_failures[i]  # Return the time when the system failed
    return None  # No system failure

# Function to run the simulation multiple times and calculate the average time to system failure
def simulate_system_failures(num_simulations):
    failure_times = []

    for sim in range(num_simulations):
        # Simulate failures and restorations for both servers
        server1_failures, server1_restorations = simulate_server_failures(mtbf, total_hours)
        server2_failures, server2_restorations = simulate_server_failures(mtbf, total_hours)

        # Check when the system fails
        failure_time = check_system_failure(server1_failures, server1_restorations, server2_failures, server2_restorations)
        
        if failure_time:
            failure_times.append(failure_time)

    # Calculate the average time until system failure
    if failure_times:
        average_failure_time = sum(failure_times) / len(failure_times)
        # Display output in best format for readability
        # years output
        if average_failure_time >= hours_per_year:
            average_failure_time /= hours_per_year
            print(f"Average time until system failure: {average_failure_time:.2f} years")
        else:
            # months output
            if average_failure_time >= 24*30:
                print(f"Average time until system failure: {average_failure_time:.2f} months")
            else:
                # days output
                if average_failure_time >= 24:
                    print(f"Average time until system failure: {average_failure_time:.2f} days")
                else:
                    # hours output
                    print(f"Average time until system failure: {average_failure_time:.2f} hours")
    else:
        print("No system failures occurred during the simulation")

# Simulate system failures across multiple runs
num_simulations = 1000  # Number of simulations to run
simulate_system_failures(num_simulations)

'''Conclusion:
Part (a) generates synthetic data for the failure and restoration times of two servers over a 20-year period.
Part (b) simulates multiple scenarios to determine how long it would take for both servers to fail within the 
same 10-hour restoration window and calculates the average time until system failure based on those simulations.'''