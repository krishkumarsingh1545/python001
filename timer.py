import time

# Record the start time
start_time = time.time()

# --- Your code or operations to be timed goes here ---
# Example: Simulate some work
time.sleep(2.444) # Pauses execution for 2.5 seconds
# --- End of code to be timed ---

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_seconds = end_time - start_time

print(f"Elapsed time: {elapsed_seconds:.2f} seconds")