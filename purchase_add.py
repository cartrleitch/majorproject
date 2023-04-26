import sqlite3
import sys
import justpy as jp
import reusables as re


def main():
    # webpage creation
    wp = jp.WebPage(delete_flag=False)

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

        # date entry
        contents_label = jp.Label(a=input_div, text='Contents', classes=label_classes)
        contents_in = jp.Input(a=input_div, placeholder='Contents', classes=input_classes, type='text')
        contents_label.for_component = contents_in

        # button that calls submit_form when pressed
        submit_button = jp.Input(value='Submit Form', type='submit', a=button_div2, classes=button_classes,
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
                    print(output)

                if output['id'] == '3':
                    total_cost = float(output.value)
                    print(output)

                if output['id'] == '4':
                    p_type = output.value
                    print(output)

                if output['id'] == '5':
                    contents = output.value
                    print(output)

            conn = sqlite3.connect('db_reimbursements.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO Purchase VALUES (1, ?, ?, ?, ?, 1)', (date, total_cost, p_type, contents))
            conn.commit()
            conn.close()

        form1.on('submit', submit_form)

    purchase_form()

    # creates webpage
    def run():
        return wp

    jp.justpy(run)


if __name__ == '__main__':
    main()
