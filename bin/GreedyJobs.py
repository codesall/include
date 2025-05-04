# Define a Job class
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id          # Job ID
        self.deadline = deadline  # Deadline (in time units)
        self.profit = profit      # Profit if job is done before or on deadline

# Greedy Job Scheduling Function
def job_scheduling(jobs):
    # Sort jobs by descending profit (Greedy strategy)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)  # Max deadline determines time slots
    slots = [None] * n  # Initialize time slots
    total_profit = 0

    for job in jobs:
        # Try to schedule job in the latest free slot before its deadline
        for i in range(min(n, job.deadline) - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job.id
                total_profit += job.profit
                break

    # Filter out None and return scheduled job order and total profit
    scheduled_jobs = [job_id for job_id in slots if job_id is not None]
    return scheduled_jobs, total_profit

# Example usage
jobs = [
    Job('J1', 2, 100),
    Job('J2', 1, 19),
    Job('J3', 2, 27),
    Job('J4', 1, 25),
    Job('J5', 3, 15)
]

scheduled, profit = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled)
print("Total Profit:", profit)
