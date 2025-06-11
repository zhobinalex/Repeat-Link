You can use the script I provided in Termux! Here’s how you can do it step by step:

### 1. Install Python in Termux

Open Termux and run:
```bash
pkg update
pkg install python
```

### 2. Create the Script

You can use a text editor like `nano` or `vim` to create your Python script:
```bash
nano auto_clicker.py
```
Paste the following code into the file (edit the `url`, `rest_time`, and `num_clicks` values as you need):

```python
import webbrowser
import time

url = "https://example.com"  # Your target link
rest_time = 10               # Time between opens (in seconds)
num_clicks = 5               # Number of times to open the link

for i in range(num_clicks):
    print(f"Opening {url} ({i+1}/{num_clicks})")
    webbrowser.open(url)
    if i < num_clicks - 1:
        print(f"Waiting {rest_time} seconds before next open...")
        time.sleep(rest_time)

print("Done!")
```

Save and exit (`Ctrl+O` to save, `Ctrl+X` to exit in nano).

### 3. Run the Script

In Termux, run:
```bash
python auto_clicker.py
```

---

**Note:**  
- On some Termux installations, `webbrowser.open()` will open links using the default Android browser, but it may require you to have a browser installed and allow Termux to open it.
- If `webbrowser` does not work as expected, you can use the `am start` command via Python to open URLs in Android:

```python
import os
import time

url = "https://example.com"
rest_time = 10
num_clicks = 5

for i in range(num_clicks):
    print(f"Opening {url} ({i+1}/{num_clicks})")
    os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
    if i < num_clicks - 1:
        print(f"Waiting {rest_time} seconds before next open...")
        time.sleep(rest_time)

print("Done!")
```

This version uses Android's Activity Manager directly and should work more reliably in Termux.

Let me know if you want the script to accept command-line arguments or save your settings!
