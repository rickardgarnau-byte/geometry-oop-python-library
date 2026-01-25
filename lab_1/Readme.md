# 🧬 DNA Sequence Parser & Visualizer

A Python-based tool for parsing raw DNA sequence data (FASTA format), analyzing nucleotide frequencies, and visualizing the results.

**Project Type:** Foundational Data Engineering / Bioinformatics  
**Status:** Completed (Educational Project)

---

## 📖 About the Project

This project was developed as part of my early Python studies to master fundamental data handling concepts. The goal was to build a script capable of ingesting unstructured raw text files containing DNA sequences, parsing the relevant data, and performing basic aggregation and visualization.

While the dataset is biological, the core logic mirrors standard **ETL (Extract, Transform, Load)** processes used in Data Engineering:

1.  **Extract:** Read raw data from text files (`.txt`).
2.  **Transform:** Clean strings, handle multi-line sequences, and aggregate counts using dictionaries.
3.  **Load/Visualize:** Present the aggregated metrics using `matplotlib`.

## 🛠️ Tech Stack & Concepts

- **Python 3.12**
- **Matplotlib** (Data Visualization)
- **File I/O** (Reading/Parsing text streams)
- **Data Structures** (Dictionaries for aggregation)
- **String Manipulation** (Data cleaning)

## 📂 Project Structure

- `dna_sequence_analysis.ipynb`: The main Jupyter Notebook containing the logic.
- `dna_raw.txt`: Simple input dataset (single line sequences).
- `dna_raw_complicated.txt`: Complex input dataset (multi-line sequences requiring state management).

## 🚀 How It Works

The script iterates through the input file line-by-line to handle memory efficiently:

1.  **Detection:** Identifies sequence headers (lines starting with `>`).
2.  **State Management:** When a new header is found, it processes and visualizes the _previous_ sequence before resetting counters.
3.  **Aggregation:** It reads DNA strands (A, C, G, T) spanning multiple lines, sanitizes the input (stripping whitespace/casing), and updates frequency counts.
4.  **Visualization:** Generates a bar chart for each sequence ID found in the file.

## 🧠 Reflections & Learnings

_From the development process:_
This project was a significant exercise in logic flow control. Initially, handling sequences that spanned multiple lines was a challenge. I had to implement logic to "remember" the current sequence state while reading the file line-by-line.

I utilized external resources (documentation and tutorials) to refine the file reading loop, ensuring the script handles file pointers correctly and closes resources efficiently using `with open(...)`.

## 📊 Example Output

The script produces bar charts for each sequence detected:

- **X-Axis:** Nucleotides (A, C, G, T)
- **Y-Axis:** Frequency Count

## 💿 Installation & Usage

1.  Clone the repo:
    ```bash
    git clone [https://github.com/din-github-user/python-bioinformatics-basics.git](https://github.com/din-github-user/python-bioinformatics-basics.git)
    ```
2.  Install dependencies:
    ```bash
    pip install matplotlib
    ```
3.  Run the notebook or script to process the text files.

---

**Author:** Rickard Garnau
