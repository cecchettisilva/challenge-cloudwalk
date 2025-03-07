import json
import re

def parse_quake_log_by_match(file_path):
    games = {}
    current_game = None
    game_count = 0
    
    # Patterns to identify important events
    init_game_pattern = re.compile(r'InitGame:')
    kill_pattern = re.compile(r'Kill: (\d+) (\d+) \d+: (.+) killed (.+) by')
    shutdown_pattern = re.compile(r'(ShutdownGame:|Exit:)')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Start of a new game
            if init_game_pattern.search(line):
                # If there's an ongoing game, convert players set to list
                if current_game is not None:
                    current_game["players"] = list(current_game["players"])
                
                game_count += 1
                game_name = f"game_{game_count}"
                current_game = {
                    "total_kills": 0,
                    "players": set(),
                    "kills": {}
                }
                games[game_name] = current_game
                
            # Processing kills
            elif current_game is not None and kill_pattern.search(line):
                match = kill_pattern.search(line)
                killer_id, victim_id, killer, victim = match.groups()
                
                # Remove possible MOD_ from victim's name
                victim = victim.split('by')[0].strip()
                
                # Increment total kills for the game
                current_game["total_kills"] += 1
                
                # Add players to the list (except world)
                if killer != "<world>":
                    current_game["players"].add(killer)
                current_game["players"].add(victim)
                
                # Initialize kill counters if needed
                if killer != "<world>" and killer not in current_game["kills"]:
                    current_game["kills"][killer] = 0
                if victim not in current_game["kills"]:
                    current_game["kills"][victim] = 0
                
                # Update kills
                if killer == "<world>":
                    current_game["kills"][victim] -= 1
                else:
                    current_game["kills"][killer] += 1
                    
            # End of game
            elif current_game is not None and shutdown_pattern.search(line):
                # Convert players set to list before finalizing the game
                if current_game:
                    current_game["players"] = list(current_game["players"])
    
    # Convert last game (if exists) to list
    if current_game:
        current_game["players"] = list(current_game["players"])
        
    # Ensure all games have their players converted to list
    for game in games.values():
        if isinstance(game["players"], set):
            game["players"] = list(game["players"])
    
    return json.dumps(games, indent=2)

# Execute parser on quake.log file
if __name__ == "__main__":
    file_path = "log/quake.log"
    print(parse_quake_log_by_match(file_path)) 