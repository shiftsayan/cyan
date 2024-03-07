import ast
import sys

from cyan.errors import CyanError


class AssertVisitor(ast.NodeVisitor):
    def visit_Assert(self, node: ast.Assert):
        if isinstance(node.test, ast.BoolOp) and isinstance(node.test.op, ast.And):
            raise CyanError(
                f"Assert with 'and' found at line {node.lineno}: Use multiple asserts instead."
            )
        if node.msg is None:
            raise CyanError(
                f"Assert without a message found at line {node.lineno}: Always include a message."
            )


def check_file(filename: str):
    with open(filename, "r") as file:
        tree = ast.parse(file.read(), filename=filename)
    visitor = AssertVisitor()
    visitor.visit(tree)


def main():
    for filename in sys.argv[1:]:
        check_file(filename)


if __name__ == "__main__":
    main()
