# Spacy-Stanza-Speed-Comparison
Comparison of Spacy and Stanza with respect to speed.

## Stanza

By default Stanza stores all of it's models at the following directory `~/stanza_resources` to specify a different directory see the [downloads](https://stanfordnlp.github.io/stanza/download_models.html) and [pipeline](https://stanfordnlp.github.io/stanza/pipeline.html) documentation.

## Installation/Requirements

Requires python>=3.6.1 and the following pips `pip install -r requirements.txt`. In addition we will need to download the English pre-trained models for both Spacy and Stanza via the [`download_models.sh` script](./download_models.sh):
```bash
./download_models.sh
```

This downloads the default English Stanza model and the large Spacy model.

We are going to use two different sources of data one is the Jane Austin Emma book from project Gutenberg and the second are some wine reviews both downloaded via NLTK using [download_data.sh script](./download_data.sh):
```bash
./download_data.sh
```

A quick analysis of the Emma and wine reviews can be seen within the [./overview_of_datasets.ipynb notebook](./overview_of_datasets.ipynb). In overview it shows the Emma book contains 2427 paragraphs with a median paragraph length in character of 234. The wine reviews are more like sentences and will be treated as such for this analysis of which there are 1230 sentences with a median length in characters of 96.

## Speed tests

Here we shall compare both Spacy and Stanza on the two different datasets (Jane Austin Emma book and wine reviews).
