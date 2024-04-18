def find_winner(votes):
    vote_count = {}
    for vote in votes:
        if vote not in vote_count:
            vote_count[vote] = 1
        else:
            count = vote_count[vote]
            vote_count[vote] = count + 1
    max_vote = 0
    winner_name = ""
    for name in vote_count.keys():
        if (vote_count[name] > max_vote or
                (vote_count[name] == max_vote and
                 name < winner_name)):
            max_vote = vote_count[name]
            winner_name = name

    return winner_name