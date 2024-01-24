import pandas as pd

# Read data from different file formats
json_data = pd.read_json('data.json')
html_data = pd.read_html('data.html')[0]  # Assuming the first table in HTML is the desired one
xml_data = pd.read_xml('data.xml')
csv_data = pd.read_csv('data.csv')

# Check for missing data
print("Missing Data in JSON file:")
print(json_data.isnull().sum())

print("Missing Data in HTML file:")
print(html_data.isnull().sum())

print("Missing Data in XML file:")
print(xml_data.isnull().sum())

print("Missing Data in CSV file:")
print(csv_data.isnull().sum())

# Handle missing data
json_data_filled = json_data.fillna(0)
html_data_filled = html_data.fillna(method='ffill')

# Check if numeric columns exist in the XML data before filling missing values
numeric_columns = ['NumericColumn1', 'NumericColumn2']
available_columns = xml_data.columns.tolist()

# Filter out only the numeric columns that exist in the XML data
numeric_columns_exist = [col for col in numeric_columns if col in available_columns]

if numeric_columns_exist:
    xml_data_filled = xml_data.fillna(xml_data[numeric_columns_exist].mean())
else:
    print("Numeric columns not found in XML data.")

csv_data_filled = csv_data.dropna()

# Check for outlier values
print("Outlier Values in JSON file:")
print(json_data.describe())

print("Outlier Values in HTML file:")
print(html_data.describe())

print("Outlier Values in XML file:")
print(xml_data.describe())

print("Outlier Values in CSV file:")
print(csv_data.describe())



















### Reading Data from Different File Formats:

#### 1. **JSON (JavaScript Object Notation):**
    # JSON files store data in a structured format, often used for exchanging data between a server and a web application.
    # We use `pd.read_json('filename.json')` to read data from a JSON file into a pandas DataFrame.

#### 2. **HTML (HyperText Markup Language):**
    # HTML files define the structure of a web page.
    # For tabular data in HTML, we use `pd.read_html('filename.html')` to extract tables and convert them into a DataFrame.

#### 3. **XML (eXtensible Markup Language):**
    # XML files store data in a structured way, commonly used for configuration and data interchange.
    # We use `pd.read_xml('filename.xml')` to read XML data into a DataFrame.

#### 4. **CSV (Comma-Separated Values):**
    # CSV files store data with each value separated by a comma.
    # Reading data from a CSV file is done with `pd.read_csv('filename.csv')`.

### Checking for Missing Data:

    # After reading the data into DataFrames, we use `isnull().sum()` to check how many missing values are there in each column.
    # Missing values might occur when data is not available or not recorded for certain entries.

### Handling Missing Data:

#### 5. **Filling Missing Data:**
    # For handling missing values, we use methods like `fillna()` to replace missing values with a specified value.
    # For instance, `fillna(0)` replaces missing values with zeros, and `fillna(method='ffill')` fills missing values with the previous non-null value.

#### 6. **Dropping Rows with Missing Data:**
    # Another strategy is to use `dropna()` to remove entire rows containing missing values.

### Identifying Outlier Values:

    # Outliers are data points that significantly differ from other data points in a dataset.
    # We use the `describe()` method to get summary statistics and identify potential outliers.

### Handling Outlier Values:

    # Handling outliers might involve applying statistical techniques, transformations, or, in some cases, removing them from the dataset.

### In a Nutshell:

    # We read data from different file formats, check for missing values, handle missing data using various strategies, identify outliers, and manage them to ensure our data is accurate and suitable for analysis. These steps help us understand and work with our data effectively.
