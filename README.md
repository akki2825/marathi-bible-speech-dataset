## Marathi Bible Speech Dataset


[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://github.com/akki2825/marathi-bible-speech-dataset/blob/master/LICENSE)


## Running

To scrape the Bible in Marathi, open jupyter notebook using:

```
jupyter notebook
```

go to `notebooks/scraper.ipynb` and find all the relevant information for scraping.

Once you get the audio&text files. You have to perform sentence-level alignment using:

```
python aligner.py -h
```

To chunk the audio files from the syncmap file (generated from the above script), run:

```
python audio_chunk.py -h
```

This will spit out audio chunk corresponding to the sentence-aligned text.
