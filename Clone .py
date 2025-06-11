import webbrowser
import time

# CONFIGURE THESE
url = "https://example.com"  # Replace with your target link
rest_time = 10               # Time to wait between opens (in seconds)
num_clicks = 5               # How many times to open the link

for i in range(num_clicks):
    print(f"Opening {url} ({i+1}/{num_clicks})")
    webbrowser.open(url)
    if i < num_clicks - 1:
        print(f"Waiting {rest_time} seconds before next open...")
        time.sleep(rest_time)

print("Done!")
