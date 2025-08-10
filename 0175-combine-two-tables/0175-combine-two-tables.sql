SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN ADDRESS a on p.personId=a.personId