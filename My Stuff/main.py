import os
import sys

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
torch.serialization.add_safe_globals([xtts_config.XttsConfig])

def main():
    # Get script directory (My Stuff)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add parent folder (TTS-webui) to sys.path so Python can find the TTS package
    tts_webui_path = os.path.abspath(os.path.join(script_dir, ".."))
    if tts_webui_path not in sys.path:
        sys.path.insert(0, tts_webui_path)

    # Load the model
    print("Loading TTS model...")
    #tts = TTS("tts_models/en/ljspeech/tacotron2-DDC", gpu=False)  # change model or gpu as needed
    # Load your model (use your exact model name here)
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

    # Print all available speakers (voices)
    print(tts.synthesizer.tts_model.speaker_manager.speakers.keys())
    speaker = "Zacharie Aimilios"

    # Text to synthesize
    text = f"Hello, this is {speaker} speaking from the My Stuff folder!"

    # Synthesize audio
    print("Synthesizing...")
    wav = tts.tts(text, speaker=speaker, language="en")

    # Output path relative to script dir
    output_path = os.path.join(script_dir, "output.wav")

    # Save audio file
    sf.write(output_path, wav, samplerate=22050)
    print(f"Audio saved to {output_path}")

if __name__ == "__main__":
    main()
