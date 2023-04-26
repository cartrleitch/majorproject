import sqlite3
import sys
import justpy as jp


def main():
    wp = jp.WebPage(delete_flag=False)

    # creates webpage
    def run():
        return wp

    jp.justpy(run)


if __name__ == '__main__':
    main()
