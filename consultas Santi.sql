use datosCovid;
select ciudad, count(*) as contagios from datos group by ciudad order by contagios desc;
select departamento, sexo, count(*) as contagios from datos group by sexo,departamento order by contagios desc, departamento;
select atencion, count(*) as persona from datos group by atencion;
select * from datos;