from pydub import AudioSegment
import numpy as np

def convert_to_8bit(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    
    # Convert to mono
    audio = audio.set_channels(1)
    
    # Reduce sample rate to 11025 Hz (typical for 8-bit audio)
    audio = audio.set_frame_rate(11025)
    
    # Reduce bit depth to 8 bits
    samples = np.array(audio.get_array_of_samples())
    max_val = np.max(np.abs(samples))
    scale_factor = max_val / 127.0
    samples = (samples / scale_factor).astype(np.int8)

    # Create new audio segment with 8-bit samples
    eight_bit_audio = AudioSegment(
        samples.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=1,  # 8 bits = 1 byte
        channels=1
    )
    
    # Export the 8-bit audio as MP3
    eight_bit_audio.export(output_file, format='mp3', bitrate='64k')
    print(f"Converted {input_file} to 8-bit and saved as {output_file}")

# Usage example
convert_to_8bit("bongo.mp3", "bongo_output.mp3")
