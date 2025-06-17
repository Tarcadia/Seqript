# Seqript (Sequence + Script)

A lightweight framework for executing structured scripts with nested operations.

## Features
- Define scripts as nested JSON structures
- Register custom engines for different operations
- Environment variable expansion support
- Sequential and parallel execution modes
- Extensible through engine contributions

## Documentation
- [Quick Start](@doc/quick_start.md)
- [Usage Guide](@doc/usage.md)
- [Project Structure](@doc/structure.md)

## Installation
`pip install seqript` (TODO: Add actual installation method)

## Example
```json
{
  "seq": [
    {"comment": "Starting operations"},
    {"sleep": 1},
    {"par": [
      {"cmd": ["echo", "Task 1"]},
      {"cmd": ["echo", "Task 2"]}
    ]}
  ]
}
```