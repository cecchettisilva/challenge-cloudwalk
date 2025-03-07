import json
import re

def parse_quake_log(file_path):
    players = set()
    kills = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # New regex pattern that matches exactly the file format
            match = re.search(r'Kill: (\d+) (\d+) \d+: (.+) killed (.+) by', line)
            if match:
                killer_id, victim_id, killer, victim = match.groups()
                
                # Remove possible MOD_ from victim's name
                victim = victim.split('by')[0].strip()

                # Add players to the list
                if killer != "<world>":
                    players.add(killer)
                players.add(victim)

                # Initialize kill counter if needed
                if killer != "<world>" and killer not in kills:
                    kills[killer] = 0
                if victim not in kills:
                    kills[victim] = 0

                # Update kills
                if killer == "<world>":
                    kills[victim] -= 1  # If killed by world, victim loses a kill
                else:
                    kills[killer] += 1  # Otherwise, killer gets a kill

    # Format output as JSON
    result = {
        "players": list(players),
        "kills": kills
    }

    return json.dumps(result, indent=2)

# Execute parser on quake.log file
if __name__ == "__main__":
    file_path = "log/quake.log"
    print(parse_quake_log(file_path))