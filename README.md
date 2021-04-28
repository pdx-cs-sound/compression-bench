# Lossless Audio Compression Benchmarks
Bart Massey 2021

This is a benchmark of lossless audio compression
quality. (Compression means file size reduction here, not
the other thing.)
    
## What's Here

* `audio/*.wav`: 48KHz 16-bit mono `wav` files intended to
  be losslessly compressed with various audio encoders.

* `compression.sh`: Bourne shell script to run the
  compressors on the samples.

* `ratios.py`: Python program to show compression ratios.

## Compressors Used

* `gzip` 1.10 (`.gz`), `xz` 5.2.5, `zstd` 1.4.8: Lossless
  general-purpose compressors

* `flac` 1.3.3: [Free Lossless Audio Codec](https://xiph.org/flac/)

* `mac` 6.21 (`.ape`):
  [Monkey's Audio Codec](https://monkeysaudio.com/developers.html)

* `ffmpeg` 4.3.2 `alac` (`.alac`):
  [Apple Lossless Audio Codec](https://macosforge.github.io/alac/)

* `ffmpeg` 4.3.2 `mp4als` (`.mp4`):
  [MPEG-4 Audio Lossless Coding](https://macosforge.github.io/alac/) (ALS)

* `baco`: [Bad Audio Compressor](https://github.com/pdx-cs-sound/baco)

* `ffmpeg` 4.3.2 `mp3` (`.mp3`): MPEG-4 Layer 3 lossy audio codec
