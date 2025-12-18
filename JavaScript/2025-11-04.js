function imageSearch(images, term) {
    let results = []

    for (let i of images) {
        if (i.toLowerCase().includes(term.toLowerCase())) results.push(i)
    }

    return results;
}