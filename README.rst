Movie reviews, annotated for emotion classification
===================================================

This repository holds annotated training and test data used in the experiments
reported on in

    L. Buitinck, J. van Amerongen, E. Tan and M. de Rijke (2015).
    `Multi-emotion detection in user-generated reviews
    <https://www.researchgate.net/publication/272677182_Multi-Emotion_Detection_in_User-Generated_Reviews/links/54eb26230cf2f7aa4d5a63d4.pdf>`_.
    Proc. 37th European Conference on Information Retrieval (ECIR).

The data consists of amateur movie reviews, scraped from IMDB and annotated
for the project Searching Public Discourse of the University of Amsterdam (UvA)
and the Netherlands eScience Center (NLeSC).  We (the authors, UvA and NLeSC)
do not hold the copyrights to the original texts. You may use this data for
academic/research purposes.


Format
------

The revies are in the directory ``brat_format/``. The original text is in the
``*.txt`` files. Annotations are in the corresponding ``.ann`` files, in the
offset format produced by `Brat <http://brat.nlplab.org/>`_.

Preprocessed versions of the data, split for training and testing a classifier,
can be found in the files ``train.txt`` and ``test.txt``. These contain one
sentence per line, with labels at the end of each line. A single space
separates the labels from the text. Multiple labels are separated by
underscores. Where a sentence received no label, the string ``None`` appears.
(No label means no emotions assigned by the annotator; all sentences have been
annotated.)

The files were converted to the final format by::

    python $BRAT/tools/sentencesplit.py < ${review}.txt > ${review}.sentences
    python sentences_with_tags.py ${review}.sentences > ${review}.senttag

(where ``$BRAT`` is the Brat source directory).

Training/test set splitting is done by ``split_train_test.py``.


Citing
------

If you use this data for your own experiments, please cite us::

    @inproceedings{buitinck2015multi,
      author = {Lars Buitinck and Jesse van Amerongen and Ed Tan
                and Maarten de Rijke},
      title = {Multi-emotion detection in user-generated reviews},
      booktitle = {Proc. European Conference on Information Retrieval (ECIR)},
      year = 2015
    }
