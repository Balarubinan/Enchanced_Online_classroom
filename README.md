
##Enhanced Online Classroom
##(Project Domain : Web Development and ML)


Introduction:
 Online classes have become a very
essential part of online education due to the
current situation. But it still has a very crude
software in terms of functionalities and needs to
have much more features to enable actual usage
in day to day class situations. The current
solution is the usage of software such as zoom,
Google classroom organise groups among
students. Even these software's have not fully
implemented all the leaps and bounds of
classroom learning. Proposed the solution hopes
to achieve an even more smooth and usable
solution than existing ones using more advanced
techniques like machine learning and create a
more integrated environment for students to learn
and share their classes

Proposed solution:
 Our solution is a combination of web
frameworks and independent machine learning
solutions that work together in a loosely bound
manner to deliver more useful features like
document validation, liveness check , more
easier and automated classroom control to the
users and Organisation using it. Solution also
takes into account its feasibility among the users
as most of its users for students for teachers who
use it almost immediately without any prior
experience. This Solution is meant to be a onestop place for students to take tests , submit
assignments, integrate and co-operate with their
classmates and teachers on a single platform
without depending on any other separate entities.
e the solution also ensures that users are
updated / informed whenever there is a change in
their classroom groups.

Tech/Frameworks used:
● Java (backend)
● Html/css/vanilla-js (frontend)
● Python (ML)
● Flask/Django (Python Rest)
● Sqlite (DBMS)

Architecture:

 The Solution is a web application that will
be based on a Java MVT/MVC modelling. Java
Rest server maybe used as an additional
advantage. The front-end will be created with pure
js and html-css combo much. Unlike traditional
Websites no js library will be used. The machine
learning aspects of the application are to be
handled by a separate python rest server running
Flask/Django to serve ML models with data and
fetch the same during the requests.
 The Classroom will consist of a test
portal, assignment portal , and a sharing portal.
Each portal is separate from the other and will
communicate only based on the interactions of the
teacher/instructor with the students. The application
will also be capable of handling cases like deadpresence (Student is online but wont respond), and
unwanted interventions/unknown access.
