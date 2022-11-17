/* CRIANDO O BANCO */
-------------------------------------------------------------
create database DGTN;
use DGTN;
-------------------------------------------------------------
-------------------------------------------------------------
/* CRIANDO AS TABELAS */
-------------------------------------------------------------
create table departamentos(
	id_dep int auto_increment not null,
    nome_dep varchar(50) not null,
    constraint primary key (id_dep)
    );
    
    show tables;

create table cargos(
	id_cargo int auto_increment not null,
    nome_cargo varchar(50) not null,
    id_dep int not null,
    constraint primary key (id_cargo),
    constraint foreign key (id_dep) references departamentos(id_dep)
    );
    
    show tables;
    
    
create table funcionarios(
	id_func int auto_increment not null,
    cpf char(11) unique,
    nome varchar(100) not null,
    idade int not null,
    salario decimal(10,2) not null,
    endereco varchar(255) not null,
    telefone char(11),
	data_nascimento datetime,
    data_admissao date,
    cidade varchar(100),
    nacionalidade varchar(50),
    id_dep int not null,
    id_cargo int not null,
    constraint primary key (id_func),
    constraint foreign key (id_dep) references departamentos(id_dep),
    constraint foreign key (id_cargo) references cargos(id_cargo)
    );

describe funcionarios;
    
    create table dependentes(
    id_dependente int auto_increment not null,
    certidao char(12) not null,
    nome varchar(100),
	data_nascimento datetime,
    local_nascimento varchar(100),
    id_func int not null,
    constraint primary key (id_dependente),
    constraint foreign key (id_func) references funcionarios(id_func)
    );
    
    show tables;
--------------------------------------------------------------------------
/* INSERINDO OS DADOS NA TABELA DEPARTAMENTOS */
--------------------------------------------------------------------------
 INSERT INTO `departamentos` VALUES (1,'Administrativo'),(2,'Produção'),(3,'Financeiro'),(4,'Departamento Pessoal'),(5,'Comercial'),(6,'Vendas'),(7,'TI'),(8,'Diretoria');

--------------------------------------------------------------------------
/* INSERINDO OS DADOS NA TABELA CARGOS */
--------------------------------------------------------------------------
 
INSERT INTO `cargos` VALUES (1,'Analista de Controle e Logística',1),(2,'Tesoureiro',3),(3,'Conferente',2),(4,'Supervisor',2),(5,'Gestão de Pessoas',4),(6,'Vendedor',6),(7,'Gerente',6),(8,'Desenvolvedor',7),(9,'Analista de TI',7),(10,'Engenheiro de Software',7),(11,'Diretor(a)',8);

--------------------------------------------------------------------------
/* INSERINDO OS DADOS NA TABELA FUNCIONÁRIOS */
--------------------------------------------------------------------------
	 


