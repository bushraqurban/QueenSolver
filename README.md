<h1 align="center">
        <img alt="QueenSolver Logo" width="400px" src="assets/logo.png">
</h1>

<div align="center">

[![Live Website Status](https://img.shields.io/badge/Live_App-View-1997B5&?style=for-the-badge&logo=license-MIT&logoColor=ffdd54)](https://queensolver.streamlit.app/)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)![License](https://img.shields.io/badge/license-MIT-1997B5&?style=for-the-badge&logo=license-MIT&logoColor=ffdd54)
</div>


![App Screenshot](assets/ui-screenshot.png)

A Streamlit-based visualization app that uses a **Genetic Algorithm** to solve the classic **N-Queens problem**. It’s a fun and interactive way to understand evolutionary algorithms in action!

---

## Features

- 🧬 Genetic Algorithm logic modularized for reusability
- 🎯 Real-time fitness evolution graph (with Plotly)
- 🖼️ Chessboard visual with queen images
- 🎛️ Sidebar to configure:
  - Number of Queens
  - Population Size
  - Mutation Rate
  - Number of Generations
- 🧠 Interactive explanation of GA concepts (via expanders)

---

## Project Structure

```
QueenSolver/
│
├── app.py               # Streamlit UI
├── assets/
│   └── queen.png        # PNG for the queen piece
├── ga/
│   ├── __init__.py
│   ├── algorithm.py       # Main GA logic
│   ├── board.py         # Board rendering logic
│   └── utils.py         # Helpers like fitness(), crossover(), mutation()
├── environment.yml      # Conda environment setup
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

```

---

## Setup Instructions

### Using Conda (recommended)

```bash
conda env create -f environment.yml
conda activate nqueens-ga
streamlit run app.py
```

### Or with pip

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## How It Works

The Genetic Algorithm evolves a population of potential board configurations by mimicking **natural selection**:

1. **Initialization**: Randomly shuffle queens on the board
2. **Fitness**: Score based on non-attacking queen pairs
3. **Selection**: Pick the fittest individuals
4. **Crossover**: Combine parents to produce offspring
5. **Mutation**: Swap queens to maintain genetic diversity

Goal: Maximize fitness to reach a solution with **zero conflicts**.

---

## Example Output

![Board Example](assets/ui-screenshot.png)
![Fitness Graph](assets/fitness_graph.png)

---