create database DatosCovid;
use DatosCovid;
drop table datos;
Create table datos(
fecha_reporte_web timestamp,
idCaso int not null primary key,#0 check
fecha_de_notificacion timestamp , #1 check
departamento varchar (70) , #3 check
municipio varchar(70) , #2 check
edad int not null,#5 check
sexo varchar(1) ,#6 check
tipoContagio varchar(50) , #7 check
ubicacion varchar(20), #19 check 
estado varchar(50) ,#8
paisProcedencia varchar(50) ,#9
recuperado varchar (11),
fecha_inicio_sintomas timestamp ,#10
fecha_de_muerte timestamp null, #11
fecha_diagnostico timestamp ,#12
fecha_de_recuperacion timestamp null,#13
tipo_recuperacion varchar(50),#15
nombreGrupoEtnico varchar(70)
);
drop table datos;
select * from datos where fechaDiagnostico between '2020-09-01' and '2020-09-30' order by fechaDiagnostico desc;

create table datosBogota(
id int auto_increment primary key,
fecha_inicio_sintomas date,
fecha_diagnostico date,
ciudad varchar(20),
localidad_asis varchar(50),
edad int,
sexo varchar(1),
fuente_o_tipo_contagio varchar(30),
ubicacion varchar(20),
estado varchar(18)
);

replace into datos 
values (fecha_reporte_web,idCaso, fecha_de_notificacion, departamento,municipio,edad,sexo,tipoContagio,ubicacion,estado,paisProcedencia,recuperado,fecha_inicio_sintomas,fecha_de_muerte,fecha_diagnostico,fecha_de_recuperacion,tipo_recuperacion,nombreGrupoEtnico);
use mysql;

insert into datos (fecha_inicio_sintomas,fecha_diagnostico,ciudad,localidad_asis,edad,sexo,fuente_o_tipo_contagio,ubicacion,estado)values
create user natalia@25.56.171.88;
grant all privileges on DatosCovid.* to natalia@25.56.171.88;
create user santiago@25.57.195.191;
grant all privileges on DatosCovid.* to santiago@25.57.195.191;
create user camila@25.56.168.158;
grant all privileges on datoscovid.*to camila@25.56.168.158;

select ciudad, count(*) as contagios from datos group by ciudad order by contagios desc;
select departamento, sexo, count(*) as contagios from datos 
group by departamento,sexo 
order by departamento desc, contagios asc;