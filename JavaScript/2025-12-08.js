function convertToKgs(lbs) {
    const kgs = (lbs * 0.453592).toFixed(2);

    if (lbs === 1) {
        return `${lbs} pound equals ${kgs} kilograms.`
    }

    else if (parseFloat(kgs) === 1) {
        return `${lbs} pounds equals ${kgs} kilogram.`
    }

    else {
        return `${lbs} pounds equals ${kgs} kilograms.`
    }

}