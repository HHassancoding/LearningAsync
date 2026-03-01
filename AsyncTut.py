import asyncio

# Note 1: async def creates a coroutine function. Unlike regular functions,
# calling it doesn't execute the code immediately—it returns a coroutine object
# that must be awaited or scheduled as a task to actually run.
async def greet(name: str) -> None:
    print(f"Hello {name}")
    # Note 2: await temporarily pauses this coroutine and lets other tasks run.
    # During this 1-second sleep, another async function can execute instead of
    # blocking the entire program. This is the foundation of async concurrency.
    await asyncio.sleep(1)
    print(f"Goodbye {name}")


# Note 3: This main function is also a coroutine. It must be awaited or run using
# asyncio.run() in synchronous code. Inside, it demonstrates sequential task execution
# (awaiting each task before creating the next), which is NOT the typical concurrent pattern.
async def main(name: str):
    # Note 4: asyncio.create_task() schedules a coroutine to run on the event loop
    # and returns immediately without waiting. However, you then await it on the
    # next line, so this waits for task1 before moving to task2—no real concurrency yet!
    task1 = asyncio.create_task(greet(name))
    # Note 5: Awaiting here blocks progress until task1 completes. For true concurrency,
    # create both tasks first, then await them together using asyncio.gather() or gather all at once.
    result = await task1
    
    task2 = asyncio.create_task(greet(name))
    result2 = await task2   
    

asyncio.run(main("Alice"))


# Note 6: To run this, you'd add: asyncio.run(main("Alice"))
# asyncio.run() creates an event loop, executes the coroutine, and closes the loop.
# Currently, this code won't execute by itself—it defines the async functions but
# never calls them! Try adding asyncio.run(main("Your Name")) at the bottom.