function numberOfPhotos(photoSizeMb, hardDriveSizeGb) {
    let hardDriveSizeMb = hardDriveSizeGb * 1000
    return Math.floor(hardDriveSizeMb / photoSizeMb)
}