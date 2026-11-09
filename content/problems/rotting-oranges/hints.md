Put **every** rotten orange in a queue at the start, then BFS one ring at a time. Each ring is one minute. At the end, if any orange is still fresh, return `-1`.

Re-scanning the whole grid every minute is O((rows · cols)²) when the rot has to snake a long way. BFS touches each cell once.
