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
                devices.append(dev_info['name'])
        return devices

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
    print(devices)

    am.play_sound("../audio/Sample1.wav", 2)

