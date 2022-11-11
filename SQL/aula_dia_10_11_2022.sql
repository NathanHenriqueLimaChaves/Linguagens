SHOW DATABASES;
USE dgt;
SELECT * FROM cargos;
SELECT * FROM funcionarios;

SELECT id_func FROM funcionarios WHERE nome_func LIKE 'N%';

CREATE TABLE pessoa(
	id int not null,
    cpf char(11) not null,
    endereco varchar(100),
    telefone char(15),
    constraint primary key(id)
);

DESCRIBE pessoa;
INSERT INTO pessoa SELECT id_func,cpf,endereco,telefone FROM funcionarios;
SELECT * FROM pessoa;  

SELECT func.id_func,func.nome_func,car.nome_cargo FROM funcionarios AS func
INNER JOIN cargos AS car
ON func.id_cargo = car.id_cargo;
