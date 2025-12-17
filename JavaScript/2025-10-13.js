function to12(time) {
    let hh = parseInt(time.toString().slice(0, 2)).toString()
    let mm = time.toString().slice(2, 4)

    if (hh === "0") {
        return `12:${mm} AM`
    }

    else if (hh < 13) {
        return `${hh}:${mm} AM`
    }

    else {
        return `${(hh - 12).toString()}:${mm} PM`
    }
}