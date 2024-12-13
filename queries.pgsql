CREATE TABLE IF NOT EXISTS menu_school (
    id serial primary key,
    num int,
    sana date,
    kun text,
    vaqt text,
    ovqat_turi text
);

TRUNCATE TABLE menu_school;