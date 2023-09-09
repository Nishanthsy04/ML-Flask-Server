# ML-Flask-Server

ML-Flask-Server is a web application built with Flask that provides rainfall prediction for various Indian subdivisions using machine learning models.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Prerequisites
- Python (3.6 or higher)
- Pip (Python package manager)




## Install project dependencies:
sh
pip install -r requirements.txt
Run the Flask application:
sh
python app.py
Access the application in your web browser at http://localhost:5000.

## Usage
    Open the web application in your browser.
    Select the desired Month, Year, and Subdivision for which you want to predict rainfall.
    Click the "Predict" button to get the rainfall prediction for the selected criteria.

## Project Structure

    app.py: The Flask application that serves as the backend.
    models/: Directory containing trained machine learning models for each subdivision.
    rainfall_data.csv: Input data file containing historical rainfall data.
    templates/: HTML templates for rendering web pages.
    static/: Static files (CSS, JavaScript, etc.) for the web application.

## Contributing


    Fork the repository.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them.
    Push your changes to your fork.
    Open a pull request to the main branch of this repository.
