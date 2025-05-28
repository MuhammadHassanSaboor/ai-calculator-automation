from transformers import pipeline
import re, os, time, ctypes

# User prompt
prompt = input("Enter a command (e.g., 'add 1 and 5'): ")

# Step 1: AI extraction
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
candidate_labels = ["add", "subtract", "multiply", "divide"]
result = classifier(prompt, candidate_labels)

# Extract scores and labels
labels = result["labels"]
scores = result["scores"]

# Improved operation detection
operation = None
# First, check if a keyword exists in the prompt
for label in candidate_labels:
    if label in prompt.lower():
        operation = label
        break

# If no keyword found, fallback to top prediction
if not operation:
    operation = labels[0]
    confidence = scores[0]
    # Optional: check confidence
    if confidence < 0.5:
        print("I'm not confident about the operation. Please try again.")
        exit()

# Extract numbers from prompt
numbers = list(map(int, re.findall(r'\d+', prompt)))
if len(numbers) < 2:
    print("Please provide at least two numbers for the operation.")
    exit()

print(f"Detected operation: {operation}, numbers: {numbers}")

# Step 2: Open Calculator
os.system('start calc')
time.sleep(1)

# Step 3: Key simulation
VK_CODE = {
    '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33,
    '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
    '8': 0x38, '9': 0x39, '+': 0x6B, '-': 0x6D,
    '*': 0x6A, '/': 0x6F, '=': 0x0D
}

def press_key(hexKeyCode):
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 0, 0)

def release_key(hexKeyCode):
    ctypes.windll.user32.keybd_event(hexKeyCode, 0, 2, 0)

def press_and_release(key):
    press_key(VK_CODE[key])
    time.sleep(0.05)
    release_key(VK_CODE[key])
    time.sleep(0.05)

op_map = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}

# Input the numbers and operation into Calculator
for digit in str(numbers[0]):
    press_and_release(digit)
press_and_release(op_map[operation])
for digit in str(numbers[1]):
    press_and_release(digit)
press_and_release('=')
