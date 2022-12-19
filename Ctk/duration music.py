from mutagen.mp3 import MP3

def set_duartion(song):

    def audio_duration(length):
        mins = length // 60
        length %= 60
        seconds = length

        return mins, seconds

    audio = MP3("../Song/"+ song + '.mp3')
    audio_info = audio.info
    length = int(audio_info.length)
    mins, seconds = audio_duration(length)
    return print('Total Duration: {}:{}'.format(mins, seconds))

set_duartion('Love Me')