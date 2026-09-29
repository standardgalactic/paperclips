# challenge

Summary:

The "challenge" repository contains a Python script (`challenge.py`) designed to solve a coding challenge from Data Incubator. The program reads numbers from standard input, one per line, and outputs the running mean, running standard deviation, and running median for each input number. It uses only the standard library (e.g., `math`), avoiding external libraries like `numpy` or `statistics`.

The core functionality is implemented in a custom `Stats` class within `challenge.py`, which calculates these statistics incrementally as new numbers are processed. The program outputs results with reasonable precision, handling both odd and even sample counts for the median.

Key requirements include:
- Reporting estimates for all steps, including the first.
- Allowing configuration of accuracy vs. resource usage trade-offs.
- Capable of processing arbitrarily long input lists, outputting results incrementally rather than waiting for complete input.

The README specifies using either biased or unbiased standard deviation estimates and mentions handling malformed inputs gracefully. The author, Nicholas dela Fuente, submitted the solution on June 16, 2021.

KEYWORDS:
coding challenge data incubator running statistics python stats class mean std median incremental processing precision resource tradeoff malformed input handling
