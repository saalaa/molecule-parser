import pytest

from molecule_parser import parse_molecule, MoleculeParserError


def test_parse_molecule(chemical):
    input = chemical["input"]
    output = chemical["output"]

    assert parse_molecule(input) == output


def test_error(chemical):
    with pytest.raises(MoleculeParserError):
        parse_molecule("{H2]2")

    with pytest.raises(MoleculeParserError):
        parse_molecule("H2O-2")

    with pytest.raises(MoleculeParserError):
        parse_molecule("H2O0")

    with pytest.raises(MoleculeParserError):
        parse_molecule(" ")
