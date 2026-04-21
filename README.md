# Quadratic Solver & NVDA Plotting

A collection of Python scripts and Jupyter notebooks for solving quadratic equations and analyzing NVDA stock data.

## Files

- **quadratic_solver.py** - Functional implementation of quadratic equation solver
- **quadratic_solver_notebook.py** - Non-functional version for Jupyter notebook (split into cells)
- **quadratic_solver.ipynb** - Jupyter notebook with quadratic solver
- **plot_nvda.py** - Script to plot NVDA stock price data
- **nvda_plot.png** - Generated plot of NVDA stock data

## Features

### Quadratic Solver
Solves equations of the form: ax² + bx + c = 0

Handles:
- Two distinct real solutions
- One repeated real solution
- Complex solutions
- Special cases (linear equations when a=0)

### NVDA Plotting
Generates visualization of NVDA stock price trends.

## Usage

### Running the Quadratic Solver
```bash
python quadratic_solver.py
```

### Running the NVDA Plot
```bash
python plot_nvda.py
```

### Using Jupyter Notebook
```bash
jupyter notebook quadratic_solver.ipynb
```

## Requirements

- Python 3.x
- math (standard library)
- Additional dependencies may be needed for plotting (matplotlib, etc.)

## License

MIT
