# RamInfoFastAPI
This is a web app to see usage of RAM during last n minutes.
Only send a request to /ram/{number} which number is last n minutes.

# How to install
pip install -r requirements.txt

# How to run
uvicorn api:app --host 0.0.0.0 --port 8080

# Example
/ram/1

output:
[
    {
        "total":8462,
        "free":245,
        "used":6107
    }
]