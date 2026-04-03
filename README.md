# Pakistan Solar Panel Requirement System

A Streamlit prototype for estimating solar system size, inverter size, battery backup, cost, savings, and payback for Pakistan local users.

## Features
- Customer profile and utility selection
- Appliance-based sizing
- Solar and backup load selection
- Roof capacity check
- Pricing and itemized cost estimation
- Results dashboard with charts
- PDF proposal export

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud deployment
1. Push this folder to a GitHub repository.
2. Open Streamlit Community Cloud.
3. Connect GitHub and select the repo.
4. Set `app.py` as the main file.
5. Deploy.

## Recommended repo structure
Keep all files exactly as they are in this project.

## Notes
- Tariffs and prices are editable in the app.
- This is an MVP estimator, not an engineering design tool.
