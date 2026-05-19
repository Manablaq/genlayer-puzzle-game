# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import json

class GenLayerRiddleChallenge(gl.Contract):
    scores:   str
    attempts: str

    def __init__(self):
        self.scores   = "{}"
        self.attempts = "{}"

    @gl.public.view
    def get_riddle(self, index: u256) -> str:
        riddles = [
            "I am not a bank, yet I hold value. I am not a judge, yet I settle disputes. I am not a brain, yet I think with AI. I live on a blockchain but I speak plain English. What am I?",
            "Validators argue, yet they always agree. I use AI to reach my verdict but no single mind controls me. I am democratic but optimistic. What consensus mechanism am I?",
            "I am a smart contract but smarter than most. I can read the web, understand language, and think before I act. On GenLayer I am the future of on-chain logic. What am I?",
            "I run inside GenLayer. I am not a human, not a server, yet I execute Intelligent Contracts and make decisions using large language models. What am I?",
            "GenLayer was once known by another name before rebranding. Builders remember the old days. What was GenLayer previously called?"
        ]
        i = int(index)
        if i >= len(riddles):
            return "No riddle at that index. Pick between 0 and 4."
        return "RIDDLE #" + str(i + 1) + ": " + riddles[i]

    @gl.public.view
    def get_score(self, player: str) -> str:
        scores   = json.loads(self.scores)
        attempts = json.loads(self.attempts)
        score    = scores.get(player, 0)
        attempt  = attempts.get(player, 0)
        return "Player: " + player + " | Score: " + str(score) + "/5 | Attempts: " + str(attempt)

    @gl.public.view
    def get_all_scores(self) -> str:
        scores   = json.loads(self.scores)
        attempts = json.loads(self.attempts)
        if not scores:
            return "No players yet. Be the first to solve a riddle!"
        leaderboard = []
        for player, score in scores.items():
            leaderboard.append({
                "player":   player,
                "score":    score,
                "attempts": attempts.get(player, 0)
            })
        leaderboard.sort(key=lambda x: x["score"], reverse=True)
        return json.dumps(leaderboard, sort_keys=True)

    @gl.public.write
    def submit_answer(self, player: str, riddle_index: u256, player_answer: str) -> str:
        answers = [
            "intelligent contract",
            "optimistic democracy",
            "intelligent contract",
            "genvm",
            "yeagerai"
        ]
        i = int(riddle_index)
        if i >= len(answers):
            return "Invalid riddle number. Pick between 0 and 4."

        correct_answer = answers[i]

        # Track attempt — persists correctly using str + JSON
        attempts         = json.loads(self.attempts)
        attempts[player] = attempts.get(player, 0) + 1
        self.attempts    = json.dumps(attempts, sort_keys=True)

        prompt = f"""
        You are the judge of a GenLayer blockchain riddle game.
        The correct answer to the riddle is: "{correct_answer}"
        The player answered: "{player_answer}"
        Be generous — accept synonyms, partial matches, or answers that show
        the player clearly understands the concept even if worded differently.
        Reply with only YES or NO.
        """

        def get_verdict():
            result = gl.nondet.exec_prompt(prompt)
            return result

        verdict = gl.eq_principle.prompt_comparative(
            get_verdict, "The verdict must be YES or NO"
        )

        if "YES" in verdict.upper():
            # Update score — persists correctly using str + JSON
            scores         = json.loads(self.scores)
            scores[player] = scores.get(player, 0) + 1
            self.scores    = json.dumps(scores, sort_keys=True)
            current_score  = scores[player]
            if current_score == 5:
                return "LEGENDARY! You solved all 5 GenLayer riddles! Hall of Fame unlocked!"
            return "Correct! Your GenLayer knowledge is real. Score: " + str(current_score) + "/5"
        else:
            return "Not quite. Study the GenLayer docs and try again, ser."
