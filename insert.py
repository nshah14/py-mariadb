#!/usr/bin/python

import sys, getopt
import mysql.connector as mariadb
import os

ENV_USER=os.environ['ENV_USER']
ENV_PASS=os.environ['ENV_PASS']
ENV_DB=os.environ['ENV_DB']


def main(argv):
   inputfile = ''
   outputfile = ''

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   insert_data(inputfile, outputfile)

def insert_data( first_name, last_name):
   print ' employee first_name', first_name
   print 'employee last_name', last_name
   mariadb_connection = connect_maria_db()
   cursor = mariadb_connection.cursor()
   cursor.execute("INSERT INTO employees (first_name, last_name) VALUES (%s, %s) ", (first_name, last_name))
   mariadb_connection.commit()

def create_table():
   mariadb_connection = connect_maria_db()
   cursor = mariadb_connection.cursor()
   cursor.execute("CREATE TABLE employees (first_name VARCHAR(255), last_name VARCHAR(255))")





def connect_maria_db():
     print ' environment variable'
     print 'ENV_USER ', ENV_USER
     print 'ENV_PASS ', ENV_PASS
     print 'ENV_DB', ENV_DB
     mariadb_connection = mariadb.connect(user=ENV_USER, password=ENV_PASS, database=ENV_DB)
     return mariadb_connection


if __name__ == "__main__":
   main(sys.argv[1:])
