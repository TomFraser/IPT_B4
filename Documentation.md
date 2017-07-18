<h1> </h1>

<h1> </h1>

# IPT B4 Assignment

### By Thomas Fraser | 12 Hamilton

### Stages 1-3

<P hidden>Page Break to end the page :thumbsup:</P>

<P style="page-break-before: always"></P>

## Stage 1 - Identification

#### Preamble

All too often do room changes at schools cause confusion and cause a waste of time for both staff and students. As the current system stands, there is no clear communication between students and staff relating room changes. Room changes are often never communicated to students. This project to be introduced aims to solve this problem with automation the room change system and database controlled information.

#### Solution

The aforementioned project provides a solution to the problem of classroom scheduling. The solution to the problem is to conceive, design and build a web based application using Python and Flask that will allow teachers to create, modify and notify students to room changes. The solution must be capable of allowing teachers to request room changes, confirm room changes wile giving a reason and to notify students via either email or integration with school box, the primary web tool used at the school. Teachers should have the ability to, via a web interface, view the class allocated to a classroom in a period and request a change. The system should be intuitive and the staff should have to enter minimal details. Some details required would be the time frame that the classroom is needed for, the date and a reason for the change. This information would then be sent via email to the staff member occupying the requested classroom. The staff member will then be offered a chance to accept the change. If the change is accepted, the teacher will be found a new free classroom automatically by the system. Once this process is completed, both teacher will be emailed a confirmation of the switch and the students of both classes will either be emailed or notified via school box about the changes.

## Stage 2 - Conceptualisation 

The goal of the project is to make a useful application that can be used by the staff and students of Brisbane Boys' College to make menial day to day tasks much easier and intuitive to complete. The success of the system will be determined by two factors. The ease of use of the system and overall acceptance of the system by staff. The project can be deemed a success if it is widely accepted at the college as the most functional system for organising room changes. The end user of the project should be able to easily organise room changes without lengthy email chains or confusing interactions communication. The system will contain data relating to rooms, classes, teachers, students and subjects. The information will be organised into tables in a database and related to each other using primary and foreign keys.

<P hidden>Page Break to end the page :thumbsup:</P>

<P style="page-break-before: always"></P>

###### Data Table Example

PK = Primary Key, FK = Foreign Key

| STUDENT       | Subject   | TEACHER       | ROOM    | ROOMCHANGE | STUDENT-SUBJECT  |
| ------------- | --------- | ------------- | ------- | ---------- | ---------------- |
| StudentID     | SubjectID | TeacherID     | RoomID  | RequestID  | StudentSubjectID |
| Student Name  | Name      | Teacher Name  | Block   | Course1ID  |                  |
| Student Email | RoomID    | Teacher Email | Subject | Course2    |                  |
| SubjectID     | TeacherID |               |         |            |                  |
|               | Old_room  |               |         |            |                  |
|               | New_Room  |               |         |            |                  |

The staff members will interact with the database using a Graphical User Interface (GUI) based in a web browser that will be written using web technologies such as HTML and CSS for the front end with a robust PYTHON and FLASK backend. The user interface will allow teachers to access with the database in a simple, intuitive and informative fashion. The user interface should be designed so that no to little instruction or training should be provided to the teachers prior to the introduction of the project into the school ecosystem.

###### WireFrame UI Example

![WireFrame UI](WireFrame UI.png)

<P hidden>Page Break to end the page :thumbsup:</P>

<P style="page-break-before: always"></P>

## Stage 3 - Formalisation		 

==//I Should have some writing here==

###### Elementary Facts

**STUDENT** has StudentID '18135'

**STUDENT** '18135' has Name '*Thomas* *Fraser*'

**STUDENT** '18135' has Email '*18135@bbc.qld.edu.au*'

**STUDENT** '18135' has CourseID '*IPT_4*'

<h1></h1>

**SUBJECT** has SubjectID '181201'

**SUBJECT** '181201' has Name '*IPT*' 

**SUBJECT** '181201' has RoomID '*R207*'

**SUBJECT** '181201' has TeacherID '*1451*' 

**SUBJECT** '181201' has Old_Room '*R207*' 

**SUBJECT** ' 181201' has New_Room '*R205*' 

<h1></h1>

**TEACHER** has TeacherID '1415'

**TEACHER** '1451' has Name '*Ron* *Plumlee*' 

**TEACHER** '1415' has Email '*rplumlee@bbc.qld.edu.au*' 

<h1></h1>

**ROOM** has RoomID 'R207'

**ROOM** 'R207' has Block '*Rudd Block*' 

**ROOM** 'R206' has Subject '*IT*'

<h1></h1> 

**ROOMCHANGE** has RoomChangeID '2038'

**ROOMCHANGE** '2038' Course1ID '*IPT*' 

**ROOMCHANGE** '2038' Course2ID '*ITS*'

###### Data Dictionary

| Field Name        | Data Type | Constraint  | Description                              |
| ----------------- | --------- | ----------- | ---------------------------------------- |
| **STUDENT TABLE** |           |             |                                          |
| StudentID         | INT       | Primary Key | Student Identifier                       |
| Student Name      | TEXT      | Not null    | Name of the student                      |
| Student Email     | TEXT      | Not null    | Email of the student                     |
| **SUBJECT TABLE** |           |             |                                          |
| SubjectID         | INT       | Primary Key | Subject Identifier                       |
| Name              | TEXT      | Not null    | Name of the subject                      |
| RoomID            | INT       | Foreign Key | Room that the class is normally in       |
| TeacherID         | INT       | Foreign Key | Identifier for the teacher taking the class |
| Old_Room          | INT       | Not null    | Old room for the subject                 |
| New_Room          | INT       | Not null    | New room for the subject                 |
| **TEACHER TABLE** |           |             |                                          |
| TeacherID         | INT       | Primary Key | Teacher Identifier                       |
| Teacher Name      | TEXT      | Not null    | Name of the teacher                      |
| Teacher Email     | TEXT      | Not null    | Email of the email                       |
| **ROOM TABLE**    |           |             |                                          |
| RoomID            | INT       | Primary Key | Identifier of the room                   |
| Block             | TEXT      | Not null    | Building that the class room is in       |
| Subject           | TEXT      | Not null    | The primary subject for the room         |
| **REQUEST TABLE** |           |             |                                          |
| RequestID         | INT       | Primary Key | The room change request Identifier       |
| Course1ID         | INT       | Not null    | STUDENT-SUBJECT table relating to course 1 |
| Course2ID         | INT       | Not null    | STUDENT-SUBJECT table relating to course 2 |
| **SS TABLE**      |           |             |                                          |
| StudentSubjectID  | INT       | Primary Key | The ID for the combination table of student and subject |
|                   |           |             |                                          |

###### Conceptual Schema Diagram (CSD)

![CSG FINAL](CSD FINAL.svg)

<P hidden>Page Break to end the page :thumbsup:</P>

<P style="page-break-before: always"></P>

###### Optimal Normal Form CSD

![CSG ONF FINAL](CSD ONF FINAL.svg)



<P hidden>Page Break to end the page :thumbsup:</P>

<P style="page-break-before: always"></P>

###### Relational Schema Diagram

![ERD FINAL](ERD FINAL.svg)



###### UI Design



