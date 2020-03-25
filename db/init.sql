CREATE TABLE Persons (
    PersonID serial primary key,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO Persons(PersonID, LastName, FirstName, Address, City)
VALUES (1, 'McDonald', 'Jordan', '1 Road', 'Town');