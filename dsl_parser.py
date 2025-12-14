from lark import Lark, Transformer
import os
import json

class DSLTransformer(Transformer):
    def start(self, items):
        return {"entry": items[0], "exit": items[1]}

    def entry_block(self, items):
        return items[0]

    def exit_block(self, items):
        return items[0]

    def or_op(self, items):
        return {"type": "binary_op", "op": "OR", "left": items[0], "right": items[1]}

    def and_op(self, items):
        return {"type": "binary_op", "op": "AND", "left": items[0], "right": items[1]}

    def comparison(self, items):
        return {
            "type": "binary_op",
            "op": items[1].value,
            "left": items[0],
            "right": items[2]
        }

    def function_call(self, items):
        return {
            "type": "indicator",
            "name": items[0].value,
            "params": items[1]
        }

    def arg_list(self, items):
        return items

    def var(self, items):
        return {"type": "field", "value": items[0].value}

    def num(self, items):
        return {"type": "number", "value": float(items[0].value)}


class DSLParser:
    def __init__(self, grammar_file="grammar.lark"):
        base_dir = os.path.dirname(__file__)
        grammar_path = os.path.join(base_dir, grammar_file)

        with open(grammar_path, "r") as f:
            grammar = f.read()

        self.parser = Lark(grammar, parser="lalr", transformer=DSLTransformer())

    def parse(self, dsl_text):
        return self.parser.parse(dsl_text)


def print_ast(ast):
    print(json.dumps(ast, indent=2))
