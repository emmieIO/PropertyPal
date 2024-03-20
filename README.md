# Project Installation Guide

Welcome to [PropertyPal]! Follow the steps below to set up the project on your local machine.

## Requirements

- Python version 3.11
- pip
- Git

## Installation Steps

### 1. Clone the Repository with your token
```bash
  git clone https://<token>@github.com/emmieIO/PropertyPal.git
```
### 2. setup a virtual environment 
  ```bash
  python -m venv .env
  source .env/Scripts/activate
```

### 3. Install Packages in in the requirements.txt
```bash
pip install -r requirements.txt
```
**Note:** If your virtual environment is not stored as *.env* please update the gitignore file with the name of your virtual env
