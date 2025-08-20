import pyaudio
import wave

CHUNK = 1024

class AudioManager:
    """
    Class for managing audio usage
    """
    
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None

    def get_output_devices(self):
        """Returns array of available sound sources."""
        devices = []
        for i in range(self.p.get_device_count()):
            dev_info = self.p.get_device_info_by_index(i)
            if dev_info['maxOutputChannels'] > 0:
                devices.append([dev_info['name'], i])
        return devices

    def get_input_devices(self):
        """Returns array of available microphones."""
        devices = []
        for i in range(self.p.get_device_count()):
            dev_info = self.p.get_device_info_by_index(i)
            if dev_info['maxInputChannels'] > 0:
                devices.append([dev_info['name'], i])
        return devices

    def play_to_microphone(self, file_path, microphone_index):
        try:
            wf = wave.open(file_path, 'rb')
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
            return None
        except wave.Error as e:
            print(f"Error: Wrong WAV-file format: {e}")
            return None

            # Output stream
        try:
            self.stream = self.p.open(
                format=self.p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                frames_per_buffer=CHUNK,
                output_device_index=microphone_index
            )
        except OSError as e:
            print(f"Failed to open stream on device with index {microphone_index}: {e}")
            print("Maybe you set wrong index or device doesn't support audio file parameters")
            self.p.terminate()
            return None

        print(f"Playing '{file_path}' into {microphone_index}...")

        # Read data from file and put to stream
        while data := wf.readframes(CHUNK):
            self.stream.write(data)

        # Finish work
        self.stream.stop_stream()
        self.stream.close()
        wf.close()

        return None

    def play_sound(self, file_path, output_device_index=None):
        """Play sound file (wav)."""
        try:
            wf = wave.open(file_path, 'rb')
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return

        # Open play stream
        self.stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                                  channels=wf.getnchannels(),
                                  rate=wf.getframerate(),
                                  output=True,
                                  output_device_index=output_device_index)

        # Read and play data
        data = wf.readframes(CHUNK)
        while len(data := wf.readframes(CHUNK)):
            self.stream.write(data)

        # Stop stream
        self.stream.stop_stream()
        self.stream.close()

    def __del__(self):
        self.p.terminate()

if __name__ == "__main__":
    am = AudioManager()
    devices = am.get_output_devices()
    micros = am.get_input_devices()
    print(devices)
    print(micros)

    # am.play_sound("../audio/Sample1.wav", devices[0][1])
    # Select VB Cable
    cable_in = None
    for x in devices:
        if "CABLE Input" in x[0]:
            cable_in = x[1]
            break

    if cable_in:
        am.play_to_microphone("../audio/Sample1.wav", cable_in)

