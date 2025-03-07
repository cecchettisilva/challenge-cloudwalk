import json
import re

def parse_quake_log_death_cause(file_path):
    games = {}
    current_game = None
    game_count = 0
    
    # Patterns to identify important events
    init_game_pattern = re.compile(r'InitGame:')
    kill_pattern = re.compile(r'Kill: \d+ \d+ \d+: .+ killed .+ by (.+)$')
    shutdown_pattern = re.compile(r'(ShutdownGame:|Exit:)')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Start of a new game
            if init_game_pattern.search(line):
                game_count += 1
                game_name = f"game_{game_count}"
                current_game = {
                    "kills_by_means": {}
                }
                games[game_name] = current_game
                
            # Processing kills
            elif current_game is not None and kill_pattern.search(line):
                match = kill_pattern.search(line)
                death_cause = match.group(1).strip()
                
                # Initialize or increment counter for this death cause
                if death_cause not in current_game["kills_by_means"]:
                    current_game["kills_by_means"][death_cause] = 0
                current_game["kills_by_means"][death_cause] += 1
                    
            # End of game
            elif current_game is not None and shutdown_pattern.search(line):
                continue  # Keep current game until finding a new InitGame
    
    return json.dumps(games, indent=2)

# Execute parser on quake.log file
if __name__ == "__main__":
    file_path = "log/quake.log"
    print(parse_quake_log_death_cause(file_path)) 