create database DatosCovid;
use DatosCovid;

Create table datos(
idCasos int not null primary key,
fechaNotificacion timestamp ,
codigoDIVIPOLA int not null ,
ciudad varchar(50) ,
departamento varchar (50) ,
atencion varchar(50) ,
edad int not null,
sexo varchar(1) ,
tipo varchar(50) ,
estado varchar(50) ,
paisProcedencia varchar(50) ,
fis timestamp ,
fechaDiagnostico timestamp ,
fechaRecuperado timestamp ,
fechaReporteWeb timestamp ,
tipoRec varchar(50),
codigoDepartamento int not null,
codigoPais int not null,
etnia varchar(50) );

insert ignore into datos 
values (idCasos, fechaNotificacion, codigoDIVIPOLA, ciudad, departamento,atencion,edad,sexo,tipo,estado,paisProcedencia,fis,fechaDiagnostico, fechaRecuperado,fechaReporteWeb,tipoRec,codigoDepartamento,codigoPais,etnia);

replace into datos 
values (idCasos, fechaNotificacion, codigoDIVIPOLA, ciudad, departamento,atencion,edad,sexo,tipo,estado,paisProcedencia,fis,fechaDiagnostico, fechaRecuperado,fechaReporteWeb,tipoRec,codigoDepartamento,codigoPais,etnia);
use mysql;
create user natalia@25.56.171.88;
grant all privileges on DatosCovid.* to natalia@25.56.171.88;
create user santiago@25.57.195.191;
grant all privileges on DatosCovid.* to santiago@25.57.195.191;

select *from prueba;