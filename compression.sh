#!/bin/sh
rm -rf compressed
mkdir compressed
for f in audio/*.wav
do
    BASE="`basename -s .wav \"$f\"`"
    echo "$BASE"
    echo "  gzip"
    gzip < "$f" > compressed/"$BASE".gz
    echo "  xz"
    xz -e -9 < "$f" > compressed/"$BASE".xz
    echo "  zstd"
    zstd -19 < "$f" > compressed/"$BASE".zstd
    echo "  flac"
    flac -s -f --best -o compressed/"$BASE".flac "$f" 
    # echo "  brotli"
    # brotli -Z "$f" -o compressed/"$BASE".br
    echo "  mac"
    mac "$f" compressed/"$BASE".ape -c5000 >/dev/null 2>&1
    echo "  alac"
    ffmpeg -v 0 -i "$f" -acodec alac compressed/"$BASE".m4a
    echo "  mp4als"
    mp4alsRM23 -7 "$f" compressed/"$BASE".als >/dev/null
    echo "  baco"
    baco -p "$f" compressed/"$BASE".baco
    echo "  mp3"
    ffmpeg -v 0 -i "$f" -acodec mp3 compressed/"$BASE".mp3
done
