# Importing the numpy library and aliasing it as np
import numpy as np

# Creating a one-dimensional data series using numpy array
data = np.array([1, 2, 3, 4, 5, 6])

# Printing the created data series
print("Data Series:", data)

# Performing mathematical operations on the data series
print("Sum:", np.sum(data))
print("Product:", np.prod(data))
print("Square root:", np.sqrt(data))
print("Exponential:", np.exp(data))
print("Logarithm:", np.log(data))

# Performing statistical operations on the data series
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# Performing array manipulation operations on the data series
print("Sorted Data:", np.sort(data))
print("Reversed Data:", np.flip(data))
print("Unique Values:", np.unique(data))
print("Reshaped Data (2x3):", np.reshape(data, (2, 3)))
print("Data Series with Element-wise Addition:", data + 2)
print("Data Series with Element-wise Multiplication:", data * 3)















### Background Information on One-Dimensional Data using Series:

#### 1. **What is One-Dimensional Data?**
   # One-dimensional data is a list of values where each value has a specific position or index.
    # Think of it like a single line of data, where each item has a place in the order.

#### 2. **What is a Series in Pandas?**
    # In Python, the `pandas` library provides a data structure called a Series.
    # A Series is like a labeled array or a simple table with one column.
    # It has both data values and labels (or indices).

#### 3. **Creating a Series:**
    # You can create a Series by giving it a list of values.
    # Each value in the list becomes a part of the Series.
    # An index is automatically assigned to each value.

#### 4. **Operations on a Series:**
   # Once you have a Series, you can do various things with it.

#### 5. **Accessing Elements:**
    # You can access individual elements in the Series using their index.

#### 6. **Summing the Elements:**
    # You can find the total sum of all values in the Series.

#### 7. **Finding Maximum and Minimum:**
    # You can find the largest (maximum) and smallest (minimum) values in the Series.

#### 8. **Performing Mathematical Operations:**
    # You can apply mathematical operations to all elements in the Series.

### Conclusion:
    # In simple terms, a one-dimensional Series is like a line of data with values and their labels. # You can easily create it using pandas and perform operations to analyze and manipulate the data. # It's a handy tool for working with lists of information in Python.

