# Audio Processing and Fourier Analysis

This project processes audio files, applies Fourier Transformations, and classifies them based on frequency characteristics.

## Features

- Load multiple audio files from the `All_Audio_Files/` directory.
- Compute the Fourier Transform (both custom implementation and SciPy's FFT).
- Compute magnitude spectra of audio signals.
- Shuffle and play a subset of audio files.
- Perform gender classification based on frequency analysis.
- Generate plots for signal waveforms and FFT results.

## Dependencies

Ensure you have the following Python libraries installed:

```bash
pip install numpy matplotlib scipy librosa sounddevice
```

## Usage

1. Place your audio files inside the `All_Audio_Files/` directory.
2. Run the script:

   ```bash
   python script.py
   ```

3. The program will:
   - Load the audio files.
   - Compute FFT and analyze frequency components.
   - Play random audio samples.
   - Perform gender classification.
   - Display relevant plots.

## License

This project is licensed under the MIT License.
