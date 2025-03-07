# Quake Log Parserr

A simple collection of Python scripts to parse and analyze Quake game log files. Extracts information about kills, players, matches, and generates various reports.
This is a challenge created for Cloud Walk (CW). 
You can visit the repository here → https://gist.github.com/drake-cloudwalk/77a7046303292b4c4d6440a59ae07c59

## Available Reports

- Basic player kills
- Match-by-match statistics
- Death causes analysis
- Player ranking

## Requirements

- Python 3.x
- No additional libraries required (uses only Python standard libraries)

## Installation

1. Install Python:
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

2. Clone or download this repository

## Usage

All scripts are in the `src` directory and the log file should be in `log/quake.log`. Run from the project root:

```bash
# Basic kills report
python src/quake_parser.py > outputs/game_report.json

# Match statistics
python src/quake_parser_by_match.py > outputs/matches_report.json

# Death causes report
python src/quake_parser_death_cause.py > outputs/death_cause_report.json

# Player ranking
python src/quake_parser_ranking.py > outputs/ranking.txt
```

## Output Examples

### Player Ranking
```
1. Isgalamido - 10 kills
2. Zeh - 7 kills
3. Dono da Bola - 3 kills
```

### Match Statistics
```json
{
  "game_1": {
    "total_kills": 3,
    "players": ["Isgalamido", "Dono da Bola", "Zeh"],
    "kills": {
      "Isgalamido": 2,
      "Dono da Bola": 0,
      "Zeh": 1
    }
  }
}
``` 

## Development Process

- This code was developed using Cursor IDE with Claude-3.5-Sonnet AI agent (default)
- The development followed a structured prompt pattern:
  1. [INTRODUCTION] → Brief overview of the expected solution
  2. [CONTEXT] → Detailed requirements and specifications
  3. [OUTPUT] → Expected output format and examples

### Example Prompt:
  1. [INTRODUCTION] Write a code with python implementing a feature that I describe bellow

  2. [CONTEXT]
  
```bash
    Quake Log Parser - AI-Driven Live Coding Test
    Truth can only be found in one place: the code.
    – Robert C. Martin

    Welcome to the Quake Log Parser Test! In this live coding challenge, you will using embedded AI tools in your IDE (e.g., Aider, Cursor, Co-pilot) to implement a log parser that processes game data from a Quake 3 Arena server. This test evaluates your technical skills, problem-solving abilities, and effective use of AI in real-time coding.

    The Challenge
    Task: Parse a Quake log file to extract and summarize match data.
    Input: A log file with match events, such as player kills and deaths. Example Snippet:
    0:00 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
    0:15 Kill: 3 2 10: Isgalamido killed Dono da Bola by MOD_RAILGUN
    1:00 Kill: 3 2 10: Isgalamido killed Zeh by MOD_RAILGUN
    Full Log

    Requirements
    Parse the log file and extract the following:

    A list of players in the match.
    A dictionary showing the number of kills per player.
    Rules:

    If <world> kills a player, that player’s kill count decreases by 1.
    <world> is not considered a player and should not appear in the output.
```
  3. [OUTPUT] Follow the example bellow:

```bash
    Output: JSON summarizing players and their kills. Example:
    {
    "players": ["Isgalamido", "Dono da Bola", "Zeh"],
    "kills": {"Isgalamido": 2, "Dono da Bola": 0, "Zeh": 0}
    }
```

