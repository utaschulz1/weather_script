# Weather and outfit suggestion script in Python with API requests


This CLI tool fetches weather data for a given city (input prompt) and suggests an appropriate outfit based on the weather conditions.

- [What the CLI tool does](#what-the-script-does)
- [Prerequisites](#prerequisites)
- [Getting started](#getting-started)
- [Notes for beginners](#notes-for-beginners)
  - [Coding setup](#coding-setup)
  - [Download and install Python](#download-and-install-python)
  - [About virtual environment](#about-virtual-environment)
  - [Get API keys and keep them safe](#get-api-keys-and-keep-them-safe)
  - [Files in your repository](files-in-your-repository)

## What the CLI tool does

The CLI tool queries the OpenCage geocoder to get the latitude and longitude of the input city and feeds it into the Open-Meteo request for current weather data.

The output is turned into a prompt to request outfit suggestions from OpenAI.

The output will be written into the .md file weather_response.md.

## Prerequisites
- Python (I used Python 3.9.7).
- A terminal or command-line interface (e.g., Command Prompt, Git Bash, or Terminal).
- Git (to clone the repository).
- If you are a total beginner, see [Notes for beginners](##notes-for-beginners) below.

## Getting started

1. Fork this repository account using the ```fork``` button to copy it to your GitHub account.
2. Clone the repository from your account to your computer and open it:
   ```
   git clone https://github.com/your-username/your-repo-name.git

   cd your-repo-name
   ```
3. Create a virtual environment:
   
      ```python -m venv venv```
4. Activate the virtual environment:

    - On Windows:
  
        ```venv\Scripts\activate```

    - On macOS/Linux: 
  
        ```source venv/bin/activate```
5. Install the required dependencies listed in the ``requirements.txt`` file:
    ```
    pip install -r requirements.txt
    ```
6. Open the .env file and add your API keys:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    OPENCAGE_API_KEY=your_opencage_api_key_here
    ```
7. Run the program
   
    ```
    python call-weather-api.py
    ```
## Notes for beginners

You need to download this repository to your computer as described in step 2 in order to use it. The following are the prerequisites you need to run this script locally on your computer.

### Coding setup
Apart from Python itself, you will need Git and a command line interface (CLI). This, for two reasons: 
- You need to interact with GitHub using Git commands.
- You need to interact with Python and your repository folder using a command line interface, like bash or terminal. The CLI is the place where you type in all the commands above.

> ⚠️ **Warning:** There is no undo button in the command line interface, no CTRL+Z. It interacts directly with your computer. You have to understand what you are doing.

**Text editor**

If you're new to using a CLI and Git, consider familiarizing yourself with a text editor such as VS Code or Sublime Text first. 
This will help you in three ways:
- You can read and write code in your repository files.
- You have one or more command lines integrated in the editor. You just need one. You use it to set up your environment, that is, to install program packages and to run your code.
- You can use extensions (plugins) to make interacting with GitHub more streamlined.
   
Here are some resources to help you get started:
- [Getting started with Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics)
- [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (typically preinstalled on Linux and macOS)
- [Basic Command Line Commands](https://www.codecademy.com/articles/command-line-commands)

### Download and install Python

If you don't have Python installed yet, go to [Python.org](https://www.python.org/) and download and install it for your operating system. 

During installation:
- Check the box that says: "Add Python to PATH". This ensures that the Python executable and its tools (like ``pip``) are accessible from the command line (CLI) without needing to specify their full file paths.
- Select the option to install Python for all users (if applicable).
  
After installation, verify Python is installed by opening a terminal and running:
```
python --version
pip --version
```
You should see the versions in your command line.

### About virtual environment

> **Note:** Don't install the packages from the requirements.txt file just yet.

It is good practice to install additional Python packages in the local project folder (created in step 2) using a virtual environment (see step 3). 

This is what you need to know to begin with:

- A virtual environment creates an isolated Python environment for your project. This ensures that:
  - Dependencies for one project don't interfere with others.
  - You don't accidentally modify the global Python environment.
- The virtual environment functionality ``venv`` comes preinstalled with the Python installation. You can type the ``venv`` commands into the CLI as instructed when you are ready for the [Getting started](#getting-started).
- The package installation functionality ```pip``` also comes preinstalled with the Python environment. You can type the ``pip`` command into the CLI as instructed above when you are ready for the [Getting started](#getting-started).
- When you are finished working in your project environment, you need to deactivate your virtual environment with ``deactivate``.
  - The virtual environment is only active in the terminal session where it was activated. If you close the terminal, the virtual environment is automatically deactivated.

### Get API keys and keep them save

You need two API keys to write into the .env file. You get them on the respective website:

- OpenCage: https://opencagedata.com/api#quickstart (account required)
- OpenAI: https://platform.openai.com/api-keys (account required)
- Open-Meteo does not require an API key.

Now you are ready to open the .env file in your text editor and add the keys as instructed in step 6. 

> **Warning:** To protect your API keys, ensure the `.env` file is excluded from version control by adding it to a `.gitignore` file. 

This repository already includes a `.gitignore` file that excludes the `.env` file. You don't need to do anything extra, but here's how it works:
 - The `.gitignore` file tells Git to ignore certain files and folders, so they are not tracked or uploaded to GitHub.
 - This prevents sensitive information, like your API keys, from being exposed publicly.
 - You can view the `.gitignore` file in the root of the repository to see what is excluded.

If you accidentally commit your `.env` file, remove it from Git tracking with the following command:
```bash
git rm --cached .env
```
### Files in your repository

``` 
weather_script/
├── llm_utils.py          # Functions related to LLM requests (e.g., OpenAI API)
├── weather_utils.py      # Functions related to weather data (e.g., Open-Meteo, OpenCage)
├── call-weather-api.py   # Main script to orchestrate the program
├── requirements.txt      # Dependencies
├── .env                  # API keys
├── weather_response.md   # Output file (generated by the script)