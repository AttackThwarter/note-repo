[![FA مشاهده نسخه فارسی](https://img.shields.io/badge/-%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D9%87%20%D9%86%D8%B3%D8%AE%D9%87%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-8A2BE2?style=for-the-badge&logo=googletranslate&logoColor=white)](README_fa.md)


# Guide to Setting Up Ollama and n8n in Google Colab for AI Models and Automation

## Introduction

This step-by-step guide will walk you through installing and running **Ollama models** (such as Llama 3, Deepseek, Phi-3, etc.) on Google Colab, as well as installing and setting up **n8n** (a powerful automation and workflow engine with support for Ollama API and Google Drive).  
All commands are tested and optimized for Colab.

> To run this code on Google Colab, use the link below:
>
> https://colab.research.google.com/github/AttackThwarter/note-repo/blob/main/AI/google_colab/N8N/pouya_customize_n8n-ollama.ipynb

---

## Table of Contents
1. Check GPU and RAM resources
2. Install Ollama in Colab (not Google Drive)
3. Run Ollama as a service and test
4. Download various Ollama models
5. Test models (sample prompt)
6. Install and configure n8n (with Google Drive)
7. Set up ngrok for external access to n8n
8. Tips and troubleshooting

---

## 1. Check System Resources

Before anything else, check Colab system resources:

```python
!nvidia-smi           # GPU details
!nvcc -V              # CUDA specs
!free -h              # RAM usage
````

---

## 2. Install Ollama in Colab Environment (Not Google Drive)

Never install Ollama in Google Drive, as it will significantly reduce speed and stability. Also, free plans don't have enough space for models.

```python
!apt-get update
!apt-get install -y curl wget

!curl -fsSL https://ollama.com/install.sh | sh

!ollama --version

!mkdir -p /tmp/ollama  # temporary model location
```

---

## 3. Run Ollama as a Service

Ollama needs to run continuously in the background:

```python
import os, subprocess, time

os.environ["OLLAMA_MODELS"] = "/tmp/ollama"    # use RAM for models

with open('/tmp/ollama.log', 'w') as log_file:
    process = subprocess.Popen(
        ["ollama", "serve"],
        stdout=log_file,
        stderr=log_file,
        preexec_fn=os.setsid
    )

time.sleep(5)  # wait for service to start

# Check status
try:
    check_process = subprocess.run(
        ["ollama", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=10
    )
    if check_process.returncode == 0:
        print("✅ Ollama started successfully.")
        !tail -n 5 /tmp/ollama.log
    else:
        print("🚫 Issue starting Ollama:")
        print(check_process.stderr)
except subprocess.TimeoutExpired:
    print("⏰ Timeout expired. Service might still be running.")
    !tail -n 5 /tmp/ollama.log

print("\nLocal service address:")
print("http://127.0.0.1:11434")
```

---

## 4. Download Desired Ollama Models

Popular models include:

* deepseek\:r1-8b
* llama3:8b
* phi3\:mini
* codellama\:python
* gemma:2b

> To download a model, simply check the box beside it. You can download multiple models based on available space in Colab.

If your model is not listed in `custom_models`, enter it manually in the format:

```bash
deepseek:r1-8b
```

```bash
gemma3:27b
```

*Note the size of models (e.g., 4–5 GB for 8B models)!*

---

## 5. Test Models with Custom Prompt

> If `run_test_prompt` is selected, your prompt will be tested on all downloaded models and results will be displayed.

Assuming deepseek\:r1-8b is downloaded.

Write your prompt in the test\_prompt section:

```python
test_prompt = "Give me an interesting idea"
!ollama run deepseek:r1-8b "$test_prompt"
```

---

## 6. Install and Set Up n8n (on Colab + Drive)

> To persist data and workflows, run n8n on Google Drive.

To install N8N on Colab:

1. Place your ngrok token in `NGROK_AUTH_TOKEN`.
2. Define a Drive path to store N8N data (default is `n8n_data`).
3. Run the block.

### Under the Hood:

* **Check and Install NodeJS**

```python
!node --version || (curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install -y nodejs)
```

* **Install n8n:**

```python
!npm install n8n -g
```

* **Set Up Google Drive:**
  Allow Colab to access your Google Drive when prompted.

**Example full folder path:**

```
/content/drive/MyDrive/n8n/
```

* **Create n8n Config and Link It:**

```python
import os

gdrive_full_path = '/content/drive/MyDrive/n8n'
config_dir = f"{gdrive_full_path}/config"
os.makedirs(config_dir, exist_ok=True)

n8n_config = f"""
module.exports = {{
  database: {{
    type: 'sqlite',
    logging: false,
    sqliteOptions: {{
      path: '{gdrive_full_path}/database/database.sqlite',
    }},
  }},
  executions: {{
    saveDataOnError: 'all',
    saveDataOnSuccess: 'all',
    saveExecutionProgress: true,
    saveManualExecutions: true,
  }},
  userManagement: {{
      isInstanceOwnerSetUp: true,
  }},
  diagnostics: {{
      enabled: false,
  }},
}};
"""
with open(f"{config_dir}/config.js", 'w') as f:
    f.write(n8n_config)
!ln -sf {config_dir}/config.js ~/.n8n/config.js
```

---

## 7. Set Up ngrok for External Access to n8n

* Sign up and copy your ngrok token
* Install and start:

```python
NGROK_AUTH_TOKEN = 'place your token here'
!pip install pyngrok
from pyngrok import ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
public_url = ngrok.connect(5678)  # default n8n port
print("n8n URL:", public_url)
```

---

## 8. Run n8n

Finally, run n8n:

```python
!n8n start
```

After it starts, open the `public_url`.

---

## 9. Connect n8n to Ollama (API Call in Workflow)

In n8n, add an **HTTP Request node**:

* You may also use Ollama's own node
* URL: `http://127.0.0.1:11434/api/generate`
* Method: `POST`
* Content-Type: application/json
* Body:

```json
{
  "model": "llama3:8b",
  "prompt": "Hello Ollama!"
}
```

* You can pass this node’s output to other workflow steps.

---

## 10. Tips and Common Issues

* Some models may not run due to Colab's RAM/VRAM limits.
* If n8n loses ngrok connection, re-run that cell.
* When using Google Drive for n8n, always verify paths.
* To save disk space: only download necessary models.
* Keep `database` and `config` folders in Drive to persist workflows.

---

## Useful Links

* [Ollama Official Docs](https://ollama.com)
* [n8n Docs](https://docs.n8n.io)
* [ngrok](https://dashboard.ngrok.com/get-started/your-authtoken)

---

### Good luck!

If you have any questions, ask here :) 👇

## [chat](https://github.com/AttackThwarter/note-repo/discussions/1)

