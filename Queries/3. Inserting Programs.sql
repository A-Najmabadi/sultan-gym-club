-- SQLite
PRAGMA foreign_keys = ON;

INSERT INTO Program (sat, sun, mon, tue, wed, thu, fri)
VALUES ('Chest-Day', 'Arm-Day', 'Leg-Day', 'Rest-Day', 'Full-Day', 'S-Day', 'Rest-Day');

INSERT INTO Program (sat, sun, mon, tue, wed, thu, fri)
VALUES ('Chest-Day', 'Chest-Day', 'Arm-Day', 'Arm-Day', 'Leg-Day', 'Leg-Day', 'Rest-Day');

INSERT INTO Program (sat, sun, mon, tue, wed, thu, fri)
VALUES ('Leg-Day', 'Leg-Day', 'Full-Day', 'Leg-Day', 'Leg-Day', 'Full-Day', 'Rest-Day');

INSERT INTO Program (sat, sun, mon, tue, wed, thu, fri)
VALUES ('Chest-Day', 'Rest-Day', 'Arm-Day', 'Rest-Day', 'Leg-Day', 'S-Day', 'Rest-Day');

INSERT INTO Program (sat, sun, mon, tue, wed, thu, fri)
VALUES ('Full-Day', 'S-Day', 'Full-Day', 'S-Day', 'Full-Day', 'S-Day', 'Rest-Day');

INSERT INTO Program (sat, sun, mon, tue, wed, thu, fri)
VALUES ('CA-Day', 'AL-Day', 'CL-Day', 'Rest-Day', 'Full-Day', 'S-Day', 'Rest-Day');

