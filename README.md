# Python WWS in venv

## Replication of Python WWS in a venv.

> ### This Repo contains the exact same files used for this test.

> ### If you do not want to use the same venv files or binaries in the repo,please clone the other? branch

<br>

## Environment

- macOS Ventura 13.1 (Intel), (Also tested on Linux)
- Python 3.10.8
- python.wasm (runtime==latest)
- Python venv initialized from running: `python -m venv`

## Issue

- When you run `wws` from a venv:
  - Mac: Memrory usage increases over time, CPU usage is high but not maxed out.
  - Linux (Not extensively tested): CPU usage is maxed out, memory increases
    over time but the pattern is unpredicatable.

## Screenshots

<img src="images/Screenshot 2023-03-01 at 9.19.32 AM.png" title="wws">
<br><br>
<img src="images/Screenshot 2023-03-01 at 9.15.17 AM.png" title="Memory Usage after ~45s" alt="Memory Usage after ~45s">
<br><br>
<img src="images/Screenshot 2023-03-01 at 9.16.45 AM.png" title="Memory Usage after ~105s" alt="Memory Usage after ~105s">
<br><br>
<img src="images/Screenshot 2023-03-01 at 9.18.01 AM.png" title="Memory Usage after ~150s" alt="Memory Usage after ~150s">
<br><br>
<img src="images/Screenshot 2023-03-01 at 9.15.38 AM.png" title="Memory Usage after ~150s" alt="Memory Usage after ~150s">
