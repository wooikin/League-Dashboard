def update_score(match, coefficient):

    if match.home_score > match.away_score:
        match.home_team.points += (coefficient*3)
    elif match.home_score < match.away_score:
        match.away_team.points += (coefficient*3)
    else:
        match.home_team.points += (coefficient*1)
        match.away_team.points += (coefficient*1)

    match.home_team.goal_difference += (coefficient* (match.home_score - match.away_score))
    match.away_team.goal_difference += (coefficient* (match.away_score - match.home_score))

    match.home_team.save()
    match.away_team.save()