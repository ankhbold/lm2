set search_path to base, codelists, public;

drop table if exists s_parcel_tbl cascade;
create table s_parcel_tbl
(
parcel_id varchar(12) primary key,
old_parcel_id varchar(14),
geo_id varchar(17),
landuse int references cl_landuse_type on update cascade on delete restrict,
area_m2 decimal,
documented_area_m2 decimal,
address_khashaa varchar(64),
address_streetname varchar(250),
address_neighbourhood varchar(250),
valid_from date default current_date,
valid_till date default 'infinity',
geometry geometry(POLYGON, 4326)
);

grant select, insert, update, delete on s_parcel_tbl to application_update;

--------------------------------

drop table if exists s_parcel_person cascade;
create table s_parcel_person
(
  person_id varchar(10) references bs_person on update cascade on delete restrict,
  parcel_id varchar(12) references s_parcel_tbl on update cascade on delete restrict,
  primary key (parcel_id, person_id)
);

grant select, insert, update, delete on s_parcel_person to application_update;