INSERT INTO `funcionarios` VALUES (1,'02802903000','Arthur da Rocha Verga',28,2700.00,'Av. Afonso Pena, 5432','6799999999','1991-06-22','2021-11-30','Campo Grande','Brasileiro',2,3),(2,'02802903011','Bianca Nair Melo Ramires',25,2700.00,'Av. Afonso Pena, 5432','6799999999','1991-06-22','2020-02-02','Manaus','Brasileira',4,5),(3,'02802903022','Bruno Eduardo de Mello Alves',34,6500.00,'Av. Afonso Pena, 5432','6799999999','1991-06-22','2020-06-07','Campo Grande','Brasileiro',7,10),(4,'02802903033','Danise Regina Rodrigues da Silva',52,8500.00,'Av. Afonso Pena, 5432','6799999999','1991-06-22','2021-01-10','Belém','Brasileira',6,7),(5,'02802903044','Douglas Gomes dos Santos',33,4800.00,'Rua das Arvores,28','6799999999','1991-06-22','2021-11-30','Dourados','Brasileiro',7,9),(6,'02802903101','Heraldo Luiz Medina Ribeiro',35,12700.00,'Av. Calógeras,55','6799999999','1991-06-22','2021-11-30','Dourados','Brasileiro',2,4),(7,'02802903105','Heytor Malaquias Bueno',25,14000.00,'Av. Calógeras,599','6799999999','1991-06-22','2019-09-09','Naviraí','Brasileiro',8,11),(8,'02802903199','Lucas Henrique de Oliveira',18,4400.00,'Rua Rui Barbosa,121','6799999999','1991-06-22','2021-11-30','Dourados','Brasileiro',7,9),(9,'02802903388','Luiz André da Silva',18,2700.00,'Rua Rui Barbosa,121','6799999999','1991-06-22','2021-11-30','São Paulo','Brasileiro',2,3),(10,'02802903065','Magno Marcos Borges Da Silva',29,6600.00,'Rua Rui Barbosa,121','6799999999','1991-06-22','2021-11-30','São Paulo','Brasileiro',6,6),(11,'02802903076','Manoel Teodoro Neto',22,4900.00,'Rua 13 de Maio,87','6799999999','1991-06-22','2021-11-30','Campo Grande','Brasileiro',6,6),(12,'02802903058','Mateus Borges Oliveira Gaspio de Araujo',18,4900.00,'R. 14 de Júlio,21','6799999999','1991-06-22','2021-11-30','São Paulo','Brasileiro',2,3),(13,'02802903039','Max Marcelo Ferreira Júnior',26,4900.00,'Rua Manoel Dantas,44','6799999999','1991-06-22','2021-11-30','Rio de Janeiro','Brasileiro',7,8),(14,'02802903071','Mayã da Silva de Souza',22,2700.00,'Rua Gal. Osório,21','6799999999','1991-06-22','2021-11-30','Rio de Janeiro','Brasileiro',2,3),(15,'02802903032','Patrick de Alcantara Strogueia',29,7700.00,'Av. Norte Sul,999','6799999999','1991-06-22','2021-11-30','Campo Grande','Brasileiro',2,3),(16,'02802903111','Renan Goetz Ojeda',44,2700.00,'Rua Bonita, 345','6799999999','1991-06-22','2021-11-30','Sidrolândia','Brasileiro',2,3),(17,'02802903999','Rogers Barros de Paula',38,7700.00,'Av. Mato Grosso,121','6799999999','1991-06-22','2021-11-30','Campo Grande','Brasileiro',6,6),(18,'02802903555','Thamiris dos Santos Silva',24,7700.00,'Av. Norte,3333','6799999999','1991-06-22','2021-11-30','Campo Grande','Brasileira',1,1),(19,'02802903470','Thiago Gonçalves de Almeida',35,2700.00,'Rua da Ilha,144','6799999999','1991-06-22','2021-11-30','Campo Grande','Brasileiro',2,3),(20,'02802903512','Wenderson Nogueira de Lima',35,5200.00,'Rua da Lontra','6799999999','1991-06-22','2021-11-30','Sidrolândia','Brasileiro',2,4),(21,'02802903123','Willer Velasco da Costa',24,4900.00,'Av São Joãoo, 444','6799999999','1991-06-22','2021-11-30','Sidrolândia','Brasileiro',7,8),(22,'02802903134','Antonio Dias Rodruigues',24,2700.00,'Rua Antonio M Coelho','6799999999','1991-06-22','2021-11-30','Caarapó','Brasileiro',2,3),(23,'02802903155','Maria Aparecida Fernandes',24,2700.00,'Av. Duque de Caxias,31','6799999999','1991-06-22','2021-11-30','Sidrolândia','Brasileiro',2,3),(24,'04402801521','Zilda Maria Silva Souza',48,2700.00,'Av. dos Cafezais,444','679999999','1967-06-01','1999-11-20','Rio Brilhante','Brasileira',2,3);


--------------------------------------------------------------------------
/* INSERINDO OS DADOS NA TABELA DEPENDENTES */
--------------------------------------------------------------------------
describe dependentes;

INSERT INTO `dependentes` VALUES (1,'213244','Marco Antonio','2000-05-18 00:00:00','Campo Grande',4),(2,'4444','Bruno Zildo','2003-08-15 00:00:00','Campo Grande',24);

SELECT * FROM cargos;
SELECT * FROM departamentos;
SELECT * FROM funcionarios;

/* inner join sem preguiça */
SELECT departamentos.nome_dep, cargos.nome_cargo
FROM departamentos
INNER JOIN cargos
ON departamentos.id_dep = cargos.id_dep;

/* inner join usando apelidos nas tables */
SELECT * FROM departamentos AS dep
INNER JOIN cargos AS car
ON dep.id_dep = car.id_dep;

SELECT funcionarios.id_func ,funcionarios.nome, departamentos.nome_dep
FROM funcionarios
INNER JOIN departamentos
ON funcionarios.id_dep = departamentos.id_dep;

/* inner join em três tabelas */
SELECT funcionarios.nome, cargos.nome_cargo, departamentos.nome_dep
FROM funcionarios
INNER JOIN cargos
ON funcionarios.id_cargo = cargos.id_cargo
INNER JOIN departamentos
ON funcionarios.id_dep = departamentos.id_dep;

/* inner join com três tabelas ordenadas */
SELECT funcionarios.nome, cargos.nome_cargo, departamentos.nome_dep
FROM funcionarios
INNER JOIN cargos
ON funcionarios.id_cargo = cargos.id_cargo
INNER JOIN departamentos
ON funcionarios.id_dep = departamentos.id_dep 
ORDER BY nome ASC;







    