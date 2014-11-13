# Demo

``
make
``

* Results in `result.out` and `plot.dat`

# Usage

``
python omniprop.py [graph filepath] [training filepath] [lambda]  > [result filepath]
python precision_at_p.py [result filepath] [test filepath] > [plot filepath]
``

* omniprop.py requires numpy/scipy

# File format

Make sure to start all node ids from 0.

## Graph file format

``
[src node id] [dst node id]
``

* See sample data file

## Training file format

``
[node id] [label id]
``

* Make sure to list labeled nodes on top, and unlabeled nodes on bottom.
* For unlabeled nodes, let [label id] = -1.
* See sample data file

## Training file format

``
[node id] [label id]
``

* Make sure to list only test nodes.
* See sample data file

## Result file format

``
[node id] [inferred label id]
``

## Plot file format

``
[precision@p] [p]
``
