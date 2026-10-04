import time
import threading

# Simulate a computationally intensive task
def intensive_task(iterations):
    start_time = time.time()
    result = 0
    for i in range(iterations):
        result += i * i  # A simple, CPU-bound operation
    end_time = time.time()
    print(f"Intensive task completed in {end_time - start_time:.4f} seconds.")
    return result

# Simulate a UI update task
def ui_update_task(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        # In a real app, this would involve updating UI elements
        pass
    print(f"UI update simulation finished after {duration:.2f} seconds.")

print("--- Native Performance Simulation ---")

# In a native app, these tasks can run truly in parallel or with high priority
# We simulate this by running them concurrently without significant blocking

# Task 1: Heavy computation
thread1 = threading.Thread(target=intensive_task, args=(10_000_000,))
thread1.start()

# Task 2: UI update simulation (simulating responsiveness)
thread2 = threading.Thread(target=ui_update_task, args=(0.5,))
thread2.start()

thread1.join()
thread2.join()

print("\n--- React Native Simulation (Conceptual) ---")
print("In React Native, heavy computation on the JS thread can block UI updates.")
print("This simulation shows how a long-running JS task might impact UI responsiveness.")

# Simulate a scenario where a long JS task blocks the main thread
print("Starting long JS task...")
# This call would block the 'main' thread (simulating JS thread)
intensive_task(10_000_000)
print("JS task finished.")

# If the UI update was attempted *during* the above task, it would be delayed.
# For demonstration, we show it after, but the point is the delay.
print("Attempting UI update *after* JS task.")
ui_update_task(0.5)

print("\n--- Comparison Notes ---")
print("Native apps can leverage separate threads for CPU-bound work and the main thread for UI, ensuring smooth performance.")
print("React Native, while efficient, might require careful management of background threads for intensive tasks to avoid UI freezes.")
