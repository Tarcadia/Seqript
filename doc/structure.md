# Project Structure

## Core Components
- `Seqript`: Main class that parses and executes scripts
- Engines: Modular operations (`cmd`, `seq`, `par`, etc.)
- Variable Expansion: `${var}` substitution system

## File Organization
```
seqript/
├── init.py
├── seqript.py # Main class
├── util/
│   └── expand_variable.py
└── engine/
    ├── init.py
    ├── cmd.py # Command execution
    ├── nop.py # No operation
    ├── par.py # Parallel execution
    ├── seq.py # Sequential execution
    └── contrib/ # Additional engines
        ├── sleep.py
        └── comment.py
```

## Extension Points
1. Add engines to `engine/contrib/`
2. Override default engines during initialization
3. Extend variable expansion patterns## Extension Points
