import sqlite3
import sys
import justpy as jp


def main():
    #conn = sqlite3.connect('db_reimbursements.db') each database interaction
    #cur = conn.cursor()
    #conn.commit()
    #conn.close()

    wp = jp.WebPage(data={'text': 'Initial'})
    button_classes = "w-32 h-10 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2" \
                     " px-4 rounded text-center align-baseline"
    div_classes = "flex m-4 flex-wrap"
    input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 " \
                    "focus:outline-none focus:bg-white focus:border-purple-500"
    p_classes = "m-2 p-2 h-10 text-xl"
    button_div = jp.Div(text='Button label: ', a=wp, classes=div_classes)

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

    # insert entries
    def inp1_ret(self, msg):
        self.val = self.value
        print(self.val)

    async def in1():
        inp_1 = jp.Input(type='number', a=wp, classes=input_classes, placeholder='Type here', model=[wp, 'text'])
        inp_1.div = jp.Div(model=['text'], text='MinistryID', classes=p_classes, a=wp)
        inp_1.on('input', inp1_ret)
        return wp

    in1()
    # insert entries

    # insert button
    def click_insert(self, msg):
        print(self.val)

    conn = sqlite3.connect('db_reimbursements.db')
    cur = conn.cursor()
    b = jp.Button(model=[wp, 'text'], text='Save', a=button_div, classes=button_classes, click=click_insert)
    b.val = inp1_ret
    conn.commit()
    conn.close()
    # insert button


# creates webpage
    def run():
        return wp

    jp.justpy(run)


if __name__ == '__main__':
    main()
