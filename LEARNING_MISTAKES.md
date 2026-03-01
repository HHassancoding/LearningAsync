# Learning Mistakes and Reminders

This file tracks repeated mistakes and what to check before doing similar tasks.

## Mistake Log

### Entry 1
- Date: 2026-03-01
- Topic: Python async execution entry point
- Mistake: Defining async functions but not running them from script entry.
- Correct Understanding: async functions do nothing until awaited or run via asyncio.run.
- Remember Rule: If this is a runnable script, include one clear entry point.
- Self-Check: Can I point to the exact line that starts program execution?

### Entry 2
- Date: 2026-03-01
- Topic: Async task timing and completion order
- Mistake: Mixing up await order with finish order of tasks.
- Correct Understanding: Finish order depends on delay/work duration, not await sequence.
- Remember Rule: Create tasks first, then reason by each task's wait time.
- Self-Check: Which task has the shortest delay, and which has the longest?

### Entry 3
- Date: 2026-03-01
- Topic: Duplicate flow definitions
- Mistake: Defining main twice and running asyncio.run(main()) twice.
- Correct Understanding: Keep one main and one script entry call unless intentional.
- Remember Rule: One lesson script should usually have a single orchestration path.
- Self-Check: Search for duplicate def main and duplicate asyncio.run.

## Before Similar Tasks (Quick Checklist)

- Confirm there is exactly one intended script entry point.
- Verify async functions are awaited or scheduled as tasks.
- Separate "start order" from "finish order" when explaining flow.
- Estimate runtime using longest overlapping wait, not sum of waits.
- Check for duplicate main definitions or duplicate run calls.
