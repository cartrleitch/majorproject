import sqlite3
import sys
import justpy as jp
import pandas as pd
from purchase_add import *
from reimbursement_add import *
from employee_add import *
from main_reimbursements import *


def main():
    wp = jp.WebPage(delete_flag=False)

    jp.justpy(reim_table)


if __name__ == '__main__':
    main()
