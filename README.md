# AI Calculator Automation 🤖🧮

This Python project automates the Windows Calculator using AI-powered natural language processing! It interprets natural prompts (like "add 1 and 5") and simulates keypresses to perform the operation.

## 🌟 Features
- Natural language interpretation of commands using Hugging Face's **BART-large-MNLI** model.
- Automatic keypress simulation for Calculator on Windows.
- No third-party automation libraries – uses native Python capabilities.

---

## 📦 Installation & Setup  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-calculator-automation.git
cd ai-calculator-automation
```

###2️⃣ Create and Activate a Virtual Environment
```bash
conda create --name myenv python=3.11
conda activate myenv
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 🚀 Running the Project
```bash
python main.py
```

- The script will prompt you to enter a natural command (e.g., "add 7 and 3").
- It will open the Windows Calculator and perform the operation.

# **Happy Coding**
