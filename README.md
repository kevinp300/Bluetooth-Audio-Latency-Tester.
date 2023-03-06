# Bluetooth-Audio-Latency-Tester.
This implementation assumes that the source device is already streaming audio over Bluetooth using the audio UUID specified. It sends a request to start the audio stream, waits for it to start, and then records the time it takes to receive each audio sample. It then calculates the latency in terms of audio samples and milliseconds, assuming a sample rate of 44.1kHz.

Bluetooth audio latency can be affected by many factors, including the Bluetooth hardware and software on both devices, the distance between the devices, and the amount of other Bluetooth traffic in the area.
