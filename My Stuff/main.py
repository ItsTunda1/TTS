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

'''def get_attention_mask(tokenizer, text):
    encoding = tokenizer.encode(text)
    input_ids = encoding.ids
    pad_id = tokenizer.token_to_id("[PAD]")
    attention_mask = [0 if token == pad_id else 1 for token in input_ids]
    return attention_mask

def truncate_text_by_tokens(text, tokenizer, max_len):
    encoding = tokenizer.encode(text)
    input_ids = encoding.ids
    if len(input_ids) > max_len:
        print(f"Truncating input tokens from {len(input_ids)} to {max_len}.")
        truncated_ids = input_ids[:max_len]
        truncated_text = tokenizer.decode(truncated_ids)
        return truncated_text
    return text'''

def main():
    import os
    import soundfile as sf
    from TTS.api import TTS

    print("Loading TTS model...")
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

    #tokenizer = tts.synthesizer.tts_model.tokenizer.tokenizer

    text = "Hello, this is techno's voice! hehe HAHA!"
    #max_len = 25
    #text = truncate_text_by_tokens(text, tokenizer, max_len)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    speaker_wav = os.path.join(script_dir, "voices", "techn0.mp3")

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