import os
import sys

# eSpeak backend
espeak_path = r"C:\Program Files\eSpeak NG"
os.environ["PATH"] += os.pathsep + espeak_path


# Add parent folder (TTS-webui) to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from TTS.api import TTS
import soundfile as sf

# fixing some weird error
import torch
from TTS.tts.configs import xtts_config
from TTS.tts.models import xtts
from TTS.config import shared_configs

torch.serialization.add_safe_globals([
    xtts_config.XttsConfig,
    xtts.XttsAudioConfig,
    xtts.XttsArgs,
    shared_configs.BaseDatasetConfig,
])

def main():
    # Get script directory (My Stuff)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add parent folder (TTS-webui) to sys.path so Python can find the TTS package
    tts_webui_path = os.path.abspath(os.path.join(script_dir, ".."))
    if tts_webui_path not in sys.path:
        sys.path.insert(0, tts_webui_path)

    # Load the model
    print("Loading TTS model...")
    # Load a multi-speaker model (example)
    tts = TTS("tts_models/en/vctk/vits")

    # List available models
    print(tts.speakers)
    speaker = "p232"

    # Text to synthesize
    text = f"Hello, this is {speaker} speaking from the My Stuff folder!"

    # Synthesize audio
    print("Synthesizing...")
    wav = tts.tts(text, speaker=speaker)

    # Output path relative to script dir
    output_path = os.path.join(script_dir, "output.wav")

    # Save audio file
    sf.write(output_path, wav, samplerate=22050)
    print(f"Audio saved to {output_path}")

if __name__ == "__main__":
    main()
