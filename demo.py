from nl_parser import nl_to_dsl
from dsl_parser import DSLParser, print_ast
from ast_to_code import generate_expr
from indicators import rsi
from backtest import backtest
import pandas as pd

df = pd.DataFrame({
    "date": pd.date_range("2023-01-01", periods=30),
    "close": range(100, 130),
    "volume": [900000, 1200000] * 15
})

df["rsi_14"] = rsi(df["close"])

english_input = """
Buy when the close price is above the 20-day moving average
and volume is above 1 million.
Exit when RSI(14) is below 30.
"""

dsl = nl_to_dsl(english_input)
print("Generated DSL:\n", dsl)

parser = DSLParser()
ast = parser.parse(dsl)
print_ast(ast)

entry_expr = generate_expr(ast["entry"])
exit_expr = generate_expr(ast["exit"])

entry_signal = eval(entry_expr, {"df": df})
exit_signal = eval(exit_expr, {"df": df})

trades = backtest(df, entry_signal, exit_signal)
print("Trades:", trades)
