-- Keep a log of any SQL queries you execute as you solve the mystery.

-- First looking through all the cases reports of 28 July, 2021 and finding about the witnesses.
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28 ORDER BY street;
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Looking through the witnesses on the day of the crime and finding out who were the three witnesses and what was there statements.
SELECT * FROM interviews WHERE month = 7 AND day = 28 ORDER BY name;
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- According to statement of Ruth the theif drove away from the bakery sometimes within ten minutes of theft, so hence looking through the license plate.
SELECT hour, minute, activity, id, license_plate FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 ORDER BY minute;
-- After running through this query we looked through the cars plate who left between 10:15am and 10:25am.
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- To find theaccount number of the person who withdraw the money according to the Eugene's statment, early in the morning at Leggett Street.
SELECT account_number, transaction_type, amount, id FROM atm_transactions
WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = "Leggett Street";
-- After executing this we look through the people who has withdram the money.
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Short numbering people by the id number from the bank transactions and finding out there account number so we can find their person_id.
SELECT * FROM bank_accounts
WHERE account_number IN ('28296815', '76054385', '49610011', '28500762', '16153065', '25506511', '81061156', '26013199');
-- After executing this we came to know there "person_id".
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- To find the people who called around the time of the crime.
-- According to Raymond's statement the theif and her/his accomplice talked less than a minute so.
SELECT id, caller, receiver, duration FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28
AND duration < 60;
-- So we came across the suspect's numbers who talked at that day.
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Now looking for the thief through the people table to find about them according to the license plate, the caller phone number and the person's id founded
-- through bank account number.
SELECT * FROM people
WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55')
INTERSECT
SELECT * FROM PEOPLE
WHERE id IN ('686048', '514354', '458378', '396669', '395717', '467400', '449774', '438727');
-- After having the data by applying this query we matched the phone number and founded two person "Diana" and "Bruce" as suspects of theft.
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Searching for the people who talked to the suspects.
SELECT * FROM people
WHERE phone_number IN ('(375) 555-8161', '(725) 555-3243' );
-- After executing this we came across two people "Philip" and "Robin".
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Now looking through the flights id and their seats the suspect took
SELECT flights.hour, flights.minute, flights.origin_airport_id, airports.full_name, airports.city, passengers.passport_number, airports.id
FROM flights JOIN airports ON airports.id = flights.origin_airport_id
JOIN passengers ON passengers.flight_id = flights.id
WHERE passengers.passport_number IN ('3592750733', '5773159633')
AND flights.year = 2021 AND flights. month = 7 AND flights.day = 29;
-- After running this we came to know that Bruce took the earliest flight from fiftyville
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Now we have written SQL query to find out the Bruce's destination.
 SELECT * FROM airports WHERE id = 4;
 -- After we run this we came to know that Bruce escaped to New York City from Fiftyville with the earliest flight.
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

 -- To recheck if the Bruce"s id, phone number, passport number and license plate matches of that the thief we run this query
 SELECT * FROM people WHERE name LIKE "Bruce";
-- And this proves that "Bruce" is intead the thief
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- To know his accomplice we will run this query
SELECT receiver FROM phone_calls WHERE caller = "(367) 555-5533" AND year = 2021 AND month = 7 AND day = 28 AND duration < 60;
--After running this query we came to know the phone number of the thief's partner
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+-----------------+

-- Now we confirm again that the receiver is indeed Robin by looking at his phone number
SELECT * FROM people WHERE name = "Robin";
-- After running this we came to know that Bruce talked to Robin at that time, whom helped him escaped from fiftyville
+---------------+----------------------+---------------------+--------------------------------+---------------+--------------------+------------------+
--------------====--------------------==== ----------------====------ THE END OF THE CASE ----====------------====----------------====-----------------
+---------------+----------------------+---------------------+--------------------------------+---------------+------- ------------+------------------+