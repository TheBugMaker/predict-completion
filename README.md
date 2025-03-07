# taxfix

## requirements
- docker

## Trigger Train/Evaluation Pipeline
```bash
docker compose up ml_pipeline
```
This will generate model.pickle file in models folder and reporting metrics in reports folder.
Pipeline and results can be viewed using kedro viz

## Visualize Pipeline
```bash 
docker compose up visulize_pipeline
```
This will start kedro viz server and you can view the pipeline at http://localhost:4141

## Start api
```bash
docker compose up api
```
This will start the api server at http://localhost:8000
Navigate to http://localhost:8000/docs to view the api documentation
example request:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/predict/' \
-H 'Content-Type: application/json' \
-d '[
    {
        "age": 30,
        "income": 75000.5,
        "employment_type": "Full-Time",
        "marital_status": "Single",
        "time_spent_on_platform": 3.5,
        "number_of_sessions": 10,
        "fields_filled_percentage": 85.0,
        "previous_year_filing": 1,
        "device_type": "Mobile",
        "referral_source": "Social Media"
    },
    {
        "age": 45,
        "income": 120000.0,
        "employment_type": "Self-Employed",
        "marital_status": "Married",
        "time_spent_on_platform": 1.2,
        "number_of_sessions": 5,
        "fields_filled_percentage": 95.0,
        "previous_year_filing": 0,
        "device_type": "Desktop",
        "referral_source": "Search Engine"
    }
]'
```
