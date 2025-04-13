import requests
from io import StringIO
import pandas as pd

# Use the raw URL, not the GitHub webpage URL
url = "https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv"
headers = {"User-Agent": "Mozilla/5.0"}

# Make the request
req = requests.get(url, headers=headers)

# Convert to CSV using StringIO
data = StringIO(req.text)

# Load into pandas DataFrame
df = pd.read_csv(data)

# Show the first few rows
print(df.head())