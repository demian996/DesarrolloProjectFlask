CREATE DATABASE DBEmpleadosFlask;
USE DBEmpleadosFlask;

CREATE TABLE Usuario(
idUsuario int primary key identity(1,1),
nickname varchar(50),
contrasena varchar(50)
);

insert into Usuario(nickname, contrasena) values ('jdcrespo','123456');

CREATE PROCEDURE CrearUsuario(
@NickName varchar(50),
@Contrasena varchar(50)
)
AS
BEGIN
	insert into Usuario (nickname, contrasena) values
	(@NickName, @Contrasena)
END

CREATE PROCEDURE ListarUsuario
AS
BEGIN
	select idUsuario, nickname, contrasena from Usuario
END

CREATE PROCEDURE EditarUsuario(
@idUsuario int,
@NickName varchar(50),
@Contrasena varchar(50)
)
AS
BEGIN
	UPDATE Usuario SET
	nickname= @NickName,
	contrasena=@Contrasena
	where idUsuario = @idUsuario
END

CREATE PROCEDURE EliminarUsuario(
@idUsuario int
)
AS
BEGIN
	delete from Usuario
	where idUsuario = @idUsuario
END

create PROCEDURE VerificarUsuario
    @nickName VARCHAR(50),
    @contrasena VARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @Result INT;

    SELECT @Result = CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END
    FROM Usuario 
    WHERE nickname = @nickName AND contrasena = @contrasena;

    SELECT @Result AS Result;
END



select * from Usuario
exec CrearUsuario 'felipe','12345';
exec ListarUsuario;
exec EliminarUsuario 2;
exec VerificarUsuario 'felipe', '123456';

