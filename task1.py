# Note 1: asyncio is Python's standard library for async/await programming.
# Note 2: It provides the event loop, coroutines, tasks, and utilities for concurrent I/O.
import asyncio
# Note 3: time.perf_counter() measures high-resolution elapsed time.
# Note 4: We use it to measure how long concurrent vs sequential execution takes.
import time

# Note 5: URLS is a list of endpoints to fetch (simulated with sleep delays).
URLS = [
    "https://example.com/api/data1",
    "https://example.com/api/data2",
    "https://example.com/api/data3",
]
# Note 6: DELAYS pairs with URLS: each URL has a corresponding wait time in seconds.
# Note 7: Using zip(URLS, DELAYS) pairs them: (url1, 2.0), (url2, 3.0), (url3, 1.0).
DELAYS = [2.0, 3.0, 1.0]

# Note 8: download() is a coroutine that simulates fetching data from a URL.
# Note 9: The delay parameter mimics real network latency.
async def download(url: str, delay: float) -> str:
    # Note 10: perf_counter() records the start time in seconds (high precision).
    start = time.perf_counter()
    print(f"[{start:.2f}] START {url}")
    # Note 11: await asyncio.sleep(delay) pauses THIS coroutine for 'delay' seconds.
    # Note 12: While paused, OTHER tasks can run. This is how concurrency works.
    await asyncio.sleep(delay)
    # Note 13: After the wait, this code resumes immediately (no additional time).
    end = time.perf_counter()
    print(f"[{end:.2f}] END   {url}")
    # Note 14: The return value is wrapped and delivered to whoever awaits this task.
    return f"data from {url}"

# Note 15: concurrent_main() demonstrates concurrent execution.
# Note 16: All tasks start together and overlap their wait times.
async def concurrent_main():
    # Note 17: Record start time to measure total elapsed time.
    start = time.perf_counter()
    # Note 18: TaskGroup automatically awaits all tasks when the 'async with' block exits.
    # Note 19: If any task raises an exception, all others are cancelled immediately.
    async with asyncio.TaskGroup() as tg:
        # Note 20: List comprehension creates one task for each (url, delay) pair.
        # Note 21: zip(URLS, DELAYS) pairs them: url1 with 2.0, url2 with 3.0, url3 with 1.0
        # Note 22: All tasks are created FIRST, so they start at nearly the same time.
        tasks = [
            tg.create_task(download(url, delay))
            for url, delay in zip(URLS, DELAYS)
        ]
    # Note 23: By this point, the TaskGroup has auto-awaited all tasks. They are all done.
    # Note 24: Total time is ~max(2.0, 3.0, 1.0) = 3.0 seconds, NOT 2.0+3.0+1.0 = 6.0 seconds.
    end = time.perf_counter()
    print(f"Concurrent total: {end - start:.2f} seconds")
    # Note 25: Now we can safely call task.result() without awaiting (tasks are already done).
    for t in tasks:
        print("Result:", t.result())

# Note 26: sequential_main() demonstrates sequential execution (no concurrency).
# Note 27: Tasks run one after another, waiting for each to complete before starting the next.
async def sequential_main():
    # Note 28: Record start time to compare against concurrent_main().
    start = time.perf_counter()
    # Note 29: Loop through each URL and delay pair.
    for url, delay in zip(URLS, DELAYS):
        # Note 30: await download() waits for THIS task to finish completely.
        # Note 31: The next loop iteration doesn't start until this await returns.
        # Note 32: No other tasks run during the wait (no overlap, no concurrency).
        result = await download(url, delay)
        print("Result:", result)
    # Note 33: Total time is sum of all delays: 2.0 + 3.0 + 1.0 = 6.0 seconds.
    end = time.perf_counter()
    print(f"Sequential total: {end - start:.2f} seconds")

# Note 34: This is the script entry point (only runs when executed directly, not when imported).
if __name__ == "__main__":
    # Note 35: asyncio.run() creates a new event loop, runs the coroutine, then closes the loop.
    # Note 36: concurrent_main() should complete in ~3 seconds (longest individual delay).
    asyncio.run(concurrent_main())
    # Note 37: Separator for readability when comparing outputs.
    print("-" * 40)
    # Note 38: sequential_main() should complete in ~6 seconds (sum of all delays).
    # Note 39: Comparing these two shows the benefit of concurrency: 3s vs 6s for the same work.
    asyncio.run(sequential_main())
