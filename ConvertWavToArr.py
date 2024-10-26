# Make sure wav is Mono & Exported with Unsigned 8 bit PCM 
# Mono = Tracks -> Mix -> Mix Stero Down to Mono
# Export -> Export as Wav -> Save as type "Wav (Microsoft)" & Encoding: "Unsigned 8-bit PCM

import wave

# Open the .wav file
filename = "8bit_portal_radio.wav"
with wave.open(filename, 'rb') as wav_file:
    # Read audio data as frames (bytes)
    audio_frames = wav_file.readframes(wav_file.getnframes())
    # Convert bytes to integer list (unsigned 8-bit values)
    audio_samples = list(audio_frames)

# Generate C++ array format
output = "const int audio_samples[] PROGMEM = { " + ", ".join(map(str, audio_samples)) + " };"
#print(output)

with open("output_samples.txt", "w") as f:
    f.write(output)
    print(f"Sample Count = {len(output)}")
