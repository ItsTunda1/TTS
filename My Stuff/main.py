import os
import sys

# Fix PATH for eSpeak
espeak_path = r"C:\Program Files\eSpeak NG"
os.environ["PATH"] += os.pathsep + espeak_path

# Ensure TTS-webui folder is in sys.path BEFORE importing anything from TTS
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# NOW it’s safe to import from TTS
import torch
import soundfile as sf
from TTS.tts.configs import xtts_config
from TTS.tts.models import xtts
from TTS.config import shared_configs
from TTS.api import TTS

# Fix torch serialization
torch.serialization.add_safe_globals([
    xtts_config.XttsConfig,
    xtts.XttsAudioConfig,
    xtts.XttsArgs,
    shared_configs.BaseDatasetConfig,
])

def main():
    print("Loading TTS model...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

    text = "Hello, this is a custom voice from the My Stuff folder!"
    speaker_wav = os.path.join(script_dir, "voices", "myvoice.wav")

    print("Synthesizing...")
    wav = tts.tts(
        text=text,
        speaker_wav=speaker_wav,
        language="en"
    )

    output_path = os.path.join(script_dir, "output.wav")
    sf.write(output_path, wav, samplerate=22050)
    print(f"Audio saved to {output_path}")

if __name__ == "__main__":
    main()





'''
Things to say:
====================
Hello! I'm testing this voice for cloning purposes.
This is a simple sentence to evaluate pronunciation.
Can you hear the difference in my tone when I ask a question?
I hope this helps make my voice clearer in the model.
'''