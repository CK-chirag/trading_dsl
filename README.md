## Trading_dsl
```bash
python demo.py
```
Output of demo.py
```bash
Generated DSL:
 ENTRY: close > sma(close,20) AND volume > 1000000
EXIT: rsi(close,14) < 30
{
  "entry": {
    "type": "binary_op",
    "op": "AND",
    "left": {
      "type": "binary_op",
      "op": ">",
      "left": {
        "type": "field",
        "value": "close"
      },
      "right": {
        "type": "indicator",
        "name": "sma",
        "params": [
          {
            "type": "field",
            "value": "close"
          },
          {
            "type": "number",
            "value": 20.0
          }
        ]
      }
    },
    "right": {
      "type": "binary_op",
      "op": ">",
      "left": {
        "type": "field",
        "value": "volume"
      },
      "right": {
        "type": "number",
        "value": 1000000.0
      }
    }
  },
  "exit": {
    "type": "binary_op",
    "op": "<",
    "left": {
      "type": "indicator",
      "name": "rsi",
      "params": [
        {
          "type": "field",
          "value": "close"
        },
        {
          "type": "number",
          "value": 14.0
        }
      ]
    },
    "right": {
      "type": "number",
      "value": 30.0
    }
  }
}
Trades: []
```

### DSL Grammar

The DSL is parsed using a formal grammar with Lark and consists of two required blocks:

ENTRY: <expression>
EXIT: <expression>

### Expressions
Expressions are built using:
- Boolean operators: `AND`, `OR`
- Comparison operators: `> < >= <= ==`

Example:
close > sma(close,20) AND volume > 1000000

### Values
A value can be:
- Field: `close`, `volume`
- Number: `20`, `1000000`
- Function call (indicator):
sma(close,20)
rsi(close,14)

The grammar is deterministic and produces an Abstract Syntax Tree (AST) for code generation and execution.
