CREATE DATABASE livraria;
USE livraria;

CREATE TABLE editora (
	id_editora int(4) zerofill not null auto_increment,
    nome_editora varchar(100) not null,
    cnpj char(14) not null,
    endereco varchar(100) not null,
    fone varchar(15) not null,
    cidade varchar(100) not null,
    estado char(2) not null,
    primary key(id_editora)
);

CREATE TABLE autor (
	id_autor int(4) zerofill not null auto_increment,
    cpf char(11) not null unique,
    nome varchar(100) not null,
    email varchar(45) not null,
    telefone char(15),
    primary key(id_autor)
);

CREATE TABLE livro (
	id_livro int(4) zerofill not null auto_increment,
    titulo varchar(75) not null,
    ISBN char(13) not null,
    paginas int(4) zerofill not null,
    idioma varchar(30) not null,
    data_publicacao date,
    id_editora int(4) zerofill,
    id_autor int(4) zerofill,
    primary key(id_livro)
);

SHOW TABLES;

INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Venus",12345678910,"Rua Lima Farias Brigadeiro 1020","48123908357","São Paulo","SP");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Andrade",23456789012,"Rua Indole Santos 345","48998904567","São Paulo","SP");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Morena",34567890321,"Rua Serra do Divisor 1127","6733057243","Campo Grande","MS");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Drize",45678904321,"Rua da Fonseca 9080","67990875465","Dourados","MS");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Belas Artes",56789043210,"Rua José Pereira 678","4633452341","Cascavel","PR");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Santo Cristo",67890543219,"Rua Copacabana 2001","2133545437","Rio de Janeiro","RJ");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Viva",78906543127,"Rua Grande 243","5433567810","Pelotas","RS");
INSERT INTO editora (nome_editora,cnpj,endereco,fone,cidade,estado) VALUES ("Zara",90123456781,"Rua da Paz 458","4833900912","São Paulo","SP");

INSERT INTO autor (cpf,nome,email,telefone) VALUES (25089056723,"José Andrade Moreira","joseamoficial@gmail.com","6799809890");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (81156721345,"Maurício de Souza","mauriciodes0uza@gmail.com","4833678909");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (06458762380,"Ana Letícia Triz","analetrizz1@gmail.com","67998786545");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (23456798010,"Teodoro Fonseca Tadeu","teodorofonsecaTadeu@gmail.com","4633456798");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (78909812334,"Içami Tiba","icamitiba26@gmail.com","4633989870");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (53412323423,"Ilhida Almeida","ilhidaalmeida1967@gmail.com","67998789561");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (12467808978,"Santos Fagunde","joseamoficial@gmail.com","46991213141");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (25486790809,"Welinton Rico Porto","joseamoficial@gmail.com","4833456745");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (68978901234,"Hundi Reis Santos","hundiletter11@gmail.com","2133213324");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (99086724531,"Arin Yewon","arinyewon@gmail.com","2198906743");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (45634512318,"Priscila Julia Almeida Trevisan","priscilajulia34@gmail.com","54990874563");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (33429801245,"Tulio Batista Frey","tuliobatistaf@gmail.com","5433456789");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (24589788890,"Neymar Junior","neymarjroff@gmail.com","2133900989");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (68903567589,"Castro Alves","castroalvesss@gmail.com","4699014567");
INSERT INTO autor (cpf,nome,email,telefone) VALUES (57284332482,"Nelson Mandela","nelsonmandela@gmail.com","21996784992");

INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("História do futebol","5768901243556",456,"Português-br","2022-06-24",0006,0013);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Era uma vez","8904561233211",578,"Português-br","2018-09-14",0007,0011);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Serra do além","8904123432109",289,"Português-br","2020-10-25",0002,0013);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("A love thing","1287903651299",155,"English","2014-02-10",0003,0001);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("A história completa do Brasil","0901487125067",1089,"Português-br","2016-08-08",0007,0012);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Indiano no Rio","9081457890123",389,"Português-br","2017-12-01",0001,0009);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("O Pantanal","6091528567090",767,"Português-br","2022-05-14",0004,0003);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Culinária sul-mato-grossense","8031678436791",290,"Português-br","2022-02-13",0003,0006);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Korean language","7809808914355",654,"Korean","2020-09-20",0005,0010);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Tempo perdido","0095175328985",890,"Português-br","2019-07-09",0005,0007);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Cebolinha","8889368790121",356,"Português-br","2022-11-01",0002,0002);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Best travel places","4353452167809",212,"English","2018-12-12",0007,0012);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Guia financeiro","7803548725800",310,"Português-br","2021-07-16",0001,0008);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Um vigarista na Bahia","9703859228464",590,"Português-br","2020-12-02",0003,0004);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Quem ama educa","7700914375675",805,"Português-br","2012-07-08",0006,0005);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Educando certo!","6899033544769",709,"Português-br","2015-05-05",0003,0005);
INSERT INTO livro (titulo,ISBN,paginas,idioma,data_publicacao,id_editora,id_autor) VALUES ("Sem vida","6789984456621",900,"Português-br","2020-09-30",0009,0014);

SELECT * FROM editora;
SELECT * FROM autor;
SELECT * FROM livro;

SELECT livro.titulo AS livro, autor.nome AS autor, editora.nome_editora AS editora
FROM livro
INNER JOIN autor
ON livro.id_autor = autor.id_autor
INNER JOIN editora
ON livro.id_editora = editora.id_editora;

SELECT autor.nome, livro.titulo
FROM autor
LEFT JOIN livro
ON livro.id_autor = autor.id_autor;

UPDATE livro SET id_autor = 0016 WHERE id_livro = 0017;

SELECT autor.nome, livro.titulo
FROM autor
RIGHT JOIN livro
ON livro.id_autor = autor.id_autor;

/* Crie um select que apresente o nome da editora, o ISBN do livro, o título do livro, 
a quantidade de páginas do livro, o nome do autor, o email dos autores, após liste so-
mente as editoras do estado de São Paulo*/
SELECT editora.nome_editora, livro.ISBN, livro.titulo, livro.paginas, autor.nome, autor.email
FROM livro
INNER JOIN editora
ON livro.id_editora = editora.id_editora
INNER JOIN autor
ON livro.id_autor = autor.id_autor
ORDER BY nome_editora ASC;

SELECT editora.nome_editora, livro.ISBN, livro.titulo, livro.paginas
FROM livro
INNER JOIN editora 
ON livro.id_editora = editora.id_editora
WHERE estado = "SP";

SELECT editora.nome_editora, livro.ISBN, livro.titulo, livro.paginas
FROM livro
RIGHT JOIN editora 
ON livro.id_editora = editora.id_editora
WHERE estado = "SP"
ORDER BY nome_editora ASC;













































