import sqlite3
import sys
import justpy as jp
import pandas as pd
from purchase_add import *
from reimbursement_add import *
from employee_add import *
from main_reimbursements import *
from purchase_table import *
from employee_table import *
import webbrowser


def main():
    # create webpage (first page is reimbursement table)
    webbrowser.open('http://127.0.0.1:8000')
    jp.justpy(reim_table)


if __name__ == '__main__':
    main()
