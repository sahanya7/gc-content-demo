# Live demo script (for the presenter, not the audience)

## Before class
1. Create a new public repo on GitHub called `gc-content-demo`.
2. Upload every file in this folder, including the hidden `.github` folder
   (easiest: drag the folder into GitHub Desktop, or use `git push`).
3. In README.md, replace YOUR-USERNAME with your GitHub username.
4. Open the Actions tab and confirm the first run is green.
5. Screen-record one green run and one red run as a backup in case of bad Wi-Fi.
6. Open these tabs in advance: the repo, the Actions tab, and fasta_stats.py.

## Demo 1: the green run (about 2 min)
1. Show `fasta_stats.py` and say what it does: GC content of DNA sequences.
2. Make a harmless edit on GitHub (e.g. add a comment line) and commit.
3. Switch to the Actions tab: a new run appears within seconds.
4. Click into it: point out the 3 parallel jobs (the matrix: 3 Python versions).
5. Click one job and expand the steps: they run in order, matching the diagram.
6. Everything turns green. Point at the badge on the README.

## Demo 2: the red run (about 2 min)
1. In `fasta_stats.py`, "accidentally" break the GC calculation. Change
       gc = sequence.upper().count("G") + sequence.upper().count("C")
   to
       gc = sequence.upper().count("G")
2. Commit with a message like "small cleanup".
3. Watch the Actions tab: the run fails with a red X.
4. Open the failed "Run the tests" step and show the log: pytest says exactly
   which test failed and what it expected (100.0) vs. got (50.0).
5. Key line for the audience: "Without this, I might have published results
   with the wrong GC content and never known. This is reproducibility on autopilot."
6. Undo the change, commit, and show it go green again.

## Closing
Show a QR code linking to the repo so classmates can copy the workflow file.
