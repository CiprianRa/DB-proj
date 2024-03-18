select nume, nume_concert, loc_scena
from muzicieni m,concerte c,participari p
where m.id_muzician=p.id_muzician
and c.id_concert=p.id_concert;

select m.nume,i.nume
from muzicieni m,instrumente i
where m.id_instrument=i.id_instrument;

SELECT m.nume, i.nume AS nume_instrument, rcp.ordine_interpretare
FROM muzicieni m
JOIN participari pcm ON m.id_muzician = pcm.id_muzician
JOIN repertoriu rcp ON pcm.id_concert = rcp.id_concert
JOIN instrumente i ON m.id_instrument = i.id_instrument
WHERE rcp.id_piesa = 1
ORDER BY m.nume;

SELECT
    c.nume_concert,
    c.data,
    i.nume AS nume_instrument,
    i.categorie
FROM
    concerte c
JOIN
    repertoriu r ON c.id_concert = r.id_concert
JOIN
    instrumente i ON r.id_piesa = i.id_instrument
ORDER BY
    c.data DESC;

SELECT
    id_concert,
    nume_concert,
    data,
    oras
FROM
    concerte
WHERE
    data BETWEEN ADD_MONTHS(SYSDATE, -3) AND SYSDATE;

INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('Gheorghe Maestro', 'gheorghe.m@gmail.com', '+40 721 789 012');
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Concert Nou', TO_DATE('2023-12-25', 'YYYY-MM-DD'), 'Brasov', 5);
INSERT INTO instrumente (nume, categorie) VALUES ('Flaut', 'suflat');
INSERT INTO muzicieni (nume, nr_de_telefon, email, id_instrument) VALUES ('Laura Harmonie', '+40 721 567 890', 'laura.h@gmail.com', 5);
INSERT INTO participari (id_muzician, id_concert, loc_scena) VALUES (5, 5, 3);
INSERT INTO piese (titlu_piesa, numele_autorului) VALUES ('Valsul Dragostei', 'Ion Composer');
INSERT INTO repertoriu (id_concert, id_piesa, ordine_interpretare) VALUES (5, 5, 1);


UPDATE dirijori SET nume = 'Gheorghe Maestru' WHERE id_dirijor = 5;
UPDATE concerte SET nume_concert = 'Concert de Craciun' WHERE id_concert = 5;
UPDATE muzicieni SET nume = 'Laura Harmonica' WHERE id_muzician = 5;
UPDATE participari SET loc_scena = 4 WHERE id_muzician = 5 AND id_concert = 5;
UPDATE piese SET titlu_piesa = 'Valsul Dragostei Eternale' WHERE id_piesa = 5;
UPDATE repertoriu SET ordine_interpretare = 2 WHERE id_concert = 5 AND id_piesa = 5;

DELETE FROM participari WHERE id_muzician = 5 AND id_concert = 5;
DELETE FROM repertoriu WHERE id_concert = 5 AND id_piesa = 5;
DELETE FROM concerte WHERE id_concert = 5;
DELETE FROM dirijori WHERE id_dirijor = 5;
DELETE FROM muzicieni WHERE id_muzician = 5;
DELETE FROM instrumente WHERE id_instrument = 5;
DELETE FROM piese WHERE id_piesa = 5;

-- Adăugare peste constrangere unique
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('C1', TO_DATE('2023-12-25', 'YYYY-MM-DD'), 'Brasov', 1);
-- Adăugare concert nou cu nume prea lung
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Concert cu un nume foarte foarte lung pentru a depasi limita', TO_DATE('2023-12-25', 'YYYY-MM-DD'), 'Brasov', 1);
-- Adăugare dirijor cu adresă de e-mail invalidă
INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('Gigel Dirijorul', 'gigel_dirijor', '+40 721 111 111');
-- Adăugare dirijor cu adresă de e-mail validă
INSERT INTO dirijori (nume, email, nr_de_telefon) VALUES ('Maria Dirijoarea', 'maria.dirijoarea@email.com', '+40 721 222 222');
-- Adăugare concert nou cu nume valid
INSERT INTO concerte (nume_concert, data, oras, id_dirijor) VALUES ('Concert de Revelion', TO_DATE('2023-12-31', 'YYYY-MM-DD'), 'Bucuresti', 8);
-- Adăugare instrument cu categorie invalidă
INSERT INTO instrumente (nume, categorie) VALUES ('Trompeta', 'categorii_nedefinite');
-- Adăugare instrument cu categorie validă
INSERT INTO instrumente (nume, categorie) VALUES ('Trompeta', 'suflat');