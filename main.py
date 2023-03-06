import time
import bluetooth

# Bluetooth address of the source device
SOURCE_ADDRESS = '00:11:22:33:44:55'

# UUID of the audio service on the source device
AUDIO_UUID = '0000110B-0000-1000-8000-00805F9B34FB'

# Number of audio samples to use for latency measurement
SAMPLE_COUNT = 1000

# Initialize the Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((SOURCE_ADDRESS, 1))

# Send a request to start the audio stream on the source device
sock.send(b'1')

# Wait for the audio stream to start
time.sleep(1)

# Record the time it takes for audio data to be transmitted from the source device to the test tool
latencies = []
for i in range(SAMPLE_COUNT):
    start_time = time.time()
    data = sock.recv(1024)
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000
    latencies.append(latency_ms)

# Close the Bluetooth socket
sock.close()

# Display the results in terms of audio samples and milliseconds
sample_rate = 44100 # assuming 44.1kHz sample rate
latency_samples = sum(latencies) / SAMPLE_COUNT * sample_rate / 1000
latency_ms = sum(latencies) / SAMPLE_COUNT
print(f'Latency: {latency_samples:.2f} samples, {latency_ms:.2f} ms')
