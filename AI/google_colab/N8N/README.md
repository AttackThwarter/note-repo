[![مشاهده نسخه فارسی](https://img.shields.io/badge/-%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D9%87%20%D9%86%D8%B3%D8%AE%D9%87%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-8A2BE2?style=for-the-badge&logo=googletranslate&logoColor=white)](README_fa.md)



# Running Ollama and n8n on Google Colab

This Google Colab notebook allows you to set up and run Ollama (a platform for running large language models locally) and n8n (a workflow automation tool) within a Colab environment. n8n data is persisted to Google Drive, and ngrok is used to create a public tunnel to your n8n service.

## Prerequisites

* A Google account for using Colab and Google Drive.
* An ngrok authentication token (you can get one from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)).

## Notebook Structure and Usage Guide

The notebook is divided into several sections (cells). For best results, run the cells in order.

### Section 1: Check and Run GPU

* **Functionality:** This cell checks the status of the available GPU in the Colab environment, the CUDA version, and the system's free memory.
    ```python
    !nvidia-smi
    !nvcc -V
    !free -h
    ```
* **How to use:** Run this cell to ensure a GPU is correctly allocated and usable, especially if you plan to use larger Ollama models.

### Section 2: Install Ollama

* **Functionality:** This cell installs Ollama in the Colab environment.
    * Updates system packages (`apt-get update`).
    * Installs necessary tools like `curl` and `wget`.
    * Downloads and runs the official Ollama installation script.
    * Checks the installed Ollama version.
    * Creates a temporary directory (`/tmp/ollama`) to store Ollama models (to avoid filling up the main Colab storage).
    ```python
    !apt-get update
    !apt-get install -y curl wget
    !curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
    !ollama --version
    !mkdir -p /tmp/ollama
    ```
* **How to use:** Run this cell to install Ollama.

### Section 3: Run Ollama Service

* **Functionality:** This cell starts the Ollama service in the background.
    * Sets the `OLLAMA_MODELS` environment variable so models are stored in `/tmp/ollama`.
    * Runs the `ollama serve` service using `subprocess` in the background, saving logs to `/tmp/ollama.log`.
    * Waits a few seconds for the service to start.
    * Checks the service status by running `ollama list` and, if successful, displays a confirmation message and the last few lines of the logs.
    * Displays the Process ID (PID) of the Ollama service and the local access address (`http://127.0.0.1:11434`).
* **How to use:** Run this cell to start the Ollama service. After successful execution, Ollama will be ready to receive requests at the specified address.

### Section 4: Download Ollama Models

* **Functionality:** This cell allows you to download various large language models for Ollama.
    * Provides a list of predefined models (e.g., `llama3:8b`, `mistral:7b`, `phi3:mini`) with options to select them (True/False).
    * Allows you to enter custom model names for download (e.g., `vicuna:latest,orca-mini:3b`).
    * Includes an option to run a test prompt on the downloaded models.
    * Downloads the selected models using the `ollama pull {model_name}` command.
    * Displays a list of all downloaded models using `ollama list`.
    * If the test prompt option is enabled, it runs the specified prompt on each downloaded model, displays the response and response time, and saves the results to a text file.
* **How to use:**
    1.  Select the model(s) you want by setting the corresponding value to `True`.
    2.  If desired, enter custom model names in the `custom_models` field.
    3.  If you want to test the models, set `run_test_prompt` to `True` and enter a `test_prompt`.
    4.  Run the cell. Downloading models can take time depending on their size and your internet speed.

### Section 5: Setup and Run n8n

* **Functionality:** This cell installs, configures, and runs n8n, connects it to Google Drive for data storage, and creates a public URL for access via ngrok.
    1.  **User Inputs:**
        * `NGROK_AUTH_TOKEN`: Your ngrok authentication token. **This field is mandatory.**
        * `gdrive_path`: The name of the folder that will be created in your Google Drive to store n8n data (default: `n8n_data`).
        * `N8N_BASIC_AUTH`: If set to `True`, basic authentication for n8n will be enabled.
        * `N8N_USERNAME` and `N8N_PASSWORD`: Username and password for n8n basic authentication (if enabled).
    2.  **Install Packages:** Installs `pyngrok`.
    3.  **Connect to Google Drive:** Connects to your Google Drive account and creates the specified folder (e.g., `n8n_data`) under `My Drive` if it doesn't exist. It also creates `data` and `database` subfolders within it.
    4.  **Configure ngrok:** Sets up your ngrok token for authentication.
    5.  **Check and Install Node.js:** Checks the Node.js version and, if necessary, installs version 18 (or a compatible later version), as n8n requires it.
    6.  **Install n8n:** If n8n is not already installed, it installs it globally using `npm`.
    7.  **Create n8n Configuration File:** Creates an `config.js` file for n8n, setting the SQLite database path to the `database` folder in your Google Drive. If `N8N_BASIC_AUTH` is enabled, it also adds authentication settings.
    8.  **Create Symbolic Link:** Creates a symbolic link from the generated configuration file to the default n8n configuration path (`~/.n8n/config.js`).
    9.  **Start ngrok Tunnel:** Creates an ngrok tunnel for local port `5678` (n8n's default port) and displays the generated public URL.
    10. **Set Environment Variables for n8n:** Sets the necessary environment variables for n8n to run, including the `WEBHOOK_URL` using the public ngrok URL.
    11. **Start n8n:** Starts the n8n service in the background using `nohup n8n start`. n8n logs are saved to a file named `n8n.log` in your `gdrive_path` folder on Google Drive.
    12. **Display Access Information:** Displays the public n8n URL (via ngrok) and login credentials (if basic authentication is enabled).
    13. **Usage Instructions:** Provides tips on how to use Ollama models in n8n (using an HTTP Request node and the local Ollama API address: `http://localhost:11434/api/generate`).
    14. **Display n8n in IFrame:** Displays the n8n user interface directly in the Colab cell output within an IFrame.
    15. **View Logs Function:** Defines a Python function `view_logs()` that, when called, allows you to view the last 20 lines of the n8n and Ollama logs.
* **How to use:**
    1.  Enter your `NGROK_AUTH_TOKEN` in the respective field.
    2.  Optionally, change the `gdrive_path` folder name and n8n authentication settings.
    3.  Run the cell. This cell might take some time to complete all installation and setup steps.
    4.  After successful execution, the public n8n URL will be displayed. You can use this URL to access the n8n interface in your browser or use the IFrame directly in the cell output.
    5.  To use Ollama in your n8n workflows, use the `HTTP Request` node and send POST requests to `http://localhost:11434/api/generate` with the appropriate JSON body (e.g., `{"model": "your-model-name", "prompt": "your-prompt"}`).

## Important Notes

* **Keeping the Notebook Active:** For the Ollama and n8n services (and the ngrok tunnel) to remain active, this Colab notebook must be open and running. If the notebook is closed or its runtime in Colab ends, the services will stop.
* **Colab Limitations:** Google Colab has limitations on notebook runtime duration and resource usage. For long-term, uninterrupted use, consider other solutions like running these services on a personal server or VPS.
* **Security:** Your ngrok token is sensitive. Do not share it with others. If you use basic authentication for n8n, use a strong password.
* **Storage Space:** Large language models can consume significant disk space. Ensure you have enough space in Google Drive (for n8n data) and in the temporary Colab environment (for Ollama models). Ollama models will be deleted from the `/tmp/ollama` folder when the Colab session ends and will need to be re-downloaded in subsequent runs unless you implement a solution for persistent storage on Google Drive (not covered in this notebook).

## Troubleshooting

* **Error starting Ollama:** Check the Ollama logs at `/tmp/ollama.log`.
* **Error starting n8n:** Check the n8n logs in your `gdrive_path` on Google Drive (file `n8n.log`). You can also use the `view_logs()` function in the last cell.
* **ngrok connection issues:** Ensure your ngrok token is valid and correctly entered. Check the ngrok service status on your ngrok dashboard.
* **Ollama model not found:** Make sure you have successfully downloaded the desired model in Section 4 and are using its correct name in your API requests. You can see the list of available models by running `!ollama list` in a new cell.

---

This README is intended to provide a comprehensive guide for using your notebook. Feel free to edit and expand upon it as needed.
