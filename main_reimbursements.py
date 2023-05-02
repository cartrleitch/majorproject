import sqlite3
import sys
import justpy as jp
import pandas as pd
from cosmetic_classes import *
global reim_sel_data
reim_sel_data = ''

conn = sqlite3.connect('db_reimbursements.db')

# gets data from query to show employee and reimbursement information
reim_table_data = pd.read_sql_query("SELECT Reimbursements.ReimID, Employee.FirstName AS 'First Name', "
                                    "Employee.LastName AS 'Last Name', "
                                    "Reimbursements.DatePaid, "
                                    "Reimbursements.DateRec AS 'Date Received', Reimbursements.Total FROM Employee "
                                    "INNER JOIN Reimbursements ON "
                                    "Employee.EmpID = Reimbursements.EmpID;", conn)
conn.close()


# takes data from selected row
def selected_row(self, msg):
    if msg.selected:
        self.row_data.text = msg.data
        global reim_sel_data
        reim_sel_data = self.row_data.text
        self.row_selected = msg.rowIndex
    elif self.row_selected == msg.rowIndex:
        self.row_data.text = ''


@jp.SetRoute("/reimbursementtable")
def reim_table():
    # creates webpage and titles it
    wp = jp.WebPage()
    wp.title = 'Reimbursement Table'

    banner_div = jp.Div(text='Five Oaks Church', a=wp, classes=banner_classes,
                        style=banner_style,
                        click=banner_click)
    banner_sub = jp.Div(text='Reimbursement Manager', a=banner_div, classes=banner_sub_classes,
                        style='font-size:15px; padding-top: 10px;')

    # divs
    table_div = jp.Div(a=wp, classes='flex flex-col items-center pt-5')
    button_div = jp.Div(a=wp, classes='flex flex-col items-center py-3')
    button_div2 = jp.Div(a=button_div, classes='flex flex-row items-center overflow-hidden')
    button_div3 = jp.Div(a=button_div, classes='flex flex-row items-center overflow-hidden')
    data_div = jp.Div(a=table_div, style='display:none;')

    # table label
    table_label = jp.Div(a=table_div, text='Reimbursement Table', classes=table_title_classes)
    table_label.for_component = table_div

    # creates table
    grid = reim_table_data.jp.ag_grid(a=table_div,
                                      style="height: 50vh; width: 50vw; margin: 0.25rem; padding: 0.25rem;")
    grid.row_data = data_div
    grid.on('rowSelected', selected_row)
    grid.options.columnDefs[0].hide = True
    grid.options.columnDefs[1].checkboxSelection = True

    # button that opens add reimbursement page
    add_reimbursement_button = jp.Button(text='Add', type='button', a=button_div2, classes=button_classes,
                                         click=add_reim_red)

    # button that opens purchase table
    view_contents_button = jp.Button(text='View Contents', type='button', a=button_div2, classes=button_classes,
                                     click=view_contents)

    # button that opens employees table
    employees_button = jp.Button(text='Employees', type='button', a=button_div2, classes=button_classes,
                                 click=employees)

    # button
    def refresh_table(self, msg):
        conn = sqlite3.connect('db_reimbursements.db')

        # gets data from query to show employee and reimbursement information
        refreshed_table_data = pd.read_sql_query("SELECT Reimbursements.ReimID, Employee.FirstName AS 'First Name', "
                                                 "Employee.LastName AS 'Last Name', "
                                                 "Reimbursements.DatePaid, "
                                                 "Reimbursements.DateRec AS 'Date Received', Reimbursements.Total FROM "
                                                 "Employee "
                                                 "INNER JOIN Reimbursements ON "
                                                 "Employee.EmpID = Reimbursements.EmpID;", conn)
        grid.load_pandas_frame(refreshed_table_data)
        grid.on('rowSelected', selected_row)
        grid.row_data = data_div
        grid.options.columnDefs[0].hide = True
        grid.options.columnDefs[1].checkboxSelection = True

        conn.close()

    refresh_table('', '')

    refresh_table_button = jp.Button(text='Refresh', type='button', a=button_div3, classes=button_classes,
                                     click=refresh_table)

    delete_selected_button = jp.Button(text='Delete', type='button', a=button_div3, classes=button_classes,
                                     click=delete_selected)

    return wp


def add_reim_red(self, msg):
    msg.page.redirect = 'http://127.0.0.1:8000/addreimbursement'


def view_contents(self, msg):
    msg.page.redirect = 'http://127.0.0.1:8000/purchasetable'


def employees(self, msg):
    msg.page.redirect = 'http://127.0.0.1:8000/employeetable'


def delete_selected(self, msg):
    conn = sqlite3.connect('db_reimbursements.db')
    cur = conn.cursor()
    reim_del = reim_sel_data['ReimID']
    cur.execute(f"DELETE FROM Reimbursements WHERE ReimID = {reim_del}")
    cur.execute(f"DELETE FROM Purchase WHERE ReimID = {reim_del}")
    conn.commit()
    conn.close()
