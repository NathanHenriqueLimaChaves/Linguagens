SHOW DATABASES;
CREATE DATABASE netflix;
USE netflix;
SHOW TABLES;

CREATE TABLE usuarios (
	id_usuario int unsigned not null unique auto_increment,
    cpf char(11) unique not null,
    nome varchar(100) not null,
    email varchar(100) not null,
    senha varchar(30) not null,
    primary key(id_usuario)
);

CREATE TABLE series (
	id_serie int unsigned not null unique auto_increment,
    nome varchar(100) not null,
    sinopse varchar(100) not null,
    temporadas smallint not null,
    primary key(id_serie)
);

CREATE TABLE play (
	id_play int unsigned not null unique auto_increment,
    data_play datetime,
    id_usuario int unsigned not null,
    id_serie int unsigned not null,
    constraint primary key(id_play),
    constraint foreign key(id_usuario) references usuarios(id_usuario),
    constraint foreign key(id_serie) references series(id_serie)
);

INSERT INTO usuarios(cpf,nome,email,senha) VALUES (25081190024,"Celia Regina Seixas","celiaseixas53@gmail.com","celinha531090");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (06458769812,"Nathan Henrique Lima","nathanhenriquelima@gmail.com","nathan1990#4");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (19980673453,"Silvana Lima","silvanalima20@gmail.com","silclarinha33_1980");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (17108965744,"Kleber Garcia","kleberglm@gmail.com","kleber_890_$");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (89400912155,"João Vitor","joaovitoraner15@gmail.com","joaov$%3241");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (79089098009,"Ana Clara","aninhaclararoblox@gmail.com","aninha$mel213");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (44565766890,"Fernando Guidorizzi","fernandoguidorizzioficial@gmail.com","ferguidorizzi#@190");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (56711221987,"Airton Lutz","aitonlutzacademiaS2@gmail.com","lutzfefe4p0");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (22132438098,"Daniela Souza","danisouza99@gmail.com","dani#1990_pç");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (32467668003,"Erick Mendes","erickmendesvendedor45@gmail.com","erick#_980!");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (65312548901,"José Fernandes","josefernan89@gmail.com","jose_12qw_çop");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (42121231005,"Vitor Guidorizzi","vitordevoficial@gmail.com","vito$#%678_gui");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (11312089077,"Catarina Sartori","catarinalinda1000@gmail.com","catarinasar!23!43");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (36903167943,"Yashimin Belucci","yashibeluccihg@gmail.com","beluc1c1_0po90");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (00908112342,"Jesus Martinz","jesusmartinz123@gmail.com","jesusinhojes198");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (54631289078,"Larissa Reiz","larissaR709@gmail.com","laryyyreizz!2121");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (55655732111,"Matheus Andrade","matandrade398kill@gmail.com","matkillmeu*89");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (24312322090,"Nathalia Clagnam","nathaliaclagnam24@gmail.com","nathaliaclagnam$$521");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (76878909088,"Caio Mesquita","caiomedmesquita@gmail.com","caiomediS2_tret");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (31112145333,"Bruno Kiel","brunokielinvestfed@gmail.com","kielINVESTE#2022pou");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (55768790015,"Jordana Costa","jordmodeloficial@gmail.com","jordKLC1209pol");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (10908902316,"Geisy Alves","geisyalvesss1100@gmail.com","geisyBRILLalv2109!@#");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (43908909081,"Gabriela Herrerias","gabiherreriaswill@gmail.com","gabiherre*&¨21");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (11000102456,"Nathalia Maróstica","natimarosticavet@gmail.com","Natvet@!2110");
INSERT INTO usuarios(cpf,nome,email,senha) VALUES (22276650099,"Gabriela Harada","gabiharada25178_0@gmail.com","gabiharadamedforlife@$!");

SELECT * FROM usuarios;

INSERT INTO series(nome,sinopse,temporadas) VALUES ("Peaky Blinders","Uma notória gangue da Inglaterra de 1919 é liderada pelo cruel Tommy Shelby, um criminoso...",6);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("ICarly","Carly, de 13 anos, cria uma websérie com a ajuda da melhor amiga Sam...",1);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Stranger Things","Quando um garoto desaparece, a cidade toda participa nas buscas...",4);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Lucifer","Entediado com a vida nas trevas, o diabo se muda para Los Angeles...",6);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Sex Education","O inseguro Otis manja tudo quando o negócio é aconselhamento sexual...",3);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Round 6","Centenas de jogadores falidos aceitam um estranho convite para um jogo...",1);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Vikings","Esta série dramática acompanha a vida do viking Ragnar Lothbrok ...",6);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("The Walking Dead","Zumbis dominam o mundo dos vivos, e os sobreviventes unem forças para manter viva a raça humana.",10);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Você","Obsessivo e perigosamente charmoso, ele vai ao extremo para entrar na vida de quem o fascina...",3);
INSERT INTO series(nome,sinopse,temporadas) VALUES ("Breaking Bad","Ao saber que tem câncer, um professor passa a fabricar metanfetamina pelo futuro da família...",5);

SELECT * FROM series;

INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),2,9);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),15,7);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),5,1);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),7,9);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),25,4);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),9,3);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),18,1);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),3,6);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),8,9);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),21,4);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),11,6);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),10,8);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),16,2);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),19,9);
INSERT INTO play(data_play,id_usuario,id_serie) VALUES (current_timestamp(),7,2);

SELECT * FROM play;

/* Utilizando o INNER JOIN, selecione todos os usuários que deram play em alguma série */
SELECT usuarios.nome, play.id_serie, play.data_play
FROM usuarios
INNER JOIN play
ON usuarios.id_usuario = play.id_usuario
ORDER BY id_serie ASC;

/* Utilizando o INNER JOIN, selecione todas as séries que constam algum play */
SELECT series.nome, play.id_play, play.data_play
FROM play
INNER JOIN series
ON play.id_serie = series.id_serie
ORDER BY series.nome ASC;

/* Utilizando o INNER JOIN, apresente o nome do usuário e qual série ele deu play */
SELECT play.id_play, usuarios.nome AS usuário, series.nome AS série
FROM play
INNER JOIN usuarios
ON play.id_usuario = usuarios.id_usuario
INNER JOIN series
ON play.id_serie = series.id_serie
ORDER BY play.id_play ASC;
