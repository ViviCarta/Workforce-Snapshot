# Workforce Snapshot API Integration Demo

A lightweight demonstration project showcasing how HR Systems (such as Workday RAAS and REST integrations) extract, transform, and prepare workforce-related data from API endpoints. This project highlights essential integration concepts such as REST requests, JSON parsing, data validation, transformation, and CSV export.

## 📁 Folder Structure
```
workforce-snapshot/
│
├── README.md
├── src/
│   ├── snapshot_api.py
│   ├── snapshot_api_csv.py
│
└── output/
    ├── workforce_snapshot.csv
    ├── example_report.txt
```

## ▶️ How to Run
Install dependencies:
```
pip install requests
```

Run snapshot script:
```
python src/snapshot_api.py
```

Run CSV export version:
```
python src/snapshot_api_csv.py
```
