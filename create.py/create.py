#!/usr/bin/python

import sys, getopt
import mysql.connector as mariadb
import os

ENV_USER=os.environ['ENV_USER']
ENV_PASS=os.environ['ENV_PASS']
ENV_DB=os.environ['ENV_DB']
MARIA_DB_HOST=os.environ['MARIA_DB_HOST']
CREATE_DB_QUERY = "CREATE DATABASE employees"
CREATE_TABLE_QUERY="CREATE TABLE employees (first_name VARCHAR(255), last_name VARCHAR(255))"

def main(argv):
    create_DB()
    create_table()


def create_DB():
    mariadb_connection = connect_maria_db()
    cursor = mariadb_connection.cursor()
    cursor.execute(CREATE_DB_QUERY)
    print ' executed query :  '
    closeConnection(mariadb_connection)

def create_table():
   mariadb_connection = connect_maria_db()
   cursor = mariadb_connection.cursor()
   cursor.execute(CREATE_TABLE_QUERY)
   closeConnection(mariadb_connection)


def closeConnection(mariadb_connection)
    print 'executed query '
    mariadb_connection.cursor().close()
    mariadb_connection.close()
    print 'cursor and connection closed' 

def connect_maria_db():
     print ' environment variable'
     print 'ENV_USER ', ENV_USER
     print 'ENV_PASS ', ENV_PASS
     print 'ENV_DB', ENV_DB
     print 'MARIA_DB_HOST', MARIA_DB_HOST
     mariadb_connection = mariadb.connect(user=ENV_USER, password=ENV_PASS, database=ENV_DB, host=MARIA_DB_HOST)
     return mariadb_connection


if __name__ == "__main__":
   main()