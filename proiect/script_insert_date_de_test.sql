INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('John Doe', 'john_doe@gmail.com', '+40 721 123 456');
INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('Anna Maestro', 'anna_maestro@gmail.com', '+40 721 987 654');
INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('David Maestru', 'david.m@gmail.com', '+40 721 456 789');
INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('Emily Director', 'emily_d@gmail.com', '+40 721 321 654');
INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('George Maestro', 'george_maestro@gmail.com', '+40 721 876 543');

INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Concert Clasic', TO_DATE('2023-12-20', 'YYYY-MM-DD'), 'Bucuresti', 1);
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Serata Muzicala', TO_DATE('2023-11-15', 'YYYY-MM-DD'), 'Timisoara', 2);
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Recital Pian', TO_DATE('2023-10-05', 'YYYY-MM-DD'), 'Cluj-Napoca', 3);
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Concert Simfonic', TO_DATE('2024-01-10', 'YYYY-MM-DD'), 'Iasi', 4);

INSERT INTO instrumente (nume, categorie) VALUES ('Vioara', 'coarda_arcus');
INSERT INTO instrumente (nume, categorie) VALUES ('Trompeta', 'suflat');
INSERT INTO instrumente (nume, categorie) VALUES ('Pian', 'complexe');
INSERT INTO instrumente (nume, categorie) VALUES ('Chitara', 'coarda_arcus');
INSERT INTO instrumente (nume, categorie) VALUES ('Flaut', 'suflat');

INSERT INTO muzicieni (nume, nr_de_telefon, email, id_instrument) VALUES ('Alex Muzicant', '+40 721 111 111', 'alex.m@gmail.com', 1);
INSERT INTO muzicieni (nume, nr_de_telefon, email, id_instrument) VALUES ('Bianca Sonor', '+40 721 222 222', 'bianca_s@gmail.com', 2);
INSERT INTO muzicieni (nume, nr_de_telefon, email, id_instrument) VALUES ('Cristian Virtuoz', '+40 721 333 333', 'cristian.virtuoz@yahoo.com', 3);
INSERT INTO muzicieni (nume, nr_de_telefon, email, id_instrument) VALUES ('Diana Armonie', '+40 721 444 444', 'diana_ar@yahoo.com', 1);
INSERT INTO muzicieni (nume, nr_de_telefon, email, id_instrument) VALUES ('Eva Armonica', '+40 721 555 555', 'eva.armonica@hotmail.com', 4);

INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (1, 1, 1);
INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (2, 1, 2);
INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (3, 2, 1);
INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (4, 3, 2);
INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (1, 4, 1);
INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (4, 4, 2);

INSERT INTO piese (titlu_piesa, numele_autorului) VALUES ('Simfonia Primavara', 'Mihai Compozitorul');
INSERT INTO piese (titlu_piesa, numele_autorului) VALUES ('Concert pentru Pian', 'Ana Autorul');
INSERT INTO piese (titlu_piesa, numele_autorului) VALUES ('Serenada Nocturna', 'Dan Scriitorul');
INSERT INTO piese (titlu_piesa, numele_autorului) VALUES ('Valsul Lunii', 'Elena Maestrul');
INSERT INTO piese (titlu_piesa, numele_autorului) VALUES ('Adagio pentru Vioara', 'Alex Compozitorul');


INSERT INTO repertoriu (id_concert, id_piesa, ordine_interpretare) VALUES (1, 1, 1);
INSERT INTO repertoriu (id_concert, id_piesa, ordine_interpretare) VALUES (1, 2, 2);
INSERT INTO repertoriu (id_concert, id_piesa, ordine_interpretare) VALUES (2, 3, 1);
INSERT INTO repertoriu (id_concert, id_piesa, ordine_interpretare) VALUES (3, 4, 1);
INSERT INTO repertoriu (id_concert, id_piesa, ordine_interpretare) VALUES (4, 5, 1);