# Hello World, I Made a Calculator! 🎉

Welcome to **Calculatore**—a simple command-line calculator with a unique feature: it understands words as operators. This is my first program and started as a fun experiment to see if I could build a simple calculator.

## How It Works

Calculatore performs arithmetic operations using either symbols or words. After each calculation, the result will be used as the starting point for the next calculation unless you type `"reset"`.

### Examples

- `1 plus 3.5`  
  Adds 3.5 to 1, resulting in 4.5.

- `divided by 6`  
  Divides the previous result (4.5) by 6, resulting in 0.75.

### Supported Operators

You can use the following operators:

- **Addition**: `plus` or `+`
- **Subtraction**: `minus` or `-`
- **Division**: `divided by` or `/`
- **Multiplication**: `times` or `*`

### Additional Commands

- `"reset"`: Resets the calculator to start fresh.
- `CTRL + C`: Exits the program.

## Installation

To install this calculator via Homebrew, you'll first need to tap the repository:

```bash
brew tap doribenba/calculatore https://github.com/doribenba/calculatore.git
brew install calculatore
 ```

## Usage

To start the calculator, simply run:

```bash
calculatore
 ```

Then enter your calculations directly in the terminal.

## Happy calculating!

## License

Anyone can use.
