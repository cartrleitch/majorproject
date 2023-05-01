import sqlite3
import sys
import justpy as jp
import pandas as pd

conn = sqlite3.connect('db_reimbursements.db')

reim_table_data = pd.read_sql_query("SELECT Employee.FirstName AS 'First Name', Employee.LastName AS 'Last Name', "
                                    "Reimbursements.DatePaid, "
                                    "Reimbursements.DateRec AS 'Date Received', Reimbursements.Total FROM Employee "
                                    "INNER JOIN Reimbursements ON "
                                    "Employee.EmpID = Reimbursements.EmpID;", conn)


def selected_row(self, msg):
    if msg.selected:
        self.row_data.text = msg.data
        self.row_selected = msg.rowIndex
    elif self.row_selected == msg.rowIndex:
        self.row_data.text = ''


@jp.SetRoute("/reimbursementtable")
def reim_table():
    wp = jp.WebPage()
    wp.title = 'Reimbursement Tables'

    # classes for design elements
    button_classes = "block w-32 h-10 bg-green-700 hover:bg-green-800 text-white font-bold py-2" \
                     "px-4 rounded m-5"
    label_classes = "grid uppercase tracking-wide text-gray-700 text-xs font-bold" \
                    "mb-2 mt-2"
    input_classes = 'form-input'

    # banner at top of page
    def banner_click(self, msg):
        msg.page.redirect = 'http://127.0.0.1:8000/reimbursementtable'

    banner_div = jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full place-items-center '
                                                               'font-bold text-xs text-white '
                                                               'align-left overflow-hidden',
                        style='background:#047857; height:75px; font-size:30px; padding: 10px; border-style: solid;'
                              'border-bottom-color: #065f46; border-bottom-width: 10px; cursor: pointer;',
                        click=banner_click)

    table_div = jp.Div(a=wp, classes='flex flex-col items-center')
    button_div = jp.Div(a=wp, classes='flex flex-col items-center py-3')
    button_div2 = jp.Div(a=button_div, classes='flex flex-row items-center py-3')

    data_div = jp.Div(a=table_div)
    grid = reim_table_data.jp.ag_grid(a=table_div,
                                      style="height: 50vh; width: 75%; margin: 0.25rem; padding: 0.25rem;")
    grid.row_data = data_div
    grid.on('rowSelected', selected_row)
    grid.options.columnDefs[0].checkboxSelection = True

    def add_reim_red(self, msg):
        msg.page.redirect = 'http://127.0.0.1:8000/addreimbursement'

    add_reimbursement_button = jp.Button(text='Add', type='button', a=button_div, classes=button_classes,
                                         click=add_reim_red)

    return wp
