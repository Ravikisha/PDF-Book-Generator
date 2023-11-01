# PDF Book Generator 📚

PDF Book Generator is a Flutter project that allows you to generate Android and iOS applications for reading PDF books. Create mobile book applications from your PDF files effortlessly.

🚀 **Open for Contribution** - We welcome contributors to enhance PDF Book Generator!

[![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Features

- 📚 Generate Android and iOS applications from PDF files.
- 🖼️ Customize app icons easily using the Android Asset Studio.
- 📂 Organize your PDFs in the 'assets' folder within the 'pdf_book' directory.
- 🚀 Simplified script execution for building the app.
- 📦 Exported Android application in the 'release' folder.
- 📱 Install the generated app on your Android device.
- 🚀 Potential to release your app on the Google Play Store.

## Usage

To create your own PDF book application, follow these steps:

1. **Generate App Icons:**

   - Visit [Android Asset Studio](https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html).
   - Design and download your app icons.
   - Copy the icon files to the `logos` folder, replacing the previous icons.

2. **Add PDF Files:**

   - Create a folder named `assets` inside the `pdf_book` directory.
   - Copy your PDF files into the 'assets' folder.

3. **Run the Script:**

   - Execute the `run.bat` (for Windows) or `run.ps1` (PowerShell) script using your terminal.
    ```cmd
       ./run.bat
    ```
   - Follow the instructions and provide the name and filename of the PDF book when prompted.

4. **Build the Application:**

   - The script will build the PDF book application for Android.
   - Find the generated Android application in the `release` folder.

5. **Install on Android:**

   - Transfer the generated APK file to your Android device.
   - Install the app on your device.

6. **Release on Play Store:**

   - You have the option to release your application on the Google Play Store.

## Contributing

We encourage contributions! If you'd like to contribute to PDF Book Generator, please review the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines and instructions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Create your mobile book applications effortlessly with PDF Book Generator! 📱📖
