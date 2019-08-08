# Police Data - README

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
- **Remove "Longitude", "Latitude", "Incident Location", and 'Hundred Block Location' columns**
"District/Sector", "Zone/Beat", and "Census Tract" all describe the location in a way that is useful in summarizing data. I chose to remove the columns listed as it contained sensitive information about the public.
- **Remove "Event Clearance SubGroup"**
"Event Clearance" and "Event Clearance Description Group" columns already outline a clear idea of the event. The SubGroup column does not add a lot of extra information.
- **Remove "Initial Type Subgroup"** - "Event Initial Type Description" and "Initial_Type_Group" provide enough information of the event.
- **Remove row 224 due to missing "District_Sector" entry** - There are no other entries with the same "Zone/Beat" entry as this row so I removed the row altogether.

## References
- **Cao, W., Colht, K., & Singh, G. (2015).** Visualizing Seattle Police Department Incident Response Data. University of Washington. Retrieved from https://visualizationdesign.files.wordpress.com/2015/06/caocolhtsingh_fr2.pdf
