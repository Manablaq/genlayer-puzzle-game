# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import json

# ── BUILT-IN QUESTION BANK (15 questions) ──────────────────────────────────────

QUESTIONS = [
    {
        "riddle": "I am not a bank, yet I hold value. I am not a judge, yet I settle disputes. I am not a brain, yet I think with AI. I live on a blockchain but I speak plain English. What am I?",
        "options": {"A": "Smart Oracle", "B": "Intelligent Contract", "C": "Decentralized Exchange", "D": "Blockchain Wallet"},
        "letter": "B", "answer": "intelligent contract", "author": "system"
    },
    {
        "riddle": "Validators argue, yet they always agree. I use AI to reach my verdict but no single mind controls me. I am democratic but optimistic. What consensus mechanism am I?",
        "options": {"A": "Proof of Work", "B": "Delegated Proof of Stake", "C": "Optimistic Democracy", "D": "Byzantine Fault Tolerance"},
        "letter": "C", "answer": "optimistic democracy", "author": "system"
    },
    {
        "riddle": "I am a smart contract but smarter than most. I can read the web, understand language, and think before I act. On GenLayer I am the future of on-chain logic. What am I?",
        "options": {"A": "ERC-20 Token", "B": "DAO Contract", "C": "Intelligent Contract", "D": "Oracle Node"},
        "letter": "C", "answer": "intelligent contract", "author": "system"
    },
    {
        "riddle": "I run inside GenLayer. I am not a human, not a server, yet I execute Intelligent Contracts and make decisions using large language models. What am I?",
        "options": {"A": "Ethereum VM", "B": "WebAssembly Runtime", "C": "Python Interpreter", "D": "GenVM"},
        "letter": "D", "answer": "genvm", "author": "system"
    },
    {
        "riddle": "GenLayer was once known by another name before rebranding. Builders remember the old days. What was GenLayer previously called?",
        "options": {"A": "ChainAI", "B": "YeagerAI", "C": "SmartLayer", "D": "LayerZero"},
        "letter": "B", "answer": "yeagerai", "author": "system"
    },
    {
        "riddle": "I am where GenLayer developers write, test, and deploy Intelligent Contracts directly in their browser. No setup required. What am I?",
        "options": {"A": "GenLayer Explorer", "B": "GenLayer Wallet", "C": "GenLayer Studio", "D": "Remix IDE"},
        "letter": "C", "answer": "genlayer studio", "author": "system"
    },
    {
        "riddle": "On GenLayer, I am connected to an LLM. I run contracts independently, check results, and must agree with others before anything finalizes on-chain. What am I?",
        "options": {"A": "Smart Node", "B": "Validator", "C": "Oracle", "D": "Miner"},
        "letter": "B", "answer": "validator", "author": "system"
    },
    {
        "riddle": "GenLayer contracts are written in me. I am not Solidity. I am human-readable, widely used, and powerful enough to think with AI. What programming language am I?",
        "options": {"A": "JavaScript", "B": "Rust", "C": "Python", "D": "Vyper"},
        "letter": "C", "answer": "python", "author": "system"
    },
    {
        "riddle": "I am the GenLayer function that fetches live data from any public URL. Unlike my broken cousin web.get(), I actually return content validators can read. What function am I?",
        "options": {"A": "web.get()", "B": "web.render()", "C": "web.fetch()", "D": "web.call()"},
        "letter": "B", "answer": "web.render", "author": "system"
    },
    {
        "riddle": "I am the GenLayer function that runs your fetch logic across all validators and uses AI to check they all got the same answer. Consensus lives inside me. What function am I?",
        "options": {"A": "exec_prompt()", "B": "run_nondet_unsafe()", "C": "prompt_comparative()", "D": "validate_result()"},
        "letter": "C", "answer": "prompt_comparative", "author": "system"
    },
    {
        "riddle": "In GenLayer, I am where all contracts live before mainnet. Real validators, real consensus, no real money. What am I?",
        "options": {"A": "Sandbox", "B": "Devnet", "C": "Testnet", "D": "Stagenet"},
        "letter": "C", "answer": "testnet", "author": "system"
    },
    {
        "riddle": "On GenLayer, I am the validator chosen to propose the result first in a consensus round. Others verify my work. If they agree, the transaction finalizes. What role am I?",
        "options": {"A": "Master Node", "B": "Proposer", "C": "Leader", "D": "Sequencer"},
        "letter": "C", "answer": "leader", "author": "system"
    },
    {
        "riddle": "I am the blockchain GenLayer builds on for Ethereum-level security and ZK-powered settlement. Which network am I?",
        "options": {"A": "Polygon", "B": "Arbitrum", "C": "Optimism", "D": "ZKsync"},
        "letter": "D", "answer": "zksync", "author": "system"
    },
    {
        "riddle": "I am the native unsigned integer type in GenLayer Intelligent Contracts — 256 bits, same as Ethereum. What type am I?",
        "options": {"A": "uint256", "B": "u256", "C": "BigInt", "D": "UInt"},
        "letter": "B", "answer": "u256", "author": "system"
    },
    {
        "riddle": "I look like a dictionary and store key-value pairs in GenLayer contracts. But beware — I do NOT persist between transactions on Studio. What storage type am I?",
        "options": {"A": "HashMap", "B": "Dict", "C": "TreeMap", "D": "StateMap"},
        "letter": "C", "answer": "treemap", "author": "system"
    },
]

