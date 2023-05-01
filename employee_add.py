import sqlite3
import sys
import justpy as jp
import reusables as re


def main():
    # webpage creation
    wp = jp.WebPage(delete_flag=False)
    wp.title = 'Add Employee'

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
    title_div = jp.Div(text='Employee Add and Edit', a=wp,
                       classes='text-center font-bold border m-5 mx-60 p-4 w-25 overflow-hidden')
    description_div = jp.Div(text='Create or Edit Employee Data', a=title_div,
                             classes='text-center text-xs overflow-hidden')

    # page divs
    form_div = jp.Div(a=wp, classes='grid h-50')
    form1 = jp.Form(a=form_div, classes='border m-5 p-5 w-100')
    input_div = jp.Div(a=form1, classes='flex flex-col items-center py-1')
    button_div = jp.Div(a=form1, classes='flex flex-col items-center py-3')
    button_div2 = jp.Div(a=button_div, classes='flex flex-row items-center py-3')

    # first name entry
    fname_label = jp.Label(a=input_div, text='First Name', classes=label_classes)
    fname_in = jp.Input(a=input_div, placeholder='First Name', classes=input_classes, type='text')
    fname_label.for_component = fname_in

    # last name entry
    lname_label = jp.Label(a=input_div, text='Last Name', classes=label_classes)
    lname_in = jp.Input(a=input_div, placeholder='Last Name', classes=input_classes, type='text')
    lname_label.for_component = lname_in

    # street entry
    street_label = jp.Label(a=input_div, text='Street', classes=label_classes)
    street_in = jp.Input(a=input_div, placeholder='Street', classes=input_classes, type='text')
    street_label.for_component = street_in

    # city entry
    city_label = jp.Label(a=input_div, text='City', classes=label_classes)
    city_in = jp.Input(a=input_div, placeholder='City', classes=input_classes, type='text')
    city_label.for_component = city_in

    # state entry
    state_label = jp.Label(a=input_div, text='State', classes=label_classes)
    state_in = jp.Input(a=input_div, placeholder='State', classes=input_classes, type='text')
    state_label.for_component = state_in

    # zip code entry
    zipcode_label = jp.Label(a=input_div, text='Zip Code', classes=label_classes)
    zipcode_in = jp.Input(a=input_div, placeholder='Zip Code', classes=input_classes, type='text')
    zipcode_label.for_component = zipcode_in

    # job title entry
    jobtitle_label = jp.Label(a=input_div, text='Job Title', classes=label_classes)
    jobtitle_in = jp.Input(a=input_div, placeholder='Job Title', classes=input_classes, type='text')
    jobtitle_label.for_component = jobtitle_in

    # employee account entry
    empaccount_label = jp.Label(a=input_div, text='Employee Account', classes=label_classes)
    empaccount_in = jp.Input(a=input_div, placeholder='Employee Account', classes=input_classes, type='text')
    empaccount_label.for_component = empaccount_in

    # ministry dropdown menu input
    ministry_label = jp.Label(a=input_div, text='Ministry', classes=label_classes)
    ministries = ['childrens', 'womens']
    select = jp.Select(a=input_div, value='childrens')
    for ministry in ministries:
        select.add(jp.Option(value=ministry, text=ministry))
    ministry_label.for_component = select


    # button that calls submit_form when pressed
    submit_button = jp.Input(value='Save', type='submit', a=button_div2, classes=button_classes,
                             style='cursor: pointer')

    # inserts values from entries into table
    def submit_form(self, msg):
        data = msg.form_data
        first_name = ''
        last_name = ''
        street = ''
        city = ''
        state = ''
        zip_code = ''
        job_title = ''
        emp_account = ''
        minis = ''

        for output in data:
            if output['id'] == '2':
                first_name = output.value

            if output['id'] == '3':
                last_name = float(output.value)

            if output['id'] == '4':
                street = output.value

            if output['id'] == '5':
                city = output.value

            if output['id'] == '6':
                state = output.value

            if output['id'] == '7':
                zip_code = output.value

            if output['id'] == '8':
                job_title = output.value

            if output['id'] == '9':
                emp_account = output.value

            if output['id'] == '10':
                minis = output.value

        conn = sqlite3.connect('db_reimbursements.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO Employee(FirstName, LastName, Street, City, State, ZipCode, '
                    'JobTitle, EmpAccount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (first_name, last_name, street, city,
                                                                                state, zip_code, job_title,
                                                                                emp_account))
        # needs corresponding IDs and date to input
        cur.execute("INSERT INTO EmpMinistry VALUES (1, 1, '12-12-2023', '12-12-2023')")
        conn.commit()
        conn.close()

    form1.on('submit', submit_form)


    # creates webpage
    return wp


if __name__ == '__main__':
    main()
