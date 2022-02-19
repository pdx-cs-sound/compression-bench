# Lossless Audio Compression Benchmarks
Bart Massey 2021

This is a benchmark of lossless audio compression
quality. (Compression means file size reduction here, not
the other thing.)
    
To run these benchmarks, you'll need to be on a Linux box
and install or comment out the compressors used in
`compression.sh`. You can then run `python3 ratios.py` to
get benchmark results.

For current benchmarks, see the bottom of this file.

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

* `flacq` 0.1.0: [Free Lossless Audio Compression by Quartile](https://github.com/BartMassey/flacq)

* `mac` 6.21 (`.ape`):
  [Monkey's Audio Codec](https://monkeysaudio.com/developers.html)

* `ffmpeg` 4.3.2 `alac` (`.m4a`):
  [Apple Lossless Audio Codec](https://macosforge.github.io/alac/)

* `mp4alsRM23` (`.als`):
  [MPEG-4 Audio Lossless Coding (ALS)](https://www.nue.tu-berlin.de/menue/research/research_topic/compression_and_transmission/mpeg_4_audio_lossless_coding_als/parameter/en/#c230252)

* `baco`: [Bad Audio Compressor](https://github.com/pdx-cs-sound/baco)

* `ffmpeg` 4.3.2 `mp3` (`.mp3`): MPEG-4 Layer 3 lossy audio codec

## Audio Files Provided

All audio tracks are by the benchmark author except 

* `00a-01sample.wav`: One zero sample.
* `00b-01sec.wav`: One second of zero samples.
* `00c-10sec.wav`: Ten seconds of zero samples.
* `01a-sine.wav`: 1KHz sine wave at -6dB.
* `01b-bigsine.wav`: 1KHz sine wave at 0dB.
* `02-overdrive.wav`: Sine wave through an overdrive plugin.
* `03-guitar.wav`: Acoustic guitar with minor peak clipping.
* `04-guitar-compressed.wav`: Guitar with moderate gain compression.
* `05-voice.wav`: Recorded speech.
* `06-synth.wav`: Soft synthesizer with high-frequency polyphony.

## Current Scores

    00a-01sample
                  00a-01sample.gz:      59  0.78×
                  00a-01sample.xz:     104  0.44×
                00a-01sample.zstd:      59  0.78×
                00a-01sample.flac:    8316  0.01×
               00a-01sample.flacq:      65  0.71×
                 00a-01sample.ape:     140  0.33×
                 00a-01sample.m4a:     737  0.06×
                 00a-01sample.als:      83  0.55×
                00a-01sample.baco:      missing
                 00a-01sample.mp3:     621  0.07×
    00b-01sec
                     00b-01sec.gz:     175 548.82×
                     00b-01sec.xz:     188 510.87×
                   00b-01sec.zstd:      65 1477.60×
                   00b-01sec.flac:    8438 11.38×
                  00b-01sec.flacq:      73 1315.67×
                    00b-01sec.ape:     140 686.03×
                    00b-01sec.m4a:    1015 94.62×
                    00b-01sec.als:      93 1032.73×
                   00b-01sec.baco:   14127  6.80×
                    00b-01sec.mp3:    8493 11.31×
    00c-010sec
                    00c-010sec.gz:    1015 945.86×
                    00c-010sec.xz:     312 3077.06×
                  00c-010sec.zstd:      94 10213.23×
                  00c-010sec.flac:    9604 99.96×
                 00c-010sec.flacq:      73 13151.29×
                   00c-010sec.ape:     140 6857.46×
                   00c-010sec.m4a:    3453 278.03×
                   00c-010sec.als:     198 4848.71×
                  00c-010sec.baco:  124236  7.73×
                   00c-010sec.mp3:   80493 11.93×
    01a-sine
                      01a-sine.gz:   16045  5.99×
                      01a-sine.xz:   10308  9.32×
                    01a-sine.zstd:   13178  7.29×
                    01a-sine.flac:   25906  3.71×
                   01a-sine.flacq:   23840  4.03×
                     01a-sine.ape:   13956  6.88×
                     01a-sine.m4a:   21844  4.40×
                     01a-sine.als:   10809  8.89×
                    01a-sine.baco:   27265  3.52×
                     01a-sine.mp3:    8493 11.31×
    01b-bigsine
                   01b-bigsine.gz:  150205  6.39×
                   01b-bigsine.xz:   88696 10.82×
                 01b-bigsine.zstd:  112388  8.54×
                 01b-bigsine.flac:  219915  4.37×
                01b-bigsine.flacq:  415821  2.31×
                  01b-bigsine.ape:  233724  4.11×
                  01b-bigsine.m4a:  436049  2.20×
                  01b-bigsine.als:  189797  5.06×
                 01b-bigsine.baco:  471218  2.04×
                  01b-bigsine.mp3:   80493 11.93×
    02-overdrive
                  02-overdrive.gz:   16553  5.80×
                  02-overdrive.xz:   10556  9.10×
                02-overdrive.zstd:   13610  7.06×
                02-overdrive.flac:   49870  1.93×
               02-overdrive.flacq:   24122  3.98×
                 02-overdrive.ape:   22564  4.26×
                 02-overdrive.m4a:   48749  1.97×
                 02-overdrive.als:   15032  6.39×
                02-overdrive.baco:   62127  1.55×
                 02-overdrive.mp3:    8493 11.31×
    03-guitar
                     03-guitar.gz: 2434169  1.16×
                     03-guitar.xz: 2030724  1.40×
                   03-guitar.zstd: 2340306  1.21×
                   03-guitar.flac: 1435625  1.97×
                  03-guitar.flacq: 1607627  1.76×
                    03-guitar.ape: 1323068  2.14×
                    03-guitar.m4a: 1461081  1.94×
                    03-guitar.als: 1362739  2.08×
                   03-guitar.baco: 2007042  1.41×
                    03-guitar.mp3:  236781 11.97×
    04-guitar-compressed
          04-guitar-compressed.gz: 2384950  1.05×
          04-guitar-compressed.xz: 2247964  1.11×
        04-guitar-compressed.zstd: 2385191  1.05×
        04-guitar-compressed.flac: 1531895  1.63×
       04-guitar-compressed.flacq: 1662874  1.50×
         04-guitar-compressed.ape: 1426174  1.75×
         04-guitar-compressed.m4a: 1555032  1.61×
         04-guitar-compressed.als: 1459492  1.71×
        04-guitar-compressed.baco: 2038826  1.22×
         04-guitar-compressed.mp3:  208660 11.97×
    05-voice
                      05-voice.gz:  392416  1.21×
                      05-voice.xz:  334616  1.42×
                    05-voice.zstd:  384952  1.23×
                    05-voice.flac:  259370  1.83×
                   05-voice.flacq:  293782  1.62×
                     05-voice.ape:  242812  1.96×
                     05-voice.m4a:  255914  1.86×
                     05-voice.als:  254760  1.87×
                    05-voice.baco:  342140  1.39×
                     05-voice.mp3:   40173 11.83×
    06-synth
                      06-synth.gz:  894143  1.13×
                      06-synth.xz:  845860  1.20×
                    06-synth.zstd:  892099  1.14×
                    06-synth.flac:  859668  1.18×
                   06-synth.flacq:  959109  1.06×
                     06-synth.ape:  604422  1.68×
                     06-synth.m4a:  856003  1.18×
                     06-synth.als:  342257  2.96×
                    06-synth.baco:  948205  1.07×
                     06-synth.mp3:   84954 11.93×
