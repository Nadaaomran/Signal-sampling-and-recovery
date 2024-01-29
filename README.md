# Signal sampling and recovery
## Overview

Signal Sampling and Recovery Application is a desktop program developed to demonstrate the importance and validation of the Nyquist rate in signal processing. The application provides various features to interactively explore signal sampling, recovery, and related scenarios.

## Features

### Sample & Recover

- Load a signal.
- Visualize and sample the signal at different frequencies.
- Recover the original signal using the Whittaker–Shannon interpolation formula.
- Provide three graphs: 
  1. Original signal with markers for sampled points.
  2. Reconstructed signal.
  3. Difference between the original and reconstructed signals.

### Load & Compose

- Load signals from files or compose signals using a signal mixer.
- Signal mixer allows adding multiple sinusoidal signals with different frequencies and magnitudes and phase shifts.
- Ability to remove components during signal composition.
- Ability to edit an existing composed signal

### Additive Noise

- Noise addition to the loaded signal with a custom/controllable Signal-to-Noise Ratio (SNR) level.
- Visualize the dependency of noise effect on signal frequency.

### Real-time Processing

- Perform sampling and recovery in real-time upon user changes.
- No manual update or refresh buttons; changes are reflected instantly.

