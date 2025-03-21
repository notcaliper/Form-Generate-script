# Google Form Automation

A powerful Python script for automating Google Form submissions with randomly generated data. This tool allows you to quickly submit multiple responses to a form for testing, data collection, or demonstration purposes.

![Form Automation Demo](https://user-images.githubusercontent.com/example/form-automation-demo.gif)

## ✨ Features

- **Automated form completion** with randomly selected answers
- **Multi-page form support** - handles forms with multiple sections
- **Customizable submission count** - generate exactly the number of responses you need
- **Parallel processing** option for significantly faster execution
- **Visual browser automation** with Chrome
- **Rich random data generation** for all form fields
- **Performance optimizations** for faster form submissions
- **Detailed logging** to track submission progress

## 🔧 Requirements

- Python 3.6+
- Chrome browser
- Internet connection

## 📋 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/notcaliper/Form-Generate-script.git
   cd Form-Generate-script
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Update the `form_url` variable in the script with your target Google Form URL:
   ```python
   form_url = 'https://forms.gle/YOUR_FORM_ID'
   ```

2. Run the script:
   ```bash
   python form_automation.py
   ```

3. When prompted:
   - Enter the number of form submissions you'd like to make
   - Choose whether to run submissions in parallel or sequentially
   - If running in parallel, specify how many browsers to run simultaneously (1-5)

## ⚙️ How It Works

The script uses Selenium WebDriver to automate browser interactions:

1. Opens a Chrome browser and navigates to the Google Form
2. Fills in a random name and selects a random age group on the first page
3. Clicks the "Next" button to proceed to subsequent pages
4. Selects random options for all questions on each page
5. Submits the form after all questions are answered
6. Repeats the process for the specified number of entries

## 🛠️ Customization

You can customize the script by:

- **Modifying the name lists**: Edit the `first_names` and `last_names` arrays
- **Changing question responses**: Update the various option arrays for different questions
- **Adjusting browser settings**: Modify the Chrome options for different environments
- **Tuning performance**: Adjust wait times and parallel processing settings
- **Adding new question types**: Extend the script to handle additional form elements

## 🎯 Example Forms

The script has been tested with various Google Forms, including:
- Car preference surveys
- Event registration forms
- Customer feedback forms
- Quiz submissions
- Application forms

## 🔍 Troubleshooting

If you encounter issues:

1. Ensure Chrome is installed and up-to-date
2. Check that the form URL is correct and accessible
3. Try running with fewer parallel browsers
4. Increase wait times if the form has slow loading elements
5. Check the console output for detailed error messages

## 📄 License

MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for legitimate testing purposes only. Please use responsibly and adhere to Google's terms of service. Excessive automated submissions may be considered spam and could result in IP blocking.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💬 Support

For support, please open an issue in the GitHub repository. 