import pafy

while True:
    url = input("Enter the url: \n")
    video = pafy.new(url)
    audio = video.audiostreams
    folder = input("Enter location: \n")

    for a in audio:
        print('bitrate : %s, ext: %s, size: %0.2fMb' % (a.bitrate, a.extension, a.get_filesize() / 1024 / 1024))

    audio[3].download(filepath=folder)
