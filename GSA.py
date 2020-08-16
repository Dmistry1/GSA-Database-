#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite 
import sys
from os import system,name
con = None        
try:
        con = lite.connect('GSA.db') 
        cur = con.cursor()
        myStmt = "go"
        while myStmt != "quit":
                system('cls')
                myStmt = input('Enter SQL Statement :') 
                if myStmt != "quit":
                        cur.execute(myStmt)
                        data = cur.fetchall()
                        print("The results are: ")
                for rec in data:
                        for field in rec: 
                                print(field,"\t",end='')
                        print()
                print()
                myWait = input('Press enter to continue :') 
        con.commit()
        con.close()
except lite.Error as e:
        print("Error %s:" % e.args[0]) 
        sys.exit(1)
