import asyncio

# Note 1: async def defines a coroutine function.
# Note 2: Calling this function returns a coroutine object; it does not run immediately.
# Note 3: Coroutines run when they are awaited directly or scheduled as tasks.
async def fetch_data(id: int, name: str, delay: float) -> str:
    # Note 4: This line runs immediately when the coroutine starts executing.
    print(f"Fetching data for ID {id}, Name {name}")
    # Note 5: await asyncio.sleep(delay) is non-blocking sleep.
    # Note 6: While this coroutine waits, the event loop can run other ready tasks.
    await asyncio.sleep(delay)  # Simulate a network delay
    # Note 7: This prints when the wait is finished and the coroutine resumes.
    print(f"Data fetched! for ID {id}, Name {name}")
    # Note 8: The return value is delivered to whoever awaits this task.
    return f"Sample Data for ID {id}, Name {name}"


# Note 9: main() coordinates the whole async workflow.
async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data(1, "Alice", 2))
        task2 = tg.create_task(fetch_data(2, "Bob", 3))
        task3 = tg.create_task(fetch_data(3, "Charlie", 1))
        tasks.append(task1)
        tasks.append(task2)
        tasks.append(task3)

    # Note 10: After the TaskGroup block, all tasks have completed.
    # Note 11: We can now access the results of each task.
    for i, task in enumerate(tasks, start=1):
        result = task.result()  # This is safe because the tasks are done.
        print(f"Result of Task {i}: {result}")



# Note 16: This is the script entry point for async programs.
# Note 17: asyncio.run creates an event loop, runs main(), then closes the loop.
asyncio.run(main())