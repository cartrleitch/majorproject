import justpy as jp

input_classes = 'w-32 text-xl m-4 p-2 bg-white  border rounded'
label_classes = "grid uppercase tracking-wide text-gray-700 text-xs font-bold" \
                "mb-2 mt-2"
button_classes = "block w-32 h-10 bg-green-700 hover:bg-green-800 text-white font-bold py-2" \
                 "px-4 rounded m-5"
wp = jp.WebPage()
form_div = jp.Div(a=wp, classes='grid h-50')
form1 = jp.Form(a=form_div)


def comp_test():

    purchaseType_label = jp.Label(a=form1, text='Purchase Type', classes=label_classes)
    purchase_types = ['once', 'many']
    select = jp.Select(a=form1, classes=input_classes, value='once')
    for pur_type in purchase_types:
        select.add(jp.Option(value=pur_type, text=pur_type))
    purchaseType_label.for_component = select

    submit_button = jp.Input(value='Submit Form', type='submit', a=form1, classes=button_classes,
                             style='cursor: pointer')

    return wp


def submit_form(self, msg):
    data = msg.form_data
    print(data)


form1.on('submit', submit_form)

jp.justpy(comp_test)
