import sqlite3
import sys
import justpy as jp
from cosmetic_classes import *


@jp.SetRoute('/addpurchase')
def add_purchase_main():
    # webpage creation
    wp = jp.WebPage(delete_flag=False)
    wp.title = 'Add Purchase'

    banner_div = jp.Div(text='Five Oaks Church', a=wp, classes=banner_classes,
                        style=banner_style,
                        click=banner_click)
    banner_sub = jp.Div(text='Reimbursement Manager', a=banner_div, classes=banner_sub_classes,
                        style='font-size:15px; padding-top: 10px;')
    title_div = jp.Div(text='Purchase Add and Edit', a=wp,
                       classes=title_classes)
    description_div = jp.Div(text='Create or Edit Purchase Data', a=title_div,
                             classes=desc_classes)

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
    save_button = jp.Input(value='Save', type='submit', a=button_div2, classes=button_classes,
                           style='cursor: pointer')

    # done button
    done_button = jp.Button(text='Done', type='button', a=button_div2, classes=button_classes,
                            click=done_red)

    form1.on('submit', submit_form)
    # creates webpage
    return wp


def done_red(self, msg):
    msg.page.redirect = 'http://127.0.0.1:8000/purchasetable'


# inserts values from entries into table
def submit_form(self, msg):
    data = msg.form_data
    date = ''
    total_cost = ''
    p_type = ''
    contents = ''
    print(data)
    for output in data:
        if output['placeholder'] == 'Date':
            date = output.value

        if output['placeholder'] == 'Total Cost':
            total_cost = float(output.value)

        if output['html_tag'] == 'select':
            p_type = output.value

        if output['placeholder'] == 'Contents':
            contents = output.value

    conn = sqlite3.connect('db_reimbursements.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Purchase(PurchaseDate, Amount, Content, PurchaseType, ReimID) '
                'VALUES (?, ?, ?, ?, 1)', (date, total_cost, p_type, contents))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    add_purchase_main()