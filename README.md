# Google Form Automation

A Python script for automating Google Form submissions with randomly generated data. This tool allows you to quickly submit multiple responses to a form for testing or data collection purposes.

## Features

- Automated form completion with randomly selected answers
- Customizable number of form submissions
- Parallel processing option for faster execution
- Visual browser automation with Chrome
- Comprehensive random data generation for all form fields

## Requirements

- Python 3.6+
- Chrome browser
- ChromeDriver (automatically managed by webdriver_manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/notcaliper/google-form-automation.git
   cd google-form-automation
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Update the `form_url` variable in the script with your target Google Form URL.

2. Run the script:
   ```
   python form_automation.py
   ```

3. When prompted:
   - Enter the number of form submissions you'd like to make
   - Choose whether to run submissions in parallel or sequentially
   - If running in parallel, specify how many browsers to run simultaneously

## How It Works

The script uses Selenium WebDriver to automate browser interactions:

1. Opens a Chrome browser and navigates to the Google Form
2. Fills in a random name and selects a random age group on the first page
3. Clicks the "Next" button to proceed to the second page
4. Selects random options for all questions on the second page
5. Submits the form
6. Repeats the process for the specified number of entries

## Customization

You can customize the script by:

- Modifying the lists of first and last names
- Changing the option arrays for different questions
- Adjusting wait times and browser settings
- Adding additional form pages or question types

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for legitimate testing purposes only. Please use responsibly and adhere to Google's terms of service. Excessive automated submissions may be considered spam and could result in IP blocking. 