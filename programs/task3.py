

teams = {
    "TeamA": [
        {"name": "Alice", "role": "Batsman"},
        {"name": "Bob", "role": "Bowler"}
    ],
    "TeamB": [
        {"name": "Charlie", "role": "Allrounder"},
        {"name": "Dave", "role": "Wicketkeeper"}
    ]
}

for key,value in teams.items():
    print(key)
    print("------------")
    for item in value:
        print(item['name'])