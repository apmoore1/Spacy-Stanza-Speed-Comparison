#! /bin/sh

python -m spacy download en_core_web_lg
python -c "import stanza;stanza.download('en')"