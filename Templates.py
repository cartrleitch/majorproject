import sqlite3
import sys
import justpy as jp


def main():
    wp = jp.WebPage()
    button_classes = "w-32 h-10 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2" \
                     " px-4 rounded text-center align-baseline"

    button_div = jp.Div(text='Button label: ', a=wp)
    jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full place-items-center '
                                                  'font-bold text-xs text-white align-left content-center',
           style='background:#497529; height:75px; font-size:30px; padding: 10px')

    # basic button
    def click_1(self, msg):
        self.num_clicked += 1
        if self.num_clicked % 2 == 0:
            self.text = 'I was clicked'
        else:
            self.text = 'Change'

    b = jp.Button(text='Button title', a=button_div, classes=button_classes, click=click_1)
    b.num_clicked = 0

    # basic button

    wp = jp.WebPage(delete_flag=False)
    button_classes = "block w-32 h-10 bg-green-700 hover:bg-green-800 text-white font-bold py-2" \
                     "px-4 rounded m-5"

    banner_div = jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full place-items-center '
                                                               'font-bold text-xs text-white '
                                                               'align-left overflow-hidden',
                        style='background:#047857; height:75px; font-size:30px; padding: 10px; border-style: solid;'
                              'border-bottom-color: #065f46; border-bottom-width: 10px')
    title_div = jp.Div(text='Ministry Add and Edit', a=wp,
                       classes='text-center font-bold border m-5 mx-60 p-4 w-25 overflow-hidden')
    description_div = jp.Div(text='Create or Edit Ministry Data', a=title_div,
                             classes='text-center text-xs overflow-hidden')

    # basic form (input and action)
    def input_form():
        # div definitions
        form_div = jp.Div(a=wp, classes='grid h-50')
        form1 = jp.Form(a=form_div, classes='border m-5 p-4 w-100')
        input_div = jp.Div(a=form1, classes='flex flex-col items-center py-1')
        button_div = jp.Div(a=form1, classes='flex flex-col items-center py-3')
        button_div2 = jp.Div(a=button_div, classes='flex flex-row items-center py-3')

        # form entry template
        minID_label = jp.Label(text='MinistryID',
                               classes='grid uppercase tracking-wide text-gray-700 text-xs font-bold',
                               a=input_div)
        in1 = jp.Input(placeholder='MinistryID', a=input_div, classes='form-input', type='number')
        minID_label.for_component = in1
        # form entry template

        ministry_label = jp.Label(text='Ministry',
                                  classes='grid uppercase tracking-wide text-gray-700 text-xs font-bold '
                                          'mb-2 mt-2',
                                  a=input_div)
        in2 = jp.Input(placeholder='Ministry', a=input_div, classes='form-input', type='text')
        ministry_label.for_component = in2

        # retrieve contents of database
        def contents_show(self, msg):
            conn = sqlite3.connect('db_reimbursements.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM Ministries')
            results = cur.fetchall()
            for row in results:
                print(row)
            conn.commit()
            conn.close()

        # buttons for submitting and retrieving data
        submit_button = jp.Input(value='Submit Form', type='submit', a=button_div2, classes=button_classes,
                                 style='cursor: pointer')
        show_button = jp.Button(text='Show Values', type='button', a=button_div2, classes=button_classes,
                                click=contents_show)

        # function for inserting and committing data
        def submit_form(self, msg):
            min_id = 0
            desc = ''

            data = msg.form_data
            for output in data:
                if output.placeholder == 'MinistryID':
                    min_id = output.value

                if output.placeholder == 'Ministry':
                    desc = output.value

            conn = sqlite3.connect('db_reimbursements.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO Ministries VALUES (?, ?)', (min_id, desc))
            conn.commit()
            conn.close()

        form1.on('submit', submit_form)

    input_form()

    # basic form (input and action)

    # dropdown menu

    import sqlite3
    import sys
    import justpy as jp
    import cosmetic_classes as re

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
        banner_div = jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full place-items-center '
                                                                   'font-bold text-xs text-white '
                                                                   'align-left overflow-hidden',
                            style='background:#047857; height:75px; font-size:30px; padding: 10px; border-style: solid;'
                                  'border-bottom-color: #065f46; border-bottom-width: 10px')
        title_div = jp.Div(text='Reimbursement Add and Edit', a=wp,
                           classes='text-center font-bold border m-5 mx-60 p-4 w-25 overflow-hidden')
        description_div = jp.Div(text='Create or Edit Reimbursement Data', a=title_div,
                                 classes='text-center text-xs overflow-hidden')

        def reim_form():
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
                cur.execute('INSERT INTO Reimbursements(ReimID, EmpID, DateRec, Total) '
                            'VALUES (1, 1, ?, ?)', (date, total))
                conn.commit()
                conn.close()

            form1.on('submit', submit_form)

        reim_form()
        return wp

    @jp.SetRoute('/addpurchase')
    def add_purchase_main():
        # webpage creation
        wp = jp.WebPage(delete_flag=False)
        wp.title = 'Add Purchase'

        # classes for design elements
        button_classes = "block w-32 h-10 bg-green-700 hover:bg-green-800 text-white font-bold py-2" \
                         "px-4 rounded m-5"
        label_classes = "grid uppercase tracking-wide text-gray-700 text-xs font-bold" \
                        "mb-2 mt-2"
        input_classes = 'form-input'

        # banner at top of page
        banner_div = jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full place-items-center '
                                                                   'font-bold text-xs text-white '
                                                                   'align-left overflow-hidden',
                            style='background:#047857; height:75px; font-size:30px; padding: 10px; border-style: solid;'
                                  'border-bottom-color: #065f46; border-bottom-width: 10px')
        title_div = jp.Div(text='Purchase Add and Edit', a=wp,
                           classes='text-center font-bold border m-5 mx-60 p-4 w-25 overflow-hidden')
        description_div = jp.Div(text='Create or Edit Purchase Data', a=title_div,
                                 classes='text-center text-xs overflow-hidden')

        def purchase_form():
            # page divs
            form_div = jp.Div(a=wp, classes='grid h-50')
            form1 = jp.Form(a=form_div, classes='border m-5 p-5 w-100')
            input_div = jp.Div(a=form1, classes='flex flex-col items-center py-1')
            button_div = jp.Div(a=form1, classes='flex flex-col items-center py-3')
            button_div2 = jp.Div(a=button_div, classes='flex flex-row items-center py-3')

            # date entry
            date_label = jp.Label(a=input_div, text='Date', classes=label_classes)
            date_in = jp.Input(a=input_div, placeholder='Date', classes=input_classes, type='date')
            date_label.for_component = date_in
            # total cost entry
            cost_label = jp.Label(a=input_div, text='Total Cost', classes=label_classes)
            cost_in = jp.Input(a=input_div, placeholder='Total Cost', classes=input_classes, type='text')
            cost_label.for_component = cost_in

            # purchase type dropdown menu input
            purchaseType_label = jp.Label(a=input_div, text='Purchase Type', classes=label_classes)
            purchase_types = ['once', 'many']
            select = jp.Select(a=input_div, value='once')
            for pur_type in purchase_types:
                select.add(jp.Option(value=pur_type, text=pur_type))
            purchaseType_label.for_component = select

            # contents entry
            contents_label = jp.Label(a=input_div, text='Contents', classes=label_classes)
            contents_in = jp.Textarea(a=input_div, placeholder='Contents', classes='form-input', type='text')
            contents_label.for_component = contents_in

            # button that calls submit_form when pressed
            submit_button = jp.Input(value='Save', type='submit', a=button_div2, classes=button_classes,
                                     style='cursor: pointer')

            # inserts values from entries into table
            def submit_form(self, msg):
                data = msg.form_data
                date = ''
                total_cost = ''
                p_type = ''
                contents = ''

                for output in data:
                    if output['id'] == '2':
                        date = output.value

                    if output['id'] == '3':
                        total_cost = float(output.value)

                    if output['id'] == '4':
                        p_type = output.value

                    if output['id'] == '5':
                        contents = output.value

                conn = sqlite3.connect('db_reimbursements.db')
                cur = conn.cursor()
                cur.execute('INSERT INTO Purchase(PurchaseDate, Amount, Content, PurchaseType, ReimID) '
                            'VALUES (?, ?, ?, ?, 1)', (date, total_cost, p_type, contents))
                conn.commit()
                conn.close()

            form1.on('submit', submit_form)

        purchase_form()
        return wp

    if __name__ == '__main__':
        jp.justpy(add_reim_main)

    # creates webpage
    def run():
        return wp

    jp.justpy(run)


if __name__ == '__main__':
    main()
