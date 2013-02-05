shortpipe
=========

shortpipe reads urls from stdin and writes them to stdout after having
unshortened them.

Install
-------

    pip install shortpipe

Usage
-----

    cat urls.txt | shortpipe > new_urls.txt

If you have a bunch of CPUs you can parallelize the lookups with:

    cat urls.txt | shortpipe --processes 4 > new_urls.txt

License
-------

* CC0


