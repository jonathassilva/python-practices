def partition(L: list, key_order: list) -> int:
    low = 0
    high = len(L) - 1
    pivot = L[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            if compare_teams(L[i], pivot, key_order) >= 0:
                break

        while True:
            j -= 1
            if compare_teams(L[j], pivot, key_order) <= 0:
                break

        if i >= j:
            return j

        L[i], L[j] = L[j], L[i]


def compare_teams(team1: dict, team2: dict, key_order: list) -> int:
    for key, reverse in key_order:
        if key == 'name':
            if team1[key].lower() != team2[key].lower():
                return -1 if team1[key].lower() < team2[key].lower() else 1
        else:
            if team1[key] != team2[key]:
                return (team1[key] - team2[key]) * (-1 if reverse else 1)
    return 0


def quick_sort(L: list, key_order: list) -> list:
    if len(L) > 1:
        partition_index = partition(L, key_order)

        left_part = L[:partition_index + 1]
        right_part = L[partition_index + 1:]

        left_part = quick_sort(left_part, key_order)
        right_part = quick_sort(right_part, key_order)

        L[:len(left_part)] = left_part
        L[len(left_part):] = right_part

    return L


def process_championships():
    n = int(input())

    for _ in range(n):
        input()
        championship_name = input().strip()
        team_numbers = int(input().strip())
        teams = []

        for i in range(team_numbers):
            team_name = input().strip()
            teams.append({
                'name': team_name,
                'points': 0,
                'games': 0,
                'wins': 0,
                'draws': 0,
                'losses': 0,
                'goals_for': 0,
                'goals_against': 0,
                'goals_diff': 0
            })

        games = int(input().strip())
        for _ in range(games):
            game = input().strip()
            team1, rest = game.split(':', 1)
            goals1, rest = rest.split('#', 1)
            team2, goals2 = rest.split(':', 1)

            goals1 = int(goals1)
            goals2 = int(goals2)

            for index, value in enumerate(teams):
                if value['name'] == team1:
                    i1 = index
                elif value['name'] == team2:
                    i2 = index

            teams[i1]['games'] += 1
            teams[i2]['games'] += 1

            teams[i1]['goals_for'] += goals1
            teams[i1]['goals_against'] += goals2
            teams[i2]['goals_for'] += goals2
            teams[i2]['goals_against'] += goals1

            if goals1 > goals2:
                teams[i1]['points'] += 3
                teams[i1]['wins'] += 1
                teams[i2]['losses'] += 1
            elif goals2 > goals1:
                teams[i2]['points'] += 3
                teams[i2]['wins'] += 1
                teams[i1]['losses'] += 1
            else:
                teams[i1]['points'] += 1
                teams[i2]['points'] += 1
                teams[i1]['draws'] += 1
                teams[i2]['draws'] += 1

        # Goals diff rating
        for team in teams:
            team['goals_diff'] = team['goals_for'] - team['goals_against']

        # Ordenation process
        key_order = [
            ('points', True),
            ('wins', True),
            ('goals_diff', True),
            ('goals_for', True),
            ('games', False),
            ('name', False)
        ]

        teams = quick_sort(teams, key_order)

        print(championship_name)

        for index, team in enumerate(teams):
            print(f"{index + 1} - {team['name']}: {team['points']} pontos, {team['games']} jogos ({team['wins']}-{team['draws']}-{team['losses']}), "
                  f"d.g. {team['goals_for'] - team['goals_against']} ({team['goals_for']}-{team['goals_against']})")



process_championships()
