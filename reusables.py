import sqlite3
import sys
import justpy as jp

wp = jp.WebPage(delete_flag=False)
button_classes = "block w-32 h-10 bg-green-700 hover:bg-green-800 text-white font-bold py-2" \
                 "px-4 rounded m-5"

banner_div = jp.Div(text='Five Oaks Church', a=wp, classes='block uppercase w-full place-items-center '
                                                           'font-bold text-xs text-white '
                                                           'align-left overflow-hidden',
                    style='background:#047857; height:75px; font-size:30px; padding: 10px; border-style: solid;'
                          'border-bottom-color: #065f46; border-bottom-width: 10px')
