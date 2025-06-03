[![View English Version](https://img.shields.io/badge/-View%20English%20Version-8A2BE2?style=for-the-badge&logo=googletranslate&logoColor=white)](README.md)



# آموزش راه‌اندازی Ollama و n8n در Google Colab برای مدل‌های هوش مصنوعی و اتوماسیون



## مقدمه

در این راهنما به صورت گام‌به‌گام نصب و اجرای **مدل‌های Ollama** (مانند Llama 3، Deepseek، Phi-3 و...) روی Google Colab و همچنین نصب و راه‌اندازی **n8n** (اتوماسیون و workflow engine پیشرفته با قابلیت اتصال به Ollama API و Google Drive) را آموزش می‌دهیم. 
تمام دستورات تست شده و برای Colab بهینه شده‌اند.

> برای اجرای این کد روی گوگل کولب از لینک زیر استفاده کنید
>
> https://colab.research.google.com/github/AttackThwarter/note-repo/blob/main/AI/google_colab/N8N/pouya_customize_n8n-ollama.ipynb



---

## فهرست مطالب
1. بررسی منابع GPU و رم
2. نصب Ollama در Colab (نه Google Drive)
3. اجرای سرویس Ollama و تست
4. دانلود مدل‌های مختلف Ollama
5. تست مدل‌ها (متن نمونه)
6. نصب و پیکربندی n8n (با Google Drive)
7. راه‌اندازی ngrok برای دسترسی خارجی به n8n
8. نکات و رفع اشکال

---

## ۱. بررسی منابع سیستم

قبل از هر کاری منابع Colab را بررسی کنید:

```python
!nvidia-smi           # نمایش جزییات GPU
!nvcc -V              # مشخصات CUDA
!free -h              # میزان حافظه رم
```

---

## ۲. نصب Ollama در محیط Colab (نه Google Drive)

به هیچ وجه Ollama را در Google Drive نصب نکنید چون سرعت و پایداری پایین می آورد و در پلن های رایگان  نیز امکان استفاده از آن به دلیل کمبود حجم درایو وجود ندارد.

```python
!apt-get update
!apt-get install -y curl wget

!curl -fsSL https://ollama.com/install.sh | sh

!ollama --version

!mkdir -p /tmp/ollama  # محل موقت برای مدل‌ها
```

---

## ۳. اجرای Ollama به صورت سرویس

Ollama باید دائماً در پس‌زمینه اجرا شود:

```python
import os, subprocess, time

os.environ["OLLAMA_MODELS"] = "/tmp/ollama"    # مدل‌ها در مموری Colab

with open('/tmp/ollama.log', 'w') as log_file:
    process = subprocess.Popen(
        ["ollama", "serve"],
        stdout=log_file,
        stderr=log_file,
        preexec_fn=os.setsid
    )

time.sleep(5)  # منتظر بمانید تا سرویس راه‌اندازی شود

# وضعیت اجرا
try:
    check_process = subprocess.run(
        ["ollama", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=10
    )
    if check_process.returncode == 0:
        print("✅ Ollama با موفقیت اجرا شد.")
        !tail -n 5 /tmp/ollama.log
    else:
        print("🚫 مشکل در راه‌اندازی Ollama:")
        print(check_process.stderr)
except subprocess.TimeoutExpired:
    print("⏰ زمان پاسخ‌دهی سر رفته. سرویس هم‌چنان ممکن است درحال اجرا باشد.")
    !tail -n 5 /tmp/ollama.log

print("\nآدرس سرویس محلی:")
print("http://127.0.0.1:11434")
```

---

## ۴. دانلود مدل‌های Ollama دلخواه

نمونه‌ای از مدل‌های مشهور:  
- deepseek:r1-8b  
- llama3:8b  
- phi3:mini  
- codellama:python  
- gemma:2b  

> برای دانلود هر مدل، کافی است تیک جلوی آن را بزنید، میتوانید با توجه به حجم فضای ذخیره گوگل کولب چند مدل را همزمان دانلود کنید

درصورت عدم یافتن مدل مورد نظر در بخش custom_models مدل ollama مورد نظر خود را با فرمت زیر وارد کنید:

```bash
deepseek:r1-8b
```

```bash
gemma3:27b
```

*حواستان به حجم مدل‌ها باشد (مثلاً ۴ الی ۵ گیگ برای ۸B)!*

---

## ۵. تست مدل‌ها با پرامپت دلخواه

> در این مرحله در صورت انتخاب گزینه run_test_prompt از تمام مدل های دانلود شده پرامپت شما پرسش و نتیحه نمایش داده میشود

فرض: مدل deepseek:r1-8b دانلود شده است.

پرامپت خود را در قسمت test_prompt: بنویسید :


اتفاقی که در جریان است :
```python
test_prompt = "یک ایده جالب به من بده"
!ollama run deepseek:r1-8b "$test_prompt"
```

---

## ۶. نصب و راه‌اندازی n8n (روی Colab با درایو)

> جهت ذخیره پایدار دیتا و workflowها، n8n را روی Google Drive اجرا کنید.


برای راه اندازی N8N روی گوگل کولب مراحل زیر را طی کنید

1. توکن ngrok خود را در کادر NGROK_AUTH_TOKEN قرار دهید
2. آدرس ذخیره اطلاعات N8N را در کادر gdrive_path قرار دهید (به صورت دیفالت n8n_data)
3. بلاک را ران کنید


### مراحل پشت پرده:

- **بررسی و نصب NodeJS**

```python
!node --version || (curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install -y nodejs)
```

- **نصب n8n:**

```python
!npm install n8n -g
```

- **ستاپ Google Drive:**  
در صورت درخواست دسترسی گوگل کولب به گوگل درایو تمام دسترسی ها را تایید کنید

**آدرس کامل فولدر درایو (مثلاً):**
```
/content/drive/MyDrive/n8n/
```

- **ساخت کانفیگ n8n و لینک به آن:**

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

## ۷. راه‌اندازی ngrok برای دسترسی خارجی به n8n

- ثبت نام و کپی توکن ngrok  
- نصب و راه‌اندازی:

```python
NGROK_AUTH_TOKEN = 'توکن خود را اینجا قرار دهید'
!pip install pyngrok
from pyngrok import ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
public_url = ngrok.connect(5678)  # پورت پیش‌فرض n8n
print("n8n URL:", public_url)
```

---

## ۸. اجرای n8n

در انتها اجرای n8n:

```python
!n8n start
```

پس از اجرا آدرس public_url را باز کنید.

---

## ۹. اتصال n8n به Ollama (API Call در workflow)

در n8n یک **HTTP Request node** اضافه کنید:
- میتوانید از خود نود ollama نیز استفاده کنید
- آدرس: `http://127.0.0.1:11434/api/generate`
- متد: `POST`
- Content-Type: application/json
- Body: 
```json
{
  "model": "llama3:8b",
  "prompt": "سلام Ollama!"
}
```
- خروجی این node را می‌توانید وارد مراحل دیگر چرخه کاری کنید.

---

## ۱۰. نکات و رفع اشکال عمومی

- بعضی مدل‌ها بخاطر محدودیت حافظه (RAM/VRAM) Colab ممکن است اجرا نشوند.
- اگر کانکشن n8n با ngrok قطع شد، Cell مربوط را مجدد اجرا کنید.
- در راه‌اندازی n8n روی Google Drive، همیشه مسیرها را چک کنید.
- برای کاهش مصرف دیسک: فقط مدل مورد نیاز را دانلود کنید.
- پوشه `database` و `config` را در Google Drive نگهدارید تا Workflowها ذخیره بماند.

---

## لینک‌های مفید

- [Ollama Official Docs](https://ollama.com)
- [n8n Docs](https://docs.n8n.io)
- [ngrok](https://dashboard.ngrok.com/get-started/your-authtoken)

---

### موفق باشید!  
هر سؤال یا نکته‌ای داشتی، اینجا بپرس :) 👇

## [chat](https://github.com/AttackThwarter/note-repo/discussions/1)