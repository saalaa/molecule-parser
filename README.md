# molecule-parser

For a given chemical formula represented by a string, count the number of atoms
of each element contained in the molecule and return a dict.

For example:

    >>> parse_molecule('H2O')
    {'H': 2, 'O': 1}


## Installation

    $ pip install molecule-parser

## Development

Make sure you have a valid virtual environment:

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -U pip
    $ pip install -r requirements-dev.txt

### Running the tests

    $ pytest
