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

    text = "Hello, this is neil's voice! hehe HAHA!"
    #max_len = 25
    #text = truncate_text_by_tokens(text, tokenizer, max_len)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    speaker_wav = os.path.join(script_dir, "voices", "neil_1-30.mp3")

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




'''
Better Training Things:
==========================
🗣️ Neutral Sentences (Clarity & Phoneme Coverage)
Hello, my name is [your name], and this is my voice.

The quick brown fox jumps over the lazy dog.

She sells seashells by the seashore.

Peter Piper picked a peck of pickled peppers.

I saw a movie last night and it was amazing.

Tomorrow is a brand new day with endless possibilities.

Can you believe how fast time flies?

I enjoy reading books, watching movies, and spending time outdoors.

😄 Happy & Upbeat
Wow, this is incredible! I can't wait to try it out!

That’s one of the best things I’ve heard all week.

I'm really excited to be part of this project.

😐 Calm & Neutral
Please follow the instructions carefully to continue.

I understand. Let’s take it one step at a time.

The weather today is slightly cloudy with a chance of rain.

😠 Frustrated / Concerned
I told you not to press that button!

This doesn’t make any sense — what are we missing?

That’s really not what I expected to happen.

❓ Questions & Intonation Variety
What do you mean by that?

Are we really going to do this?

How long will it take to get there?
'''