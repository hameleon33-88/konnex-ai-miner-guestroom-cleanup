# Guestroom Cleanup AI Miner

This repository contains a simple Robotics AI model created for the Konnex testnet.

## Task
Clean-up the guestroom:
- Collect trash
- Organize misplaced items
- Make the bed
- Verify that the room is clean

## How it works
The robot operates in a simulated guestroom environment.
It follows a rule-based decision flow and updates the environment state
after completing each action.

## File structure
- main.py — simulation entry point
- environment.py — guestroom state model
- robot.py — robot behavior logic
- requirements.txt — no external dependencies

## Run
```bash
python3 main.py
