import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Establish connection to MySQL database
config = {
    "host":r"localhost",
    "user":r"sample_user",
    "password":r"sample_password",
    "database":r"data_holder"
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()


# Retrieve data from MySQL
cursor.execute("SELECT * FROM data_holder.compile")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=cursor.column_names)
# Close cursor and connection
cursor.close()
connection.close()

#Compile the data
all_wins = df["wins"].tolist()
opt_wins = all_wins.count('1.0')
print(opt_wins)
x_values = ['OPTIMAL', 'RANDOM']
y_values = [opt_wins, len(all_wins)-opt_wins]

# Plot the results
plt.bar(x_values, y_values, width=0.7)
plt.ylabel('Frequency')
plt.title('Optimal wins vs Random Wins')
plt.grid(True)
plt.show()