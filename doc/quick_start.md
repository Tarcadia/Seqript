# Quick Start

## Basic Usage

1. Create a script file (`example.json`):
```json
{
  "seq": [
    {"comment": "My first script"},
    {"sleep": 2},
    {"cmd": ["echo", "Hello World"]}
  ]
}
```

2. Execute it:
```python
from seqript import Seqript

seqript = Seqript(name="example")
with open("example.json") as f:
    seqript(**json.load(f))
```

## Available Engines
- `seq`: Sequential execution
- `par`: Parallel execution
- `cmd`: Command execution
- `nop`: No operation
- `sleep`: Delay execution
- `comment`: Print message