def number_of_photos(photo_size_mb, drive_size_gb):
    drive_size_mb = drive_size_gb * 1000
    no_of_photos = int(drive_size_mb / photo_size_mb)
    return no_of_photos