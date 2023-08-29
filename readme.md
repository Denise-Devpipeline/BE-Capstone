Login:8888
Password:deezcapstone@gmail.com

Link for BE Capstone Postman collection:
https://solar-meadow-704042.postman.co/workspace/Team-Workspace~ecc52ca2-7897-4d33-8f19-0ed314512819/collection/25296206-11a318af-8dfc-4858-abf5-68aa4dbb24c4?action=share&creator=25296206

About:
This idea is about event planning. There are customers that work with event planners to work out planned events with dates, themes and services provided.

Event Planner has 5 tables.
*Customer
*Event Planner
*Event Services
*Planner Event xRef
\*Venue

File Access:
\*Customer has access to adding user, updating only that user. Upon set up they are authmatically set to active.
They cannot delete, activate, deactivate, or get all customers.

\*Event Planner has access to adding, updating, activating, deactivating, deleting and get all for a customer.
A planner should be able to add, update, activate, deactivate themselves.  
Not be able to delete themselves.
Planners should be able to view everything on Event Services and on Venue tables.

In Postman you can: SEE Postman Collection called "BE Capstone"

When a customer wants to add themself to the database, they must fill in all fields:
First Name
Last Name
Phone
email
password
city
state
event date
active - is automatic

When a planner wants to add themself to the database, they must fill in all fields:
Phone
email
password
specialty
active - is automatic
