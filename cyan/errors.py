import ast


class CyanError(Exception):
    def __init__(self, node: ast.AST, message: str):
        self.node = node
        self.message = message