# ── HELPERS ────────────────────────────────────────────────────────────────────

def _shuffle(seed_str: str, total: int, pick: int) -> list:
    seed = 0
    for c in seed_str.replace("0x", "").replace("0X", ""):
        seed = seed * 31 + ord(c)
    indices = list(range(total))
    for i in range(len(indices) - 1, 0, -1):
        seed = (seed * 1103515245 + 12345) & 0x7fffffff
        j = seed % (i + 1)
        indices[i], indices[j] = indices[j], indices[i]
    return indices[:pick]

def _make_room_code(host: str) -> str:
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    seed = 0
    for c in host.replace("0x", "").replace("0X", ""):
        seed = seed * 31 + ord(c)
    code = ""
    for _ in range(6):
        seed = (seed * 1103515245 + 12345) & 0x7fffffff
        code += chars[seed % len(chars)]
    return code

def _format_riddle(q: dict, label: str, q_index: int, pos: int) -> str:
    author_tag = ""
    if q.get("author", "system") != "system":
        author_tag = "  [Custom riddle by " + q["author"][:8] + "...]\n"
    return (
        label + " | QUESTION " + str(pos + 1) + " of 5  (ID:" + str(q_index) + ")\n"
        + author_tag + "\n"
        + q["riddle"] + "\n\n"
        + "A.  " + q["options"]["A"] + "\n"
        + "B.  " + q["options"]["B"] + "\n"
        + "C.  " + q["options"]["C"] + "\n"
        + "D.  " + q["options"]["D"] + "\n\n"
        + "Reply with A, B, C or D — or type your full answer."
    )

def _all_questions(custom_bank: list) -> list:
    """Merge built-in questions with custom questions."""
    return QUESTIONS + custom_bank


# ── CONTRACT ────────────────────────────────────────────────────────────────────

