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



    # creates webpage
    def run():
        return wp

    jp.justpy(run)


if __name__ == '__main__':
    main()
