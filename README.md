# ETL with python

In this repo, I implement a simple ETL pipeline with python that Extracts the, data from one source (web site) and performs some transformations on it, and finally load the data into data warehouse.

# files description:
**data** -> contains two folders, 
- **source** -> contains the downloaded data which is in compressed format.
- **row** -> contains the data after unzipped it (the row data).

**scripts** -> contains the scripts I used to implement the pipeline,
- **common** -> contains the scripts that connect to the database and instantiate the tables (we need to edit the database details in **base.py** file and then run **create_tables.py** in order to connect to your database and create the needed tables).
- **extract.py** -> downloads the new dataset from the source and save it at **data/source**, then unzip the downloaded file to get the row data and save it at **data/row**. Every time the ETL is performed, it save the data in a new folder whos name is the date on which it was made.
- **transform.py** -> performs some changes on the data such as make all string data in lower case, removing symbols from price column and save it as integer, update date format, and some other changes. and fianlly save the data at a temporary table in the database.
- **load.py** -> loads the data into a new clean table.
- **execute.py** -> this file is the one we need to run to start the pipeline. By running this file, it calls all the functions I have implemented the above three files. so when we need to get new data and start the pipeline to perform all the ETL steps, all we have to do is to run this file.
