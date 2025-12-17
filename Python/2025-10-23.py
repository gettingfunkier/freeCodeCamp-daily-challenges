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

    return top_songs





# TEST 1 - return ['Sync or Swim', 'Earbud Blues']
print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))

# TEST 2 - return ['Clickwheel Love', '99 Downloads']
print(favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]))

# TEST 3 - return ['Song B', 'Song C']
print(favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]))