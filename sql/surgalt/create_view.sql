set search_path to base, codelists, admin_units, public;

drop view if exists s_person_parcel_view cascade;
create or replace view s_person_parcel_view as
	
	select row_number() over(), person.person_id, person.name, person.first_name, parcel.parcel_id, parcel.address_khashaa, 
	parcel.landuse, landuse.description, au2.name as soum_name, parcel.geometry from s_parcel_person as person_parcel

	join bs_person as person on person_parcel.person_id = person.person_id
	join s_parcel_tbl as parcel on person_parcel.parcel_id = parcel.parcel_id
	join cl_landuse_type as landuse on parcel.landuse = landuse.code
	join au_level2 as au2 on ST_Within(parcel.geometry, au2.geometry);

grant select, insert, update, delete on s_person_parcel_view to cadastre_update;
grant select on s_person_parcel_view to cadastre_view, reporting;
