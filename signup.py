import pyodbc
import json

def sign_up_user(username, email, password):
    # Get the Azure SQL Database connection string
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=styleup.database.windows.net;DATABASE=Signup;UID=styleupadmin;PWD=Lawofpatk@911;Encrypt=True;TrustServerCertificate=True'

    # Connect to Azure SQL Database
    connection = pyodbc.connect(connection_string)

    # Create a new user account
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (Username, Email, Password) VALUES (?, ?, ?)', (username, email, password))

    # Commit the changes
    connection.commit()

    # Close the connection
    connection.close()

if __name__ == '__main__':
    # Get the user's input from the form data
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Sign up the new user
    sign_up_user(username, email, password)

    # Redirect the user to a success page
    return redirect('/success')
