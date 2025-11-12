import os
import pandas as pd

# Load the sample data
data_file = 'sample_data.csv'
if not os.path.exists(data_file):
    message = (
        f"Error: '{data_file}' not found. "
        "Please ensure the file is created."
    )
    print(message)
    exit()

df = pd.read_csv(data_file)
print("Data loaded successfully.")

# Group by conversion status
# Calculate the mean of session_duration_minutes
average_duration = (
    df.groupby('is_conversion')['session_duration_minutes']
    .mean()
    .reset_index()
)

# Rename the 'is_conversion' column values for clarity
# duplicate replacement removed (mapping already applied above)
average_duration['is_conversion'] = average_duration['is_conversion'].replace(
    {
        0: 'No Conversion',
        1: 'Converted',
    }
)
