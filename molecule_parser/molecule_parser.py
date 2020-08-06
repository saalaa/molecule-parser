import os

from lark import Lark, Transformer, UnexpectedInput

GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), "formula.g")

with open(GRAMMAR_FILE) as file:
    GRAMMAR = file.read()


class MoleculeParserError(Exception):
    def __init__(self, line, column):
        self.line = line
        self.column = column

        message = "Error at line {} column {}".format(self.line, self.column)

        super().__init__(message)


class FormulaTransformer(Transformer):
    def element(self, tree):
        return "".join(tree)

    def index(self, tree):
        return int("".join(tree), base=10)

    def term(self, tree):
        """Transform a term.

        As defined in our grammar, a term can be an element or a formula
        followed by an optional index.

        Both cases are handled here.

        See: formula.g
        """
        index = 1
        if len(tree) == 2:
            index = tree[1]

        if isinstance(tree[0], dict):
            return {k: v * index for k, v in tree[0].items()}

        return {tree[0]: index}

    def formula(self, tree):
        """Transform a formula

        As defined in our grammar, a formula is composed of several terms so
        they are aggregated. Repeating elements are added up together.

        See: formula.g
        """
        result = {}

        for subtree in tree:
            for k, v in subtree.items():
                if k not in result:
                    result[k] = v
                else:
                    result[k] += v

        return result


def parse_molecule(formula):
    """Parse a molecule formula into a dictionary counting individual elements.

    >>> parse_molecule('H2O')
    {'H': 2, 'O': 1}
    """
    lark = Lark(GRAMMAR)

    try:
        tree = lark.parse(formula)
    except UnexpectedInput as e:
        raise MoleculeParserError(e.line, e.column)

    return FormulaTransformer().transform(tree)
