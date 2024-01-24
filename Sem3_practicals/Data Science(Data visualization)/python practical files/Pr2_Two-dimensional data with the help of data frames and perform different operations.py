# Importing pandas library and aliasing it as pd
import pandas as pd

# Creating a two-dimensional data frame using a dictionary
data = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                     'B': [6, 7, 8, 9, 10],
                     'C': [11, 12, 13, 14, 15]})

# Printing the entire data frame
print("Data Frame:")
print(data)

# Accessing and printing individual columns
print("Column A:")
print(data['A'])
print("Column B:")
print(data['B'])
print("Column C:")
print(data['C'])

# Accessing and printing individual rows using the loc method
print("Row 0:")
print(data.loc[0])
print("Row 1:")
print(data.loc[1])
print("Row 2:")
print(data.loc[2])

# Calculating and printing the sum of each column
print("Sum of Column A:", data['A'].sum())
print("Sum of Column B:", data['B'].sum())
print("Sum of Column C:", data['C'].sum())

# Calculating and printing the mean of each row using the loc method
print("Mean of Row 0:", data.loc[0].mean())
print("Mean of Row 1:", data.loc[1].mean())
print("Mean of Row 2:", data.loc[2].mean())

# Transposing the data frame (switching rows and columns)
transposed_data = data.transpose()
print("Transposed Data Frame:")
print(transposed_data)























### Understanding Two-Dimensional Data with DataFrames:

#### 1. **What is Two-Dimensional Data?**
    # Two-dimensional data is like a table or grid, where information is organized in rows and columns.
    # Picture it as an Excel sheet, with rows representing different entries and columns holding specific details.

#### 2. **What is a DataFrame in Pandas?**
    # In Python, a DataFrame is a tool from the `pandas` library that helps us manage and work with two-dimensional data.
    # Think of it as a digital table where you can store and manipulate your data easily.

#### 3. **Creating a DataFrame:**
    # To create a DataFrame, you input your data, typically in the form of lists or dictionaries.
  
### Performing Different Operations on the DataFrame:

#### 4. **Accessing Data:**
    # You can fetch specific pieces of data by referring to the column names or row indices.

#### 5. **Adding a New Column:**
    # You can add new information by creating and inserting a new column.

#### 6. **Summarizing Data:**
    # You can quickly get an overview of your data, like finding the average age.

#### 7. **Filtering Data:**
    # You can focus on specific parts of your data by setting conditions.

#### 8. **Sorting Data:**
    # You can arrange your data in a specific order, such as sorting by age.

### In a Nutshell:
    # Two-dimensional data is like an organized table, and pandas DataFrames make handling this type of data in Python super convenient.
    # With DataFrames, you can easily access, add, summarize, filter, and sort your data—making it a handy tool for data exploration and analysis.
