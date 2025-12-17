function favoriteSongs(playlist) {

    let top1Count = 0
    let top2Count = 0
    let top1Name
    let top2Name

    let topSongs = []

    for (let song of playlist) {
        if (song["plays"] >= top1Count) {
            top1Count = song["plays"]
            top1Name = song["title"]
        }
    }

    for (let song of playlist) {

        let countCache
        let nameCache

        if (song["plays"] >= top2Count) {
            countCache = top2Count
            top2Count = song["plays"]

            nameCache = top2Name
            top2Name = song["title"]
        }

        if (top2Count === top1Count) {
            top2Count = countCache
            top2Name = nameCache
        }
    }

    topSongs.push(top1Name)
    topSongs.push(top2Name)

    return topSongs
}