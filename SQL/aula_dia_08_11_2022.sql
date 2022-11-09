SHOW DATABASES;
USE DGT;
SHOW TABLES;
SELECT * FROM funcionarios;

CREATE DATABASE garagem;
SHOW DATABASES;
SHOW TABLES;
USE garagem;
CREATE TABLE pessoa (
	id_pessoa int not null auto_increment,
    cpf char(11) unique not null,
    nome varchar(125) not null,
    constraint primary key (id_pessoa)
);

CREATE TABLE carro (
	id_carro int not null auto_increment,
    ranavam int unsigned zerofill not null,
    placa char(8) not null,
    id_pessoa int not null,
    constraint primary key (id_carro),
    constraint foreign key (id_pessoa) references pessoa(id_pessoa)
);

INSERT INTO pessoa (cpf,nome) VALUES ("1111111", "Nathan Henrique");
INSERT INTO pessoa (cpf,nome) VALUES ("1111114", "Thiago Reis");
SELECT * FROM pessoa;

INSERT INTO carro (ranavam,placa,id_pessoa) VALUES (2248, "POLO", 3);
INSERT INTO carro (ranavam,placa,id_pessoa) VALUES (2250, "POLO", 2);
SELECT * FROM carro;

CREATE DATABASE empresa;
USE empresa;
CREATE TABLE funcionario (
	id int not null auto_increment,
    nome varchar(125) not null,
    data_nasc date not null,
    admissao datetime,
    constraint primary key (id)
);
ALTER TABLE funcionario ADD COLUMN cadastro timestamp;
DESCRIBE funcionario;
INSERT INTO funcionario (nome,data_nasc, admissao) VALUES ("Thiago","1986-09-27",current_date());
INSERT INTO funcionario (nome,data_nasc,admissao) VALUES ("João",curdate(),current_date());
SELECT * FROM funcionario;

SELECT current_date();
SELECT current_timestamp();
SELECT current_time();
SELECT curdate();
SELECT curtime();
SELECT now();
SELECT DATE_FORMAT(admissao,'%d/%m/%y') FROM funcionario; /*y minúsculo traz só os dois últimos dígitos do ano*/
SELECT nome,DATE_FORMAT(admissao,'%d/%m/%Y') as data FROM funcionario; 
SELECT DATE_ADD(admissao,INTERVAL 30 DAY) FROM funcionario;
SELECT DATE_ADD(admissao,INTERVAL 45 DAY) FROM funcionario;
SELECT nome,data_nasc,DATE_ADD(data_nasc,INTERVAL 30 DAY) FROM funcionario;
SELECT nome,admissao,DATE_ADD(admissao,INTERVAL 2 YEAR) FROM funcionario;
SELECT nome,year(data_nasc) FROM funcionario where nome like "T%";
SELECT timestampdiff(year,data_nasc,now()) from funcionario;

INSERT INTO funcionario (nome,data_nasc,admissao) VALUES ("Nathan Henrique","1998-08-26",current_timestamp());
SELECT timestampdiff(year,data_nasc,now()) as idade from funcionario;
SELECT nome,DATE_FORMAT(data_nasc,'%d/%m/%Y') as data_nascimento,DATE_FORMAT(current_date(),'%d/%m/%Y') as data_atual, timestampdiff(year,data_nasc,now()) as idade from funcionario;
 







