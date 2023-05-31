#!/bin/bash

function getpwd() {
    pwd | xsel -b
}

function timestamp() {
    echo $(date "+%Y-%m-%d_%H-%M-%S")
}

function find_duplicates_recursive() {
    # https://stackoverflow.com/questions/16276595/how-to-find-duplicate-filenames-recursively-in-a-given-directory-bash #
    find $1 -type f -printf '%p/ %f\n' | sort -k2 | uniq -f1 --all-repeated=separate
}

function remove_pdf_comments() {
    pdftk \"$1\" output - uncompress | sed '/^\/Annots/d' | pdftk - output out.pdf compress
}

function trim_image() {
    for i in $@; do
        basename=${i%.*}
        convert $i -trim $i
    done
}

function save_image_from_clipboard() {
    xclip -selection clipboard -target image/png -out > Screenshot_"$(date "+%Y-%m-%d_%H-%M-%S")".png
}

function sort_python_inputs() {
    xsel -b > sort.py && isort sort.py -d | xsel -b && rm sort.py
}
