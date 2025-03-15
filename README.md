# Advanced Python Calculator

An advanced calculator application built in Python demonstrating software engineering principles, design patterns, and comprehensive error handling and logging.

## Project Overview

This project implements a feature-rich calculator that goes beyond basic arithmetic to showcase good programming practices, modular design, and robust error management. The application serves as both a practical tool and an educational example of advanced Python concepts.

## Features

- **Comprehensive Mathematical Operations**
  - Basic arithmetic (addition, subtraction, multiplication, division)
  - Advanced operations (exponents, roots, logarithms, trigonometric functions)
  - Complex number support
  - Statistical functions

- **Memory Management**
  - Store, recall, and clear memory values
  - Support for multiple memory slots

- **History Tracking**
  - Record of all performed calculations
  - Ability to recall and reuse previous results

- **Error Handling**
  - Comprehensive exception handling
  - Detailed error messages
  - Graceful recovery from invalid inputs

- **User Interface**
  - Command-line interface
  - Clean and intuitive interaction

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShriyaSharma1122334455/Advance-Python-Calculator.git
   cd Advance-Python-Calculator
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Calculator

Execute the main script to start the calculator:

```bash
python main.py
```

## Usage Examples

### Basic Operations

Use the calculator for basic arithmetic operations like addition, subtraction, multiplication, and division.

### Advanced Operations

Perform advanced operations such as exponents, square roots, logarithms, and trigonometric functions.

### Using Memory Functions

Store values in memory, recall them later, add to stored values, and clear memory when needed.

### Working with History

Track calculation history and reuse previous results in new calculations.

## Architecture

### Design Patterns Implementation

This calculator implements several key design patterns to enhance code organization, maintainability, and extensibility:

#### 1. Strategy Pattern

The calculator uses the Strategy pattern to encapsulate different calculation algorithms and make them interchangeable. This allows for easy extension with new operations without modifying existing code.

#### 2. Singleton Pattern

The Logger class is implemented as a Singleton to ensure a single logging instance throughout the application, providing consistent logging behavior.

#### 3. Facade Pattern

The main Calculator class serves as a Facade, providing a simplified interface to the complex subsystem of operations, memory management, and history tracking.

#### 4. Command Pattern

Each operation is encapsulated as a Command object, allowing for operation history and potential undo functionality. This separates the request for an operation from its execution.

#### 5. Observer Pattern

The calculator uses the Observer pattern to notify components like the logger and history tracker when operations are performed, ensuring all systems remain synchronized.

### Logging Strategy

The calculator implements a comprehensive logging system to track operations, errors, and system states:

#### Logging Levels and Categories

- **DEBUG**: Detailed information for troubleshooting
- **INFO**: Regular operation information
- **WARNING**: Potential issues that don't prevent execution
- **ERROR**: Serious problems that prevent specific operations
- **CRITICAL**: Fatal errors that prevent application functioning

#### Log Format

Logs are stored in JSON format with the following information:
- Timestamp
- Log level
- Operation details (when applicable)
- Input values
- Result or error information
- Module and function information

#### Benefits of the Logging Strategy

1. **Debugging Aid**: Detailed logs help identify and fix issues quickly
2. **Performance Monitoring**: Track execution times for optimization
3. **User Behavior Analysis**: Understand how the calculator is used
4. **Audit Trail**: Maintain a record of all operations for reference
5. **Error Analysis**: Identify common errors for improved error handling

## Testing

The project includes comprehensive unit tests for all components:

```bash
# Run all tests
python -m unittest discover tests

# Run specific test category
python -m unittest tests.test_basic_ops
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Commit your changes (`git commit -m 'Add new feature'`)
6. Push to your branch (`git push origin feature/new-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
