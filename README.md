# Police_Data

## Summary
This dataset contains the Seattle Police Department's incident response data. This dataset was obtained from the **Seattle Police Department website** found [here](https://data.seattle.gov/Public-Safety/Seattle-Police-Department-911-Incident-Response/3k2p-39jp).

## Getting Started
### Dependencies
- Windows 10
- Python 3

### Clean Dataset
- Remove potential errors
- Remove potential outliers
- Remove duplicate records
- Remove unnecessary data
- Provide a clean copy of the data

### Libraries
- pandas
- numpy
- matplotlib
- seaborn
- calendar


## Steps
1. Import Data
2. Clean Data
3. Write DataFrame to a .csv


## Explanation of Column Deletions 
- **Over half of data missing for "At Scene Time" column.**
This figure is too high to fill in, so removing the column is a better idea.
- **Remove "CAD CDW ID", "CAD Event Number", "General Offense Number", and "Event Clearance Code" columns.**
These columns are not necessary for the analysis.
