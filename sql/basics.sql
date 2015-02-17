create table pets (
  id                serial   PRIMARY KEY NOT NULL,
  owner_id          int,
  name              varchar(80),
  specie            varchar(80),
  colour            varchar(80),
  date_of_birth     date
);

create table owners (
  id                serial   PRIMARY KEY NOT NULL,
  first_name        varchar(80),
  last_name         varchar(80),
  date_of_birth     date,
  city              varchar(80)
);
