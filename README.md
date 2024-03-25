# Streamlit Python Dynamic Dashboard

## **Getting Started**

1. Un-zip the envStreamlit.7z file containing the python env
2. Be sure to place all of your tables in as many CSV files than you have table. The CSV folder/file MUST follow this type :

   - separated by coma ","
   - encoding = UTF8
   - 1 file = 1 table
   - file name = table name

   ```csv
   Date,HeureDebut,Duree,Cours,CodeCours,Local,Site,ConcatAnneeEtudeSection_UF
   2024-01-08,10:30,120,Machines tournantes  triphasées,E2081,S13,SCH,2° Electromécanique
   2024-01-08,10:45,120,Statistique et mathématiques financières,X104,124,WLW,1° International Business
   2024-01-08,10:45,120,Statistique et mathématiques financières,X104,125,WLW,1° International Business
   2024-01-08,10:45,120,Statistique et mathématiques financières,X104,127,WLW,1° International Business
   2024-01-08,10:45,120,Statistique et mathématiques financières,X104,A04,WLW,1° International Business
   ```
3. Run the following command, in order to deleting the existing docker compose file for a fresh start

   ```bash
   docker-compose down
   docker-compose build
   docker-compose up
   ```

   Notice that we are here using the wait-for-it.sh script that can be found on this repo [(vishnubob/wait-for-it)](https://github.com/vishnubob/wait-for-it)

## Customization Options

Have a look at the *color_cells()* method described in the maindashboard top lines and custom the differents aspect rules your way.

## Bibliography

To carry out this project, I used several sources such as:

* Streamlit's online documentation
* The .pdf documents attached in the eponymous folder
