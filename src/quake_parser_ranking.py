import re
from collections import defaultdict

def parse_quake_log_ranking(file_path):
    total_kills = defaultdict(int)
    
    # Pattern to identify kills
    kill_pattern = re.compile(r'Kill: \d+ \d+ \d+: (.+) killed (.+) by')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = kill_pattern.search(line)
            if match:
                killer, victim = match.groups()
                
                # Remove possible MOD_ from victim's name
                victim = victim.split('by')[0].strip()
                
                # Update kill counter
                if killer != "<world>":
                    total_kills[killer] += 1
                else:
                    # If killed by world, victim loses a kill
                    total_kills[victim] -= 1

    # Filter players with positive kills and sort by kill count (descending)
    sorted_players = sorted(
        [(player, kills) for player, kills in total_kills.items() if kills > 0],
        key=lambda x: x[1],
        reverse=True
    )
    
    # Format ranking as text
    ranking_text = "RANKING - Sorted by number of kills (highest to lowest):\n"
    ranking_text += "=" * 50 + "\n\n"
    
    if sorted_players:
        for position, (player, kills) in enumerate(sorted_players, 1):
            ranking_text += f"{position}. {player} - {kills} kills\n"
    else:
        ranking_text += "No players with positive kills found.\n"
    
    return ranking_text.strip()

# Execute parser on quake.log file
if __name__ == "__main__":
    file_path = "log/quake.log"
    print(parse_quake_log_ranking(file_path)) 