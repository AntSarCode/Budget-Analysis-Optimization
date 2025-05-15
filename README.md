# Budget Analysis

[![PyPI version](https://img.shields.io/pypi/v/budget-analysis)](https://pypi.org/project/budget-analysis)  
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Analyze your “Monthly Joint Expenses” block in an Excel file, compare each line-item against target budget percentages, and get spending recommendations.

---
## Features

- 🔍 Reads an Excel sheet and locates your “Monthly Joint Expenses” section.  
- 📊 Computes each category’s share of the total joint expenses.  
- ✂️ Compares actual percentages against your predefined targets.  
- 💡 Prints clear recommendations on which categories to trim.  

## Prerequisites

- Python 3.8 or higher  
- [pandas](https://pandas.pydata.org/) (for data handling)  
- [openpyxl](https://openpyxl.readthedocs.io/) (for reading `.xlsx` files)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/budget-analysis.git
   cd budget-analysis
