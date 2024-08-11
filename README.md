# Navttc-Task-10-QR-Code-Generator


# QR Code Generator

## Description

This Python script generates a QR code from a user-provided URL and saves it as an SVG file. It also displays the QR code in the terminal. The script utilizes the `pyqrcode` library to create the QR code.

## Code

```python
import pyqrcode
from pyqrcode import QRCode

# String which represents the QR code
content = input("Enter Your URL: ")

# Generate QR code
url = pyqrcode.create(content)

# SVG file creation
file_name = input("Enter Your file name: ")
file_name = file_name + ".svg"
url.svg(file_name, scale = 5)

# Display the QR code in the terminal
print(url.terminal(quiet_zone=1))
```

## Steps

1. **Import Required Modules:**
   - Import the `pyqrcode` library and the `QRCode` class from `pyqrcode`.

2. **Get User Input:**
   - Prompt the user to input the URL they wish to convert into a QR code.

3. **Generate the QR Code:**
   - Use the `pyqrcode.create()` function to generate a QR code from the provided URL.

4. **Save the QR Code as an SVG File:**
   - Ask the user to input a file name, and save the generated QR code as an SVG file with the specified name.

5. **Display the QR Code in the Terminal:**
   - The QR code is displayed in the terminal using the `terminal()` method of the `QRCode` object.

## How to Run

1. **Ensure Python and Required Libraries are Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - Install the required `pyqrcode` library using the following command:
     ```bash
     pip install pyqrcode
     ```

2. **Save the Script:**
   - Save the provided Python code into a file named `10-QR Code.py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `10-QR Code.py` is saved.
   - Run the script using the following command:
     ```bash
     python 10-QR Code.py
     ```

4. **Enter URL and File Name:**
   - Input the URL you want to generate a QR code for and the desired file name when prompted.

5. **View Output:**
   - The QR code will be saved as an SVG file with the specified name, and it will also be displayed in the terminal.

## Example

- If you enter the URL `https://www.numl.edu.pk` and it will asks for the file name such as i have put  `Numl Website Link.svg`, the script will generate a QR code, save it as `Numl Webstie.svg`, and display it in the terminal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at  nasirsharifqasoori786@gmail.com

