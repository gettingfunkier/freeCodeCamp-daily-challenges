def favorite_songs(playlist):

    top1_count, top2_count = 0, 0
    top1_name, top2_name = "", ""

    top1_count = 0

    top_songs = []

    for song in playlist:
        if song["plays"] >= top1_count:
            top1_count = song["plays"]
            top1_name = song["title"]

    for song in playlist:
        if song["plays"] >= top2_count:
            count_cache = top2_count
            top2_count = song["plays"]

            name_cache = top2_name
            top2_name = song["title"]

        if top2_count == top1_count:
            top2_count = count_cache
            top2_name = name_cache

    top_songs.append(top1_name)
    top_songs.append(top2_name)
    print(top_songs)

    return top_songs


p = [
    {
        "title": "Sync or Swim",
        "plays": 3
    },
    {
        "title": "Byte Me",
        "plays": 1
    },
    {
        "title": "Earbud Blues",
        "plays": 2
    }
]

favorite_songs(p)