class GenLayerRiddleChallenge(gl.Contract):
    scores:        str   # global leaderboard  {player: score}
    attempts:      str   # global attempts     {player: count}
    rooms:         str   # rooms {code: {host, players[], room_scores{}, active, custom_only}}
    custom_riddles: str  # community riddles [{riddle, options, letter, answer, author}]

    def __init__(self):
        self.scores         = "{}"
        self.attempts       = "{}"
        self.rooms          = "{}"
        self.custom_riddles = "[]"

    # ── READ METHODS ───────────────────────────────────────────────────────────

    @gl.public.view
    def get_riddle(self, index: u256) -> str:
        """Get any built-in riddle by index (0 to 14)."""
        i = int(index)
        if i >= len(QUESTIONS):
            return "Built-in questions: 0 to " + str(len(QUESTIONS) - 1) + "."
        return _format_riddle(QUESTIONS[i], "BUILT-IN", i, i)

    @gl.public.view
    def get_custom_riddle(self, index: u256) -> str:
        """Get a community-created riddle by index."""
        custom = json.loads(self.custom_riddles)
        i = int(index)
        if i >= len(custom):
            return "Custom question index out of range. Total custom: " + str(len(custom))
        return _format_riddle(custom[i], "CUSTOM", len(QUESTIONS) + i, i)

    @gl.public.view
    def get_my_riddle(self, player: str, position: u256) -> str:
        """Get your personal shuffled riddle (0-4). Picks from all questions including custom."""
        custom  = json.loads(self.custom_riddles)
        all_q   = _all_questions(custom)
        order   = _shuffle(player, len(all_q), 5)
        pos     = int(position)
        if pos >= 5:
            return "Position must be 0 to 4."
        q_index = order[pos]
        return _format_riddle(all_q[q_index], "YOUR SESSION", q_index, pos)

    @gl.public.view
    def get_room_riddle(self, player: str, room_code: str, position: u256) -> str:
        """Get your shuffled riddle inside a room (0-4)."""
        rooms = json.loads(self.rooms)
        if room_code not in rooms:
            return "Room " + room_code + " not found."
        room = rooms[room_code]
        if player not in room["players"]:
            return "You are not in room " + room_code + ". Call join_room first."
        custom = json.loads(self.custom_riddles)

        # If room is custom-only, use only the room's pinned custom questions
        if room.get("custom_only") == "true" and room.get("custom_ids"):
            custom_ids = room["custom_ids"]
            all_q      = _all_questions(custom)
            pool       = [all_q[idx] for idx in custom_ids if idx < len(all_q)]
            if len(pool) < 5:
                pool = _all_questions(custom)
            order   = _shuffle(player + room_code, len(pool), min(5, len(pool)))
            pos     = int(position)
            if pos >= len(order):
                return "Position out of range for this room's question set."
            q_local = order[pos]
            actual_index = custom_ids[q_local] if q_local < len(custom_ids) else q_local
            return _format_riddle(pool[q_local], "ROOM " + room_code, actual_index, pos)
        else:
            all_q   = _all_questions(custom)
            order   = _shuffle(player + room_code, len(all_q), 5)
            pos     = int(position)
            if pos >= 5:
                return "Position must be 0 to 4."
            q_index = order[pos]
            return _format_riddle(all_q[q_index], "ROOM " + room_code, q_index, pos)

    @gl.public.view
    def get_score(self, player: str) -> str:
        scores   = json.loads(self.scores)
        attempts = json.loads(self.attempts)
        return (
            "Player: " + player
            + " | Score: " + str(scores.get(player, 0))
            + " | Attempts: " + str(attempts.get(player, 0))
        )

    @gl.public.view
    def get_all_scores(self) -> str:
        """Global leaderboard ranked by score."""
        scores   = json.loads(self.scores)
        attempts = json.loads(self.attempts)
        if not scores:
            return "No players yet. Be the first!"
        board = sorted(
            [{"player": p, "score": s, "attempts": attempts.get(p, 0)} for p, s in scores.items()],
            key=lambda x: x["score"], reverse=True
        )
        return json.dumps(board, sort_keys=True)

    @gl.public.view
    def get_room_info(self, room_code: str) -> str:
        rooms = json.loads(self.rooms)
        if room_code not in rooms:
            return "Room " + room_code + " not found."
        room = rooms[room_code]
        return json.dumps({
            "room_code":    room_code,
            "host":         room["host"],
            "players":      room["players"],
            "player_count": len(room["players"]),
            "scores":       room["room_scores"],
            "active":       room["active"],
            "custom_only":  room.get("custom_only", "false")
        }, sort_keys=True)

    @gl.public.view
    def get_room_scores(self, room_code: str) -> str:
        """Leaderboard for a specific room."""
        rooms = json.loads(self.rooms)
        if room_code not in rooms:
            return "Room " + room_code + " not found."
        room  = rooms[room_code]
        board = sorted(
            [{"player": p, "score": s} for p, s in room["room_scores"].items()],
            key=lambda x: x["score"], reverse=True
        )
        return json.dumps({"room_code": room_code, "leaderboard": board}, sort_keys=True)

    @gl.public.view
    def list_custom_riddles(self) -> str:
        """See all community-created riddles."""
        custom = json.loads(self.custom_riddles)
        if not custom:
            return "No custom riddles yet. Create one with add_custom_riddle!"
        result = []
        for i, q in enumerate(custom):
            result.append({
                "index":   len(QUESTIONS) + i,
                "riddle":  q["riddle"][:80] + "...",
                "author":  q.get("author", "unknown"),
                "options": q["options"]
            })
        return json.dumps(result, sort_keys=True)

    @gl.public.view
    def get_total_questions(self) -> str:
        custom = json.loads(self.custom_riddles)
        return (
            "Built-in questions: " + str(len(QUESTIONS))
            + " | Custom questions: " + str(len(custom))
            + " | Total: " + str(len(QUESTIONS) + len(custom))
        )

    # ── WRITE METHODS ──────────────────────────────────────────────────────────

    @gl.public.write
    def add_custom_riddle(self, author: str, riddle: str, option_a: str, option_b: str, option_c: str, option_d: str, correct_letter: str, correct_answer: str) -> str:
        """
        Create your own riddle and add it to the game.
        correct_letter must be A, B, C or D.
        correct_answer is the text answer (e.g. 'bitcoin').
        """
        assert len(riddle) >= 10, "Riddle must be at least 10 characters."
        assert correct_letter in ["A", "B", "C", "D"], "correct_letter must be A, B, C or D."
        assert len(correct_answer) >= 1, "Correct answer cannot be empty."

        custom = json.loads(self.custom_riddles)

        # Check for duplicates
        for q in custom:
            if q["riddle"].strip().lower() == riddle.strip().lower():
                return "This riddle already exists in the custom bank."

        new_q = {
            "riddle":  riddle,
            "options": {"A": option_a, "B": option_b, "C": option_c, "D": option_d},
            "letter":  correct_letter.upper(),
            "answer":  correct_answer.lower(),
            "author":  author
        }
        custom.append(new_q)
        self.custom_riddles = json.dumps(custom, sort_keys=True)
        new_index = len(QUESTIONS) + len(custom) - 1
        return (
            "Custom riddle added! ID: " + str(new_index) + "\n"
            + "Your riddle will now appear in shuffled sessions for all players.\n"
            + "To use ONLY your riddle in a room: create_custom_room(host, " + str(new_index) + ")"
        )

    @gl.public.write
    def create_room(self, host: str) -> str:
        """Create a standard multiplayer room with all questions."""
        rooms     = json.loads(self.rooms)
        room_code = _make_room_code(host)
        if room_code in rooms:
            room_code = room_code + "2"
        rooms[room_code] = {
            "host":        host,
            "players":     [host],
            "room_scores": {host: 0},
            "active":      "true",
            "custom_only": "false",
            "custom_ids":  []
        }
        self.rooms = json.dumps(rooms, sort_keys=True)
        return (
            "Room created! Code: " + room_code + "\n\n"
            + "Share this code with friends.\n"
            + "Friends join with:   join_room(their_wallet, " + room_code + ")\n"
            + "Get your riddle:     get_room_riddle(wallet, " + room_code + ", 0)\n"
            + "Submit your answer:  submit_room_answer(wallet, " + room_code + ", question_id, answer)"
        )

    @gl.public.write
    def create_custom_room(self, host: str, custom_riddle_ids: str) -> str:
        """
        Create a room using ONLY specific custom riddle IDs.
        custom_riddle_ids: comma-separated IDs e.g. '15,16,17,18,19'
        Players will only see your chosen riddles — great for friend challenges!
        """
        rooms     = json.loads(self.rooms)
        custom    = json.loads(self.custom_riddles)
        all_q     = _all_questions(custom)
        room_code = _make_room_code(host + "custom")
        if room_code in rooms:
            room_code = room_code + "X"

        # Parse IDs
        try:
            ids = [int(x.strip()) for x in custom_riddle_ids.split(",")]
        except Exception:
            return "Invalid IDs format. Use comma-separated numbers like: 15,16,17"

        valid_ids = [i for i in ids if i < len(all_q)]
        if len(valid_ids) == 0:
            return "No valid question IDs found. Check your IDs with list_custom_riddles."

        rooms[room_code] = {
            "host":        host,
            "players":     [host],
            "room_scores": {host: 0},
            "active":      "true",
            "custom_only": "true",
            "custom_ids":  valid_ids
        }
        self.rooms = json.dumps(rooms, sort_keys=True)
        return (
            "Custom room created! Code: " + room_code + "\n"
            + "Using " + str(len(valid_ids)) + " custom riddle(s): " + str(valid_ids) + "\n\n"
            + "Friends join with:  join_room(their_wallet, " + room_code + ")\n"
            + "Get your riddle:    get_room_riddle(wallet, " + room_code + ", 0)\n"
            + "Submit answer:      submit_room_answer(wallet, " + room_code + ", question_id, answer)"
        )

    @gl.public.write
    def join_room(self, player: str, room_code: str) -> str:
        """Join a room using the 6-character room code."""
        rooms = json.loads(self.rooms)
        if room_code not in rooms:
            return "Room " + room_code + " not found. Double-check the code."
        room = rooms[room_code]
        if room["active"] != "true":
            return "Room " + room_code + " is already closed."
        if player in room["players"]:
            return "You are already in room " + room_code + "."
        room["players"].append(player)
        room["room_scores"][player] = 0
        rooms[room_code] = room
        self.rooms = json.dumps(rooms, sort_keys=True)
        return (
            "Joined room " + room_code + "! "
            + str(len(room["players"])) + " players in room.\n\n"
            + "Start: get_room_riddle(" + player + ", " + room_code + ", 0)"
        )

    @gl.public.write
    def submit_answer(self, player: str, question_id: u256, player_answer: str) -> str:
        """Solo mode — submit answer. Use the question_id shown in get_my_riddle."""
        custom = json.loads(self.custom_riddles)
        all_q  = _all_questions(custom)
        i      = int(question_id)
        if i >= len(all_q):
            return "Invalid question ID. Use get_my_riddle to see your questions."
        q = all_q[i]

        attempts         = json.loads(self.attempts)
        attempts[player] = attempts.get(player, 0) + 1
        self.attempts    = json.dumps(attempts, sort_keys=True)

        # ── RICHER AI VERDICT ──────────────────────────────────────────────────
        # AI does not just say YES/NO — it judges quality, confidence, and reasoning.
        # 5 validators each independently run this prompt and must agree on the verdict
        # AND have confidence scores within 25 points. This is genuine AI consensus.
        prompt = (
            "You are the judge of a GenLayer blockchain riddle game.\n"
            "Riddle: \"" + q["riddle"] + "\"\n"
            "Correct answer: option " + q["letter"] + " = \"" + q["options"][q["letter"]] + "\" (keyword: " + q["answer"] + ")\n"
            "Player answered: \"" + player_answer + "\"\n\n"
            "Evaluate the player's answer and respond ONLY with valid JSON:\n"
            "{\"verdict\":\"CORRECT\" or \"WRONG\","
            "\"confidence\":0-100,"
            "\"reasoning\":\"one sentence explaining your judgment\"}\n\n"
            "Rules:\n"
            "- CORRECT if: player chose letter " + q["letter"] + ", OR text clearly matches \"" + q["answer"] + "\", OR is a valid synonym.\n"
            "- WRONG if: wrong letter, unrelated answer, or gibberish.\n"
            "- confidence: how certain you are (100 = certain, 50 = borderline)\n"
            "- Respond ONLY with the JSON. No markdown, no extra text."
        )

        def get_verdict():
            return gl.nondet.exec_prompt(prompt)

        result = gl.eq_principle.prompt_comparative(
            get_verdict,
            "Two verdicts are equivalent if: (1) the 'verdict' field is identical "
            "(both say CORRECT or both say WRONG), AND (2) confidence scores are within 25 points. "
            "The reasoning text may differ in wording."
        )

        # Parse the richer verdict
        try:
            clean = result.strip().strip('`').strip()
            if clean.lower().startswith('json'): clean = clean[4:].strip()
            verdict_data = json.loads(clean)
            is_correct   = verdict_data.get("verdict", "").upper() == "CORRECT"
            confidence   = verdict_data.get("confidence", 0)
            reasoning    = verdict_data.get("reasoning", "")
        except Exception:
            # Fallback to simple YES/NO parse if JSON fails
            is_correct = "CORRECT" in result.upper() or "YES" in result.upper()
            confidence = 80
            reasoning  = ""

        if is_correct:
            scores         = json.loads(self.scores)
            scores[player] = scores.get(player, 0) + 1
            self.scores    = json.dumps(scores, sort_keys=True)
            total = scores[player]
            msg = "CORRECT"
            if total >= 5: msg = "LEGENDARY"
            return json.dumps({
                "result":    msg,
                "score":     total,
                "answer":    q["letter"] + ". " + q["options"][q["letter"]],
                "confidence": confidence,
                "reasoning": reasoning
            }, sort_keys=True)
        else:
            return json.dumps({
                "result":     "WRONG",
                "answer":     q["letter"] + ". " + q["options"][q["letter"]],
                "confidence": confidence,
                "reasoning":  reasoning
            }, sort_keys=True)

    @gl.public.write
    def submit_room_answer(self, player: str, room_code: str, question_id: u256, player_answer: str) -> str:
        """Room mode — submit answer. Use question_id shown in get_room_riddle."""
        rooms = json.loads(self.rooms)
        if room_code not in rooms:
            return "Room " + room_code + " not found."
        room = rooms[room_code]
        if player not in room["players"]:
            return "You are not in room " + room_code + ". Call join_room first."

        custom = json.loads(self.custom_riddles)
        all_q  = _all_questions(custom)
        i      = int(question_id)
        if i >= len(all_q):
            return "Invalid question ID. Use get_room_riddle to see your questions."
        q = all_q[i]

        attempts         = json.loads(self.attempts)
        attempts[player] = attempts.get(player, 0) + 1
        self.attempts    = json.dumps(attempts, sort_keys=True)

        prompt = (
            "You are the judge of a GenLayer blockchain riddle game.\n"
            "Riddle: \"" + q["riddle"] + "\"\n"
            "Correct answer: option " + q["letter"] + " = \"" + q["options"][q["letter"]] + "\" (keyword: " + q["answer"] + ")\n"
            "Player answered: \"" + player_answer + "\"\n\n"
            "Evaluate the player's answer and respond ONLY with valid JSON:\n"
            "{\"verdict\":\"CORRECT\" or \"WRONG\","
            "\"confidence\":0-100,"
            "\"reasoning\":\"one sentence explaining your judgment\"}\n\n"
            "Rules:\n"
            "- CORRECT if: player chose letter " + q["letter"] + ", OR text clearly matches \"" + q["answer"] + "\", OR is a valid synonym.\n"
            "- WRONG if: wrong letter, unrelated answer, or gibberish.\n"
            "- confidence: how certain you are (100 = certain, 50 = borderline)\n"
            "- Respond ONLY with the JSON. No markdown, no extra text."
        )

        def get_verdict():
            return gl.nondet.exec_prompt(prompt)

        result = gl.eq_principle.prompt_comparative(
            get_verdict,
            "Two verdicts are equivalent if: (1) the 'verdict' field is identical "
            "(both say CORRECT or both say WRONG), AND (2) confidence scores are within 25 points. "
            "The reasoning text may differ in wording."
        )

        try:
            clean = result.strip().strip('`').strip()
            if clean.lower().startswith('json'): clean = clean[4:].strip()
            verdict_data = json.loads(clean)
            is_correct   = verdict_data.get("verdict", "").upper() == "CORRECT"
            confidence   = verdict_data.get("confidence", 0)
            reasoning    = verdict_data.get("reasoning", "")
        except Exception:
            is_correct = "CORRECT" in result.upper() or "YES" in result.upper()
            confidence = 80
            reasoning  = ""

        if is_correct:
            scores         = json.loads(self.scores)
            scores[player] = scores.get(player, 0) + 1
            self.scores    = json.dumps(scores, sort_keys=True)
            room["room_scores"][player] = room["room_scores"].get(player, 0) + 1
            rooms[room_code] = room
            self.rooms       = json.dumps(rooms, sort_keys=True)
            room_score = room["room_scores"][player]
            msg = "LEGENDARY" if room_score >= 5 else "CORRECT"
            return json.dumps({
                "result":     msg,
                "room_score": room_score,
                "answer":     q["letter"] + ". " + q["options"][q["letter"]],
                "confidence": confidence,
                "reasoning":  reasoning
            }, sort_keys=True)
        else:
            return json.dumps({
                "result":     "WRONG",
                "answer":     q["letter"] + ". " + q["options"][q["letter"]],
                "confidence": confidence,
                "reasoning":  reasoning
            }, sort_keys=True)

    @gl.public.write
    def generate_ai_riddle(self, requester: str, topic: str) -> str:
        """
        ── CORE AI MECHANIC ──────────────────────────────────────────────────────
        AI generates a brand-new GenLayer riddle on any topic.
        5 validators independently generate a riddle and must reach consensus
        that their riddles test the same knowledge and have the same correct answer.
        This is IMPOSSIBLE without GenLayer AI + Optimistic Democracy consensus.
        Generated riddles are stored on-chain permanently and enter the game pool.
        ─────────────────────────────────────────────────────────────────────────
        """
        assert len(topic.strip()) >= 3, "Topic must be at least 3 characters."
        assert len(topic) <= 100, "Topic too long. Keep it under 100 characters."

        def generate() -> str:
            prompt = (
                "You are creating a riddle for a GenLayer blockchain knowledge game.\n"
                "Topic to test: \"" + topic + "\"\n\n"
                "Create ONE riddle in this EXACT JSON format (no markdown, no extra text):\n"
                "{\"riddle\":\"...the riddle text as a puzzle or question...\","
                "\"options\":{\"A\":\"...\",\"B\":\"...\",\"C\":\"...\",\"D\":\"...\"},"
                "\"letter\":\"A or B or C or D\","
                "\"answer\":\"...correct answer text in lowercase...\","
                "\"explanation\":\"...one sentence why this is correct...\"}\n\n"
                "Requirements:\n"
                "- The riddle MUST test knowledge about: " + topic + "\n"
                "- Exactly ONE option must be correct. Label it with the 'letter' field.\n"
                "- The other three options must be plausible but wrong.\n"
                "- The riddle must be solvable by someone with GenLayer knowledge.\n"
                "- Respond ONLY with the JSON object. No extra text."
            )
            return gl.nondet.exec_prompt(prompt)

        result = gl.eq_principle.prompt_comparative(
            generate,
            "Two AI-generated riddles about \"" + topic + "\" are equivalent if: "
            "(1) both test knowledge of " + topic + ", "
            "(2) the same letter (A/B/C/D) is marked as correct in both, "
            "(3) all four options A, B, C, D are present, "
            "(4) the answer fields refer to the same concept. "
            "Differences in exact wording of the riddle text or options are acceptable."
        )

        try:
            clean = result.strip()
            # Strip markdown code fences if present
            if "```" in clean:
                clean = clean.split("```")[1]
                if clean.startswith("json"): clean = clean[4:]
            clean = clean.strip()
            riddle_data = json.loads(clean)

            # Validate required fields
            for field in ["riddle", "options", "letter", "answer"]:
                if field not in riddle_data:
                    return json.dumps({"status": "error", "message": "AI returned incomplete riddle. Try again."})

            if riddle_data["letter"] not in ["A", "B", "C", "D"]:
                return json.dumps({"status": "error", "message": "AI returned invalid letter. Try again."})

            riddle_data["author"]       = "AI"
            riddle_data["topic"]        = topic
            riddle_data["generated_by"] = requester

            custom = json.loads(self.custom_riddles)
            custom.append(riddle_data)
            self.custom_riddles = json.dumps(custom, sort_keys=True)

            new_id = len(QUESTIONS) + len(custom) - 1
            return json.dumps({
                "status":  "generated",
                "id":      new_id,
                "topic":   topic,
                "riddle":  riddle_data["riddle"],
                "options": riddle_data["options"],
                "message": "AI-generated riddle stored on-chain permanently. ID: " + str(new_id)
            }, sort_keys=True)

        except Exception:
            return json.dumps({
                "status":  "error",
                "message": "Failed to parse AI riddle. Try a more specific topic."
            })

    @gl.public.write
    def get_riddle_hint(self, question_id: u256) -> str:
        """
        AI generates a personalised hint for any riddle.
        Each of 5 validators independently generates a hint — consensus ensures
        the hint is helpful without giving away the answer directly.
        """
        custom = json.loads(self.custom_riddles)
        all_q  = _all_questions(custom)
        i      = int(question_id)
        if i >= len(all_q):
            return "Invalid question ID."
        q = all_q[i]

        def generate_hint() -> str:
            prompt = (
                "You are a helpful hint-giver in a GenLayer blockchain riddle game.\n"
                "The riddle is: \"" + q["riddle"] + "\"\n"
                "Options: A=" + q["options"]["A"] + ", B=" + q["options"]["B"]
                + ", C=" + q["options"]["C"] + ", D=" + q["options"]["D"] + "\n\n"
                "Give ONE helpful hint that guides the player toward the correct answer "
                "WITHOUT revealing the answer letter or the answer text directly.\n"
                "Reference GenLayer concepts in your hint to help narrow it down.\n"
                "Keep it to 1-2 sentences maximum.\n"
                "Do NOT say the answer letter. Do NOT say the answer text."
            )
            return gl.nondet.exec_prompt(prompt)

        hint = gl.eq_principle.prompt_comparative(
            generate_hint,
            "Two hints are equivalent if they guide toward the same answer without "
            "revealing it directly, and reference similar GenLayer concepts. "
            "Exact wording may differ between validators."
        )
        return "HINT: " + hint.strip()

    @gl.public.write
    def close_room(self, host: str, room_code: str) -> str:
        """Close your room (host only). Shows final scores."""
        rooms = json.loads(self.rooms)
        if room_code not in rooms:
            return "Room " + room_code + " not found."
        if rooms[room_code]["host"] != host:
            return "Only the room host can close the room."
        rooms[room_code]["active"] = "false"
        self.rooms = json.dumps(rooms, sort_keys=True)
        final = rooms[room_code]["room_scores"]
        return "Room " + room_code + " closed. Final scores: " + json.dumps(final)
