# Automation with Python

Welcome to the "Automation with Python" repository! This collection of Python scripts is designed to automate various tasks, from data conversion and financial calculations to organizing your digital workspace and scheduling emails. Whether you're a seasoned developer or just starting, these projects will help streamline your workflow and save you valuable time.

## Prerequisites

To execute the code in this repository, you will need:

- **Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **IDE**: Any Integrated Development Environment (IDE) like PyCharm, VSCode, or Jupyter Notebook.

## Projects

### 1. CSV to PDF Converter

**Description**: This script converts CSV files into well-formatted PDF documents, adding titles and dates to enhance data presentation.

**Library Required**: `reportlab`

**Installation**:

```powershell
pip install reportlab
```

### 2. Dinar Converter

**Description**: Convert Tunisian Dinars (TND) to other major currencies (USD, CAD, EUR, AUD, CNY) using real-time exchange rates from the FreeCurrencyAPI.

**Libraries Required**: `requests`

**Installation**:

```powershell
pip install requests
```

**Additional Setup**: Generate an API key from the FreeCurrencyAPI website.

### 3. Directory Organizer

**Description**: This script sorts all files in a specified directory by their extensions into respective folders, ensuring a neat and organized directory structure.

**Libraries Required**: None (Uses Python's built-in `shutil` and `os` libraries).

### 4. Email Sender

**Description**: Schedule emails by specifying receivers, subject, date, time, and content. This tool uses Google's application-specific passwords for secure email automation.

**Library Required**: `schedule`

**Installation**:

```powershell
pip install schedule
```

### 5. Video Screenshot Capture

**Description**: Capture your PC screen, start and stop video recordings, and save the video in a chosen folder. Ideal for creating tutorials or recording presentations.

**Library Required**: `pyautogui`

**Installation**:

```powershell
pip install pyautogui
```

## Getting Started

1. **Make sure python is installed :**
    
    ```powershell
    python --version
    ```
    
2. **Clone the Repository**:
    
    ```powershell
    git clone https://github.com/yourusername/automation-with-python.git
    cd automation-with-python
    ```
    
3. **Run the Scripts**:

## Project Details

### 1. CSV to PDF Converter

**Usage**: Converts CSV files to PDFs with a title and date for better visualization.

**How to Run**:

- Ensure `reportlab` is installed.
- Modify the `csv_path`, `pdf_path`, and `title` variables as needed.
- Run the script to generate the PDF.

### 2. Dinar Converter

**Usage**: Converts TND to other currencies using the FreeCurrencyAPI.

**How to Run**:

- Ensure `requests` is installed.
- Obtain and set the API key.
- Run the script to get the conversion rates.

### 3. Directory Organizer

**Usage**: Organizes files in a specified directory by file type.

**How to Run**:

- Specify the path of the directory to be organized.
- Run the script to sort files into folders based on their extensions.

### 4. Email Sender

**Usage**: Schedules and sends emails automatically.

**How to Run**:

- Ensure `schedule` is installed.
- Set up the email details and schedule time in the script.
- Run the script to start the scheduling service.

### 5. Video Screenshot Capture

**Usage**: Captures your desktop screen and saves the video to a specified folder.

**How to Run**:

- Ensure `pyautogui` is installed.
- Run the script, and use the specified keys “s” to start and “q” to stop recording.
