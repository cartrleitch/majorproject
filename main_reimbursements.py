import sqlite3
import sys
import justpy as jp


def main():
    wp = jp.WebPage(delete_flag=False)
    button_classes = "w-32 h-10 bg-green-500 m-2 hover:bg-green-700 text-white font-bold py-2" \
                     " px-4 rounded text-center"
    div_classes = "flex m-4 flex-wrap"
    p_classes = "m-2 p-2 h-10 text-xl"

    banner = jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full h-1000 bg-blue place-items-top '
                                                           'font-bold text-xs text-white align-left')

    # basic form (input and action)
    def input_form():
        form_div = jp.Div(a=wp, classes='grid h-screen place-items-center')
        form1 = jp.Form(a=form_div, classes='flex flex-col border m-5 p-4 w-100')
        input_div = jp.Div(a=form1, classes='py-1 pl-8')
        button_div = jp.Div(a=form1, classes='py-3')

        # form entry template
        minID_label = jp.Label(text='MinistryID',
                               classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 mt-2',
                               a=input_div)
        in1 = jp.Input(placeholder='MinistryID', a=input_div, classes='form-input', type='number')
        minID_label.for_component = in1
        # form entry template

        ministry_label = jp.Label(text='Ministry',
                                  classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 mt-2',
                                  a=input_div)
        in2 = jp.Input(placeholder='Ministry', a=input_div, classes='form-input', type='text')
        ministry_label.for_component = in2

        def contents_show(self, msg):
            conn = sqlite3.connect('db_reimbursements.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM Ministries')
            results = cur.fetchall()
            for row in results:
                print(row)
            conn.commit()
            conn.close()

        submit_button = jp.Input(value='Submit Form', type='submit', a=button_div, classes=button_classes)
        show_button = jp.Button(text='Show Values', type='button', a=button_div, classes=button_classes,
                                click=contents_show)

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

    # creates webpage
    def run():
        return wp

    jp.justpy(run)


if __name__ == '__main__':
    main()
