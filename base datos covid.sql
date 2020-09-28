create database DatosCovid;
use DatosCovid;

Create table datos(
idCasos int not null primary key,#0
fechaNotificacion timestamp , #1
codigoDIVIPOLA int not null , #2
ciudad varchar(50) , #3
departamento varchar (70) , #4
atencion varchar(50) ,#5
edad int not null,#6
sexo varchar(1) ,#7
tipo varchar(50) , #8
estado varchar(50) ,#9
paisProcedencia varchar(50) ,#10
fis timestamp ,#11
fechaDeMuerte timestamp null, #12
fechaDiagnostico timestamp ,#13
fechaRecuperado timestamp null,#14
fechaReporteWeb timestamp ,#15
tipoRec varchar(50),#16
codigoDepartamento int not null,#17
codigoPais int null,#18
etnia varchar(50),#19 
nombreGrupoEtnico varchar(70));#20
drop table datos;
select * from datos;

insert ignore into datos 
values (idCasos, fechaNotificacion, codigoDIVIPOLA, ciudad, departamento,atencion,edad,sexo,tipo,estado,paisProcedencia,fis,fechaDiagnostico, fechaRecuperado,fechaReporteWeb,tipoRec,codigoDepartamento,codigoPais,etnia);

replace into datos 
values (idCasos, fechaNotificacion, codigoDIVIPOLA, ciudad, departamento,atencion,edad,sexo,tipo,estado,paisProcedencia,fis,fechaDiagnostico, fechaRecuperado,fechaReporteWeb,tipoRec,codigoDepartamento,codigoPais,etnia);
use mysql;
create user natalia@25.56.171.88;
grant all privileges on DatosCovid.* to natalia@25.56.171.88;
create user santiago@25.57.195.191;
grant all privileges on DatosCovid.* to santiago@25.57.195.191;
