# Importing pandas library and aliasing it as pd
import pandas as pd

# Creating a hierarchical data frame with year, quarter, sales, and expenses columns
data = pd.DataFrame({'Year': [2019, 2019, 2020, 2020],
                     'Quarter': [1, 2, 1, 2],
                     'Sales': [100, 200, 150, 250],
                     'Expenses': [50, 75, 60, 90]})

# Printing the original data frame
print("Original Data Frame:")
print(data)

# Performing reshaping of hierarchical data by setting 'Year' and 'Quarter' as the index
reshaped_data = data.set_index(['Year', 'Quarter'])
print("Reshaped Data:")
print(reshaped_data)

# Performing pivoting of the data frame, using 'Year' as the index, 'Quarter' as columns, and 'Sales' and 'Expenses' as values
pivoted_data = data.pivot(index='Year', columns='Quarter', values=['Sales', 'Expenses'])
print("Pivoted Data:")
print(pivoted_data)













### Reshaping Hierarchical Data:

#### 1. **Original Data Frame:**
    # You have a table with columns like 'Year', 'Quarter', 'Sales', and 'Expenses'.
    # Each row represents data for a specific quarter in a particular year.

#### 2. **Reshaping Data:**
    # By setting 'Year' and 'Quarter' as the index, you're rearranging the data.
    # Think of it like organizing the information based on the year and quarter, making it easier to focus on specific periods.

#### 3. **Reshaped Data:**
    # The result is a new view of your data, where each row is identified by both the year and quarter.
    # It's like having a more structured way to access and analyze your information.

### Pivoting Data Frame:

#### 4. **Original Data Frame (Again):**
    # You start with the same table structure, but this time you're thinking about how to present the information differently.

#### 5. **Pivoting Data:**
    # By pivoting, you're reorganizing your table to have 'Year' as the rows and 'Quarter' as the columns.
   # This makes it easy to see how sales and expenses change over different quarters within each year.

#### 6. **Pivoted Data:**
   # The result is a new table where years are listed vertically, quarters are listed horizontally, and values like sales and expenses fill in the intersections.
    # It's like turning your original table to get a different perspective, especially useful for summarizing and comparing data.

### In a Nutshell:
    # Reshaping is like organizing your data in a way that's easier to understand, using specific identifiers like year and quarter.
    # Pivoting is about changing the layout of your table to make it more insightful, especially when you want to see how values change across different categories.








#IN ANSWER:The first level of columns represents the variables: 'Sales' and 'Expenses'.
#The second level of columns represents the quarters: 1 and 2.
#The index represents the years: 2019 and 2020.
#For each year and quarter combination, the corresponding values of sales and expenses are filled in the pivoted data frame. Let's break down the values:
# For the year 2019:
# In Quarter 1, the sales value is 100, and the expenses value is 50.
# In Quarter 2, the sales value is 200, and the expenses value is 75.
# For the year 2020:
# In Quarter 1, the sales value is 150, and the expenses value is 60.
# In Quarter 2, the sales value is 250, and the expenses value is 90.





