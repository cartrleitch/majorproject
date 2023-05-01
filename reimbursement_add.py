import sqlite3
import sys
import justpy as jp
import reusables as re


@jp.SetRoute('/addreimbursement')
def add_reim_main():
    # webpage creation
    wp = jp.WebPage(delete_flag=False)
    wp.title = 'Add Reimbursement'

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
    banner_sub = jp.Div(text='Reimbursement Manager', a=banner_div, classes='block uppercase w-full place-items-center '
                                                                            'italic text-xs text-white',
                                                                            style='font-size:15px; padding-top: 10px;')

    title_div = jp.Div(text='Reimbursement Add and Edit', a=wp,
                       classes='text-center font-bold border m-5 mx-60 p-4 w-25 overflow-hidden')
    description_div = jp.Div(text='Create or Edit Reimbursement Data', a=title_div,
                             classes='text-center text-xs overflow-hidden')

    # page divs
    form_div = jp.Div(a=wp, classes='grid h-50')
    form1 = jp.Form(a=form_div, classes='border m-5 p-5 w-100')
    input_div = jp.Div(a=form1, classes='flex flex-col items-center py-1')
    button_div = jp.Div(a=form1, classes='flex flex-col items-center py-3')
    button_div2 = jp.Div(a=button_div, classes='flex flex-row items-center py-3')

    # purchase type dropdown menu input
    employee_label = jp.Label(a=input_div, text='Employees', classes=label_classes)

    # get list a concatenation of first and last name from a select from Employee
    employees = ['John', 'Doe']
    select = jp.Select(a=input_div, value='John')
    for employee in employees:
        select.add(jp.Option(value=employee, text=employee))
    employee_label.for_component = select

    # date entry
    date_label = jp.Label(a=input_div, text='Reimbursement Date', classes=label_classes)
    date_in = jp.Input(a=input_div, placeholder='Date', classes=input_classes, type='date')
    date_label.for_component = date_in

    # button that calls submit_form when pressed
    submit_button = jp.Input(value='Save', type='submit', a=button_div2, classes=button_classes,
                             style='cursor: pointer')

    # add purchase function and button
    def add_purchase_red(self, msg):
        msg.page.redirect = 'http://127.0.0.1:8000/addpurchase'

    add_purchase_button = jp.Button(text='Add Purchase', type='button', a=button_div2, classes=button_classes,
                                    click=add_purchase_red)

    # inserts values from entries into table
    def submit_form(self, msg):
        data = msg.form_data
        emp = ''
        date = ''

        for output in data:
            if output['id'] == '2':
                # translate emp from input into corresponding employee ID
                emp = output.value

            if output['id'] == '3':
                date = output.value

        conn = sqlite3.connect('db_reimbursements.db')
        cur = conn.cursor()
        total = 122.0
        # calculate total
        cur.execute('INSERT INTO Reimbursements(EmpID, DateRec, Total) '
                    'VALUES (1, ?, ?)', (date, total))
        conn.commit()
        conn.close()

    form1.on('submit', submit_form)


    # creates webpage
    return wp


if __name__ == '__main__':
    add_reim_main()
