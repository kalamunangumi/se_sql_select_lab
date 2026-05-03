# STEP 1A
# Import SQL Library and Pandas
import pandas as pd
import sqlite3

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# result = pd.read_sql("""SELECT * FROM employees""", conn)

# print("---------------------Employee Data---------------------")
# print(result)

# # STEP 2
# # Replace None with your code
# df_first_five = pd.read_sql("""SELECT * FROM employees LIMIT 5""", conn)
# print("---------------------First Five Employees---------------------")
# print(df_first_five)

# # STEP 3
# # Replace None with your code
# df_five_reverse = pd.read_sql("""SELECT * FROM employees ORDER BY employeeNumber DESC LIMIT 5""", conn)
# print("---------------------Last Five Employees---------------------")
# print(df_five_reverse)

# # STEP 4
# # Replace None with your code
# df_alias = pd.read_sql("""SELECT employeeNumber as ID FROM employees""", conn)
# print("---------------------Employee IDs---------------------")
# print(df_alias)

# STEP 5
# Replace None with your code
# df_executive = pd.read_sql(""" SELECT *, CASE WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive' ELSE 'Non-Executive' END AS Job_Type FROM employees""", conn)
# print("---------------------Employee Job Type---------------------")
# print(df_executive)

# STEP 6
# Replace None with your code
# df_name_length = pd.read_sql("""SELECT *, LENGTH(lastName) as name_length FROM employees""", conn)
# print("---------------------Employee Name Length---------------------")
# print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle,1, 2) AS short_title FROM employees""", conn)
print("---------------------Employee Short Titles---------------------")
print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""SELECT SUM(priceEach * quantityOrdered) AS total_price FROM orderdetails""", conn)
print("---------------------Total Price of All Orders---------------------")
print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""SELECT orderNumber, orderDate, STRFTIME('%d', orderDate) AS day, STRFTIME('%m', orderDate) AS month, STRFTIME('%Y', orderDate) AS year FROM orders""", conn)


conn.close()