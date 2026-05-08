# GenLayer Riddle Challenge 🧩

An AI-powered on-chain riddle game built on GenLayer for the Mini-games for GenLayer's Community mission.

## What it does
Players solve 5 GenLayer-themed riddles. The answers are judged by multiple AI validators using GenLayer's Optimistic Democracy consensus — so even creative answers can pass!

## Features
- 5 riddles all about GenLayer concepts
- AI judge powered by GenLayer's LLM consensus
- Score and attempt tracking per player
- Hall of Fame for players who solve all 5

## How to play
1. Call `get_riddle(0)` to get the first riddle
2. Call `submit_answer(your_name, 0, your_answer)` to submit
3. Keep going until you solve all 5!

## Deployed on
GenLayer Testnet Studio — studio.genlayer.com

## Built with
- GenLayer Intelligent Contracts
- Python / GenVM
- gl.nondet.exec_prompt + gl.eq_principle.prompt_comparative
