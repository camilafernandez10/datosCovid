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

create user natalia@25.56.171.88;
grant all privileges on DatosCovid.* to natalia@25.56.171.88;
create user santiago@25.57.195.191;
grant all privileges on DatosCovid.* to santiago@25.57.195.191;
create user camila@25.56.168.158;
grant all privileges on datoscovid.*to camila@25.56.168.158;

select month(fecha_reporte_web) as mes, count(*) as contagios from datos 
where fecha_reporte_web between "2020-03-06" and "2020-08-10"
group by month(fecha_reporte_web);

select municipio, count(*) as contagios from datos group by municipio order by contagios desc;
select departamento, sexo, count(*) as contagios from datos 
group by departamento,sexo 
order by departamento desc, contagios asc;

select month("2020-10-01");

select localidad_asis,month(fecha_diagnostico) as mes,count(*) as contagios from datosbogota 
where month(fecha_diagnostico) between 3 and month(curdate()) and localidad_asis<>"Sin dato" and localidad_asis<>'Fuera de Bogotá'
group by localidad_asis,month(fecha_diagnostico) 
order by localidad_asis,mes;  
select distinct localidad_asis from datosbogota where localidad_asis<>"Sin dato" and localidad_asis<>'Fuera de Bogotá';
desc datos;

select departamento,month(fecha_reporte_web) as mes,count(*) as contagios from datos 
where month(fecha_diagnostico) between 3 and month(curdate()) 
group by departamento,month(fecha_reporte_web) 
order by departamento,mes;  


set @total:=0;
select q1.mes,q1.contagios, (@total:=@total+q1.contagios) as acumulado 
from 
(select month(fecha_reporte_web) as mes,count(*)as contagios 
from datos 
where recuperado is null and fecha_de_muerte is null
group by month(fecha_reporte_web) ) as q1;


select month(fecha_reporte_web) as mes,count(*)as contagios from datos 
group by month(fecha_reporte_web);

select count(*)
from datos 
where fecha_de_muerte is null and fecha_de_recuperacion is null;

set @primerDia:=(select fecha_reporte_web from datos where municipio="Tunja" limit 1);

select timestampdiff(day,@primerDia,(select fecha_reporte_web from datos where municipio="Tunja" and @primerDia<fecha_reporte_web limit 1));

set @total:=0;
set @primerDia:=(select fecha_reporte_web from datos where municipio="Bogotá" limit 1);
select q1.fecha,q1.contagios, (@total:=@total+q1.contagios)as acumulado ,
(timestampdiff(day,@primerDia, q1.fecha)) as dia 
from 
(select fecha_reporte_web as fecha,count(*)as contagios 
from datos 
where municipio="Bogotá"
group by fecha_reporte_web ) as q1;

select count(*) from datosBogota;


desc datos;

select distinct municipio from datos where departamento = "Cundinamarca";

select count(*) from datos where municipio="Abejorral";
