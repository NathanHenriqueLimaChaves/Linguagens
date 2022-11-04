CREATE DATABASE DGT;
SHOW DATABASES;
USE DGT;
SHOW TABLES;
SELECT * FROM departamentos;
SELECT * FROM cargos;

CREATE TABLE departamentos (
	id_departamento int not null auto_increment,
    nome_departamento varchar(125) not null,
    constraint primary key(id_departamento)
);

INSERT INTO departamentos (nome_departamento) VALUES ("Vendas");

CREATE TABLE cargos (
	id_cargo int not null auto_increment,
    nome_cargo varchar(75) not null,
    id_departamento int not null,
    constraint primary key(id_cargo),
    constraint foreign key(id_departamento) REFERENCES departamentos(id_departamento)
);

INSERT INTO cargos (nome_cargo, id_departamento) VALUES ("Vendedor", 9);

CREATE TABLE funcionarios(
id_func int not null auto_increment,
cpf char(11) not null unique,
nome_func varchar(125) not null,
idade int not null,
salario varchar(15) not null,
endereco varchar(150) not null,
telefone varchar(15) not null,
data_nascimento date not null,
data_admissao date not null,
cidade varchar(75) not null,
nacionalidade varchar(30) not null,
id_cargo int not null,
constraint primary key(id_func),
constraint foreign key(id_cargo) REFERENCES cargos(id_cargo)
);

INSERT INTO funcionarios (cpf,nome_func,idade,salario,endereco,telefone,data_nascimento,data_admissao,cidade,nacionalidade,id_cargo)
VALUES ("20221152678", "Thiago Sandre Trevisan", 19, "R$8.100,00", "Rua Trevisan 158", "48990674530", 20031120, 20221026, "Florianópolis", "Brasileiro", 4);

SELECT * FROM funcionarios;

CREATE TABLE dependentes (
	id_dependente int not null auto_increment,
    num_certidao varchar(30) not null,
    nome_dependente varchar(125) not null,
    data_nasci date not null,
    local_nascimento varchar(100) not null,
    id_func int not null,
    constraint primary key(id_dependente),
    constraint foreign key(id_func) REFERENCES funcionarios(id_func)
);

INSERT INTO dependentes (num_certidao,nome_dependente,data_nasci,local_nascimento,id_func)
VALUES ("30465780-189", "Maria Linda Cruz", 20190214, "Florianópolis", 5);

/* exercitando */
SELECT * FROM funcionarios;
SELECT * FROM departamentos;
SELECT * FROM cargos;
SELECT * FROM dependentes;
UPDATE funcionarios SET salario = "R$6.500,00" WHERE id_func = 3; 
SELECT nome_func,idade FROM funcionarios ORDER BY idade DESC;
SELECT * FROM funcionarios ORDER BY nome_func DESC;
SELECT * FROM funcionarios WHERE id_func > 8 AND id_func < 18;
SELECT * FROM funcionarios WHERE id_func IN (1,2,8);
SELECT nome_func,salario FROM funcionarios WHERE nome_func LIKE 'J%';
SELECT nome_func,salario FROM funcionarios WHERE nome_func LIKE '%A';
SELECT COUNT(id_func) AS total FROM funcionarios;
SELECT MIN(salario) AS minímo FROM funcionarios;
SELECT MAX(idade) AS velho FROM funcionarios;
SELECT AVG(idade) AS media FROM funcionarios;
SELECT idade,COUNT(id_func) AS total FROM funcionarios GROUP BY idade HAVING idade <> 17;


