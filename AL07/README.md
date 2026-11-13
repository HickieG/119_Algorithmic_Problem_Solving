# AL07: Greedy Claims and Memoization Evidence

Name: Garrett Hickie
Partner(s): Elijah Ferrer
My contribution:
    Tuesday: Elijah started coding greedy change function while I compared to the demo, working together to understand the logic behind the function's flow. Then we swapped and I coded Tuesday's assertions. 

    Thursday: I started coding the calculate cached function with Elijah in the passenger. After some difficulty remembering where to enable memoization, my fire alarm went off and I left Elijah for a bit. When I returned, he started writing assertions for Thursday, having brainstormed some on his own. Then we finished our READMEs together.

## Run

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 test_assignment.py
```

The --n option is used after enabling Thursday's stage.

In my case, simply run "main.py --n 5"! Version mismatch on my end (still on python 3.12).

## Work Notes

- Payment finding: With our first two test cases (A shorter exact payment existing & Largest-first coin getting stuck), we can see that our greedy payment is not always the most efficient. In the first example, choosing the largest coin results in 3 total coins needed, whereas using the fewest would only need 2. Even worse, in the second test, being greedy fails to produce an exact payment. 
- Saved-answer finding: Uncached calls counts every time that the (uncached) Fibonacci function runs. Cached calls count every time the cached Fibonacci function is called, including hits, but it excludes recursive calls that the uncached function would perform. The 3 hits are on values already within the cache, and the 6 distinct inputs are new values added to the cache. Data is stored in the cache when a new value is found through the Fibonacci function, and it is reused when it is "hit". 
- Pair question/decision: We were trying to bring argparse over to our main file for some time before deciding together that it ran fine calling from the supplied module. Using argparse when running the file is enough. Instead, we followed "Run" instructions above with "--n 5", "--n 1", or "--n 0" to test different values.


## Assistance

Supplied files: coin_cases.py, console_style.py, investigation_display.py, investigation_support.py, and reference_solver.py
We also used the starters for main.py, test_assignment.py, and README.md

AI Use Statement: AI was used primarily for reformatting asks within the README template and helping structure our assertions. In our test_assignment.py, we tasked Copilot with structuring the starter's commented asks into separate spaced comments, then added to them after building. Towards the end of our project, Elijah and I got a bit confused by what was desired in the work notes. To combat this, we asked Copilot to rephrase the bracketed asks into full questions so we could more easily formulate a response. It helped us realize that I had already written up a concrete conceptualization that fit for saved-answer finding, and also gave us better context for what we were meant to record observations of. 

## Instructor Comments

[Reserved for instructor feedback.]
