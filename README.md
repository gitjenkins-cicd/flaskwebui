# flaskwebuinew

docker run --name mysql-latest  \
-p 3306:3306  \
-e MYSQL_ROOT_HOST='%' -e MYSQL_ROOT_PASSWORD='strongpassword'   \
-d mysql/mysql-server:latest

docker exec -it mysql-latest mysql -uroot -pstrongpassword

CREATE database codethunder;

CREATE TABLE contacts (
  sno int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50) DEFAULT NULL,
  phone_num int(10) DEFAULT NULL,
  msg varchar(1000) DEFAULT NULL,
  date date DEFAULT NULL,
  email varchar(40) DEFAULT NULL,
  PRIMARY KEY (sno)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1

git clone https://github.com/gitjenkins-cicd/flaskwebuinew.git

docker build -t flaskwebuinew .

docker run -itd -p 80:5005 flaskwebuinew  
