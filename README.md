
# Crime Solving Assistant Program

Author: Rachael Savage
Course: CSC370 - Artificial Intelligence (AI)
Date: 3/24/23
Python Version: 3.10.10 (64-bit)

---

## Introduction

The Crime Solving Assistant Program is designed to assist C.I.A. agents in enhancing their capabilities for finding suspects and analyzing images. This program utilizes the DeepFace library, OpenCV, and other Python libraries to perform various tasks related to image analysis and identification.

---

## Getting Started

### Prerequisites

Make sure you have the following Python packages installed:

- DeepFace (Install using `pip install deepface`)
- OpenCV (Install using `pip install opencv-python`)
- pandas (Install using `pip install pandas`)
- numpy (Install using `pip install numpy`)
- matplotlib (Install using `pip install matplotlib`)
- colorama (Install using `pip install colorama`)

### Installation

1. Clone this repository or download the source code files.
2. Ensure you have the required Python packages installed.
3. Run the program using `python main.py` or your preferred Python execution method.

---

## Program Features

### 1. Finding a Target Image (Option 1)

- This option allows agents to search for a target image in a database.
- The program will return results if a matching image is found.
- Results may include the person's name, age estimation, gender, and race.

### 2. Analyzing Images of Suspects (Option 2)

- Option 2 enables agents to analyze images for age, gender, and race estimation.
- Results are displayed in a tabular format, showing the possibilities for each attribute.
- The program also generates a CSV file named `people.csv` containing the analysis results.

### 3. Crime Rate Graph (Option G)

- Option G displays a bar chart comparing crime rates in four different cities.
- The cities included in the comparison are St. Louis (Missouri), Oakland (California), Memphis (Tennessee), and Detroit (Michigan).
- Crime types compared in the chart include murder, rape, robbery, and theft.

---

## Program Instructions

- When prompted, select one of the following options:
  - Option 1 (F): Find a target image in the database.
  - Option 2 (A): Analyze images for age, gender, and race.
  - Option G (G): Display a crime rate graph.

- Follow the on-screen instructions for each option.
- After completing an option, you can choose to restart the program.

---

## Enjoy using the Crime Solving Assistant Program!

This program is designed to assist C.I.A. agents in their investigative work. Explore its features and capabilities to enhance your crime-solving efforts.

