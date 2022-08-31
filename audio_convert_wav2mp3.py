from pydub import AudioSegment
import glob2
from multiprocessing import Pool, cpu_count


def load_save_audio(audio_path):
    hires_audio = AudioSegment.from_file(str(audio_path))
    hires_audio.export(str(audio_path[:-4]+".mp3"),format="mp3",bitrate="320k")
    print(f"{audio_path[31:]}")

def convert():
    print(f'Starting computations on {cpu_count()} cores')
    with Pool() as pool:
        res = pool.map(load_save_audio, glob2.glob("/media/anubhav/New Volume/songs/1/*"))
        print("Task Completed!!\n")
        


if __name__ == "__main__":
    convert()

