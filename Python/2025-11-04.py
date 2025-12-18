def image_search(images, term):
    results = []

    for i in images:
        if term.lower() in i.lower():
            results.append(i)

    return results