def rankings(participants):
    ranking_dict = {}

    for i in range(len(participants)):
        ranking_dict[participants[i]] = i + 1

    return ranking_dict