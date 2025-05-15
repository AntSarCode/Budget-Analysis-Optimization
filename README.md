# Budget Analysis

[![GitHub Release][release-badge]][release-link]  
[![Build Status][ci-badge]][ci-link]    
[![License: MIT][license-badge]][license-link]

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

[release-badge]: https://img.shields.io/github/v/release/yourusername/budget-analysis
[release-link]: https://github.com/yourusername/budget-analysis/releases
[ci-badge]:    https://img.shields.io/github/actions/workflow/status/yourusername/budget-analysis/ci.yml
[ci-link]:     https://github.com/yourusername/budget-analysis/actions

pip install pandas openpyxl
