from pydub import AudioSegment
from pydub.playback import play

def play_wav(file_path):
    sound = AudioSegment.from_file(file_path, format="wav")
    play(sound)

# Example usage
file_path = 'output.wav'
play_wav(file_path)
