# introduce_python_workshop_1

## Running Playwright Python Script to Automate Browser Actions

This repository contains a Python script that demonstrates how to use Playwright to automate browser actions, such as navigating to a website, performing a search, clicking a link, and taking a screenshot.

### Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.7 - 3.11. note do not use the 3.13 version
- `pip` (Python package manager)

#### Set Up a Virtual Environment (Recommended)

It is recommended to use a virtual environment to avoid conflicts with your system’s Python packages.

##### Creating a Virtual Environment

1. **Create the virtual environment**:
   Run the following command in your terminal (replace `myenv` with any name you like):

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/winstonisgood/python_introduction.git
2. Navigate to the cloned repository directory:
   ```bash
   cd introduce_python
3. Install the required Python packages using pip:
   ```bash
   pip install playwright
4. Install browser dependencies for Playwright:
   ```bash
   python -m playwright install

### Running the Script
1. Ensure you are in the repository directory where the Python script (script.py) is located.
2. Run the Python script:
   ```bash
   python browser_automation.py
   ```