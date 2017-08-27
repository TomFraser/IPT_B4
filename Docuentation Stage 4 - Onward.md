<h1> </h1>

<h1> </h1>

# IPT B4 Assignment

### Thomas Fraser | 12 Hamilton

### Stages 4-6

<P hidden>Page Break to end the page 👍</P>

<P style="page-break-before: always"></P>

## Stage 4 - Implementation

The Web Application was designed using web technologies such as Python, Flask, Sqlite3, HTML, CSS and a tid-bit of Javascript. All of these technologies came together to form the bases of a Web Application designed to help staff member request and organise room changes. Database and HTML web page construction was one of the most time consuming and difficult stages of the Web App design and construction. Many changes were made from the database provided in the CSD and ONF diagrams as it was found that the layout of the database would not be able to achieve the desired usability. Changes to the database layout include the introduction of tables labeled; 'ROOMTIMETABLE' and 'CHANGES'. These two tables contain the timetable for each room and the changes requested across the system respectively. These tables replaced most of the need for the 'COURSES' table however it is still used for some course naming around the app and therefore cannot be removed from the database. Due to a lack of time to complete the web application, the component that notified students of database changes had to be removed from the project. The aforementioned changes to the database led to the lack of time causing certain parts of the project design to be not completed. With that being said, the student notification part of the project could be implemented somewhat easily if extra time was allowed. Changes were made to the staff table to contain a 'schoolboxstaffId' column that contains the staff members SchoolBox UID. This is used to automatically collect and display the staff members picture by using the SchoolBox database that already exists. However, for this feature to work, the user of the Web App must be signed into SchoolBox as well. Queries to the database mostly consist of 'SELECT' queries with the occasional 'INSERT' query used to place room change information into the database.

###### Example Queries

The login query to check user login information

![Screen Shot 2017-08-27 at 12.38.58 pm](../../../../../Desktop/Screen Shot 2017-08-27 at 12.38.58 pm.png)

The query that collects information about a room pertaining to a certain period and day of the week

![Screen Shot 2017-08-27 at 12.39.10 pm](../../../../../Desktop/Screen Shot 2017-08-27 at 12.39.10 pm.png)

The query that collects information about a change before displaying it to a user in the 'view' tab

![Screen Shot 2017-08-27 at 12.39.22 pm](../../../../../Desktop/Screen Shot 2017-08-27 at 12.39.22 pm.png)

The query that adds the room change into the 'CHANGES' table

![Screen Shot 2017-08-27 at 12.43.05 pm](../../../../../Desktop/Screen Shot 2017-08-27 at 12.43.05 pm.png)

 ###### Final Database Design

 ###### ![Screen Shot 2017-08-27 at 12.42.11 pm](../../../../../Desktop/Screen Shot 2017-08-27 at 12.42.11 pm.png)

## Stage 5 - Testing

####Test Design



## Stage 6 - Evaluation

