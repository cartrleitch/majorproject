import sqlite3

conn = sqlite3.connect('db_reimbursements.db')
cur = conn.cursor()
cur.execute(f"SELECT Reimbursements.ReimID, Employee.FirstName AS 'First Name', "
            f"Employee.LastName AS 'Last Name', "
            f"Reimbursements.DateRec AS 'Date Received' "
            f"FROM Employee "
            f"INNER JOIN Reimbursements ON "
            f"Employee.EmpID = Reimbursements.EmpID WHERE Employee.EmpID = 32;")
selected_reim = cur.fetchone()
conn.close()

print(selected_reim)