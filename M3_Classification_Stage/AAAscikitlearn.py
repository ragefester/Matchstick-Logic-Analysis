import pandas as pd
import mysql.connector
# Credentials
config = {
        "host":r"localhost",
        "user":r"root",
        "password":r"sample_password",
        "database":r"sample_database"
}
# Create a connection
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
# Command
sql1 = "SELECT * FROM compile"
# Execute command
cursor.execute(sql1)
# Reconstruct the pandas dataframe we entered
rows = cursor.fetchall()
dataset = pd.DataFrame(rows, columns=cursor.column_names)

# Create dataset to work with
# It should prt easily as I've made the dataframe before saving it to csv
#dataset = pd.read_csv(r"Potential\Matchsticks_Problem\zzzFinal product\data.csv")
# Our tests are everything that is not wins
# Import libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# Used for graphing a tree
feature_names = dataset.columns.tolist()
feature_names = feature_names[1:]
# X = All columns EXCEPT wins
X = dataset.drop(columns=["wins"])
y = dataset["wins"]
# split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #random_state=42

clf = RandomForestClassifier()
# Fit the train values to the Ai function
clf.fit(X_train, y_train)
# These are our results from the prediction
y_result = clf.predict(X_test)
# shows the prediction and sample number
for i, prediction in enumerate(y_result):
    print(f"Sample {i+1}: Predicted class {prediction}")
# Compares the prediction to actual answer
accuracy = accuracy_score(y_test, y_result)
print("Accuracy:", accuracy)


from sklearn.tree import export_graphviz
import pydot
# Pulling one tree from the forest
tree = clf.estimators_[5]
export_graphviz(tree, out_file='tree1.dot', feature_names = feature_names, rounded = True, precision=1)
(graph,) = pydot.graph_from_dot_file('tree1.dot')
graph.write_png('tree1.png')
