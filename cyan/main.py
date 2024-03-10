import ast
import sys
from io import TextIOWrapper
from typing import Optional, Sequence

from cyan.errors import CyanError


class AssertVisitor(ast.NodeVisitor):
    def visit_Assert(self, node: ast.Assert):
        if isinstance(node.test, ast.BoolOp) and isinstance(node.test.op, ast.And):
            raise CyanError(
                node=node,
                message="Assert with 'and' found. Use multiple asserts instead.",
            )
        if node.msg is None:
            raise CyanError(
                node=node,
                message="Assert without message found.",
            )


def check_file(filename: str):
    with open(filename, "r") as file:
        tree = ast.parse(file.read(), filename=filename)
    visitor = AssertVisitor()
    try:
        visitor.visit(tree)
    except CyanError as e:
        print(f"{filename}:{e.node.lineno}:{e.node.col_offset}: {e.message}")
        sys.exit(1)


def main(argv: Optional[Sequence[str]] = None, stdin: Optional[TextIOWrapper] = None):
    arguments = argv if argv is not None else sys.argv[1:]
    for filename in arguments:
        check_file(filename)


if __name__ == "__main__":
    main()
