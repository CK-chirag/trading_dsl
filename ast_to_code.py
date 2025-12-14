def generate_expr(node, df="df"):
    if node is None:
        raise ValueError("AST node is None")

    if node["type"] == "binary_op":
        op = node["op"]

        if op == "AND":
            py_op = "&"
        elif op == "OR":
            py_op = "|"
        else:
            py_op = op

        return f"({generate_expr(node['left'])} {py_op} {generate_expr(node['right'])})"

    if node["type"] == "field":
        return f"{df}['{node['value']}']"

    if node["type"] == "number":
        return str(node["value"])

    if node["type"] == "indicator":
        name = node["name"]
        params = node["params"]

        # First argument (e.g. close)
        series = generate_expr(params[0], df)

        # Second argument (e.g. 20)
        period = int(params[1]["value"])

        if name == "sma":
            return f"{series}.rolling({period}).mean()"

        if name == "rsi":
            return f"{df}['rsi_{period}']"

    raise ValueError(f"Unknown AST node: {node}")
