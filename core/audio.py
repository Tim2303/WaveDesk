import pyaudio
import wave

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
        data = wf.readframes(1024)
        while data:
            self.stream.write(data)
            data = wf.readframes(1024)

        # Stop stream
        self.stream.stop_stream()
        self.stream.close()

    def __del__(self):
        self.p.terminate()
