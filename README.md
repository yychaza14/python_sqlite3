# python_sqlite3


name: Timestamp Tracker

on:
  # Run every 12 hours
  schedule:
    - cron: '0 */12 * * *'
  
  # Allow manual triggering
  workflow_dispatch:

jobs:
  track-timestamp:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
    
    - name: Run timestamp tracking script
      run: |
        python -m pip install --upgrade pip
        python timestamp_tracker.py
    
    - name: Commit and push changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add data/timestamps.db
        git commit -m "Update timestamps database" || exit 0
        git push