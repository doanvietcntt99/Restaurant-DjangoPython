create database PythonWebTasteit;
use PythonWebTasteit;
create table Admin_Login
(
	idAdmin int auto_increment primary key,
    usernameAdmin varchar(50) not null unique,
    passwordAdmin varchar(50) not null
);
create table Admin_Position
(
	positionIdAdmin int auto_increment primary key,
    positionNameAdmin nvarchar(50) not null
);
create table Admin_Detail
(
	idAdmin int primary key,
    fullnameAdmin nvarchar(50) not null,
    dobAdmin date not null,
    phoneAdmin varchar(12) not null,
    emailAdmin varchar(50) not null,
    addressAdmin nvarchar(50) not null,
    positionIdAdmin int not null,
    statusAdmin binary default true,
    avatarAdmin nvarchar(500) default 'default-avatar.jpg',
	foreign key (idAdmin) references Admin_Login(idAdmin),
    foreign key (positionIdAdmin) references Admin_Position(positionIdAdmin)
);
create table User_Login
(
	idUser int primary key auto_increment,
    usernameUser varchar(50) not null unique,
    passwordUser varchar(50) not null
);
create table User_Detail
(
	idUser int primary key,
    fullnameUser nvarchar(50) not null,
    dobUser date not null,
    phoneUser varchar(12) not null,
    emailUser varchar(50) not null,
    addressUser nvarchar(50),
    pointUser float default '1',
    statusUser bit default true,
    avatarUser nvarchar(50) default 'default-avatar.jpg',
    foreign key (idUser) references User_Login(idUser)
);

insert User_Login(usernameUser, passwordUser) values('admin2', 'admin123');
insert into User_Login values (usernameUser = 'admin123', passwordUser = '456');
create table Food_Detail
(
	idFoodDetail int primary key auto_increment,
    nameFoodDetail nvarchar(50) not null,
    priceFoodDetail float not null,
    desciptionFoodDetail nvarchar(200) not null,
    avatarFoodDetail nvarchar(200) default 'default-food.jpg'
);
create table Chef_Position
(
	positionIdChef int primary key auto_increment,
    positionNameChef nvarchar(50)
);
create table Chef
(
	idChef int primary key auto_increment,
    nameChef nvarchar(50) not null,
    positionIdChef int not null,
	dayBeginChef date not null,
    foreign key (positionIdChef) references Chef_Position(positionIdChef)
);
create table Food_Chef
(
	idFoodChef int auto_increment primary key,
    idFoodDetail int not null,
    idChef int not null,
    rateFoodChef int default 5,
    foreign key(idFoodDetail) references Food_Detail(idFoodDetail),
    foreign key(idChef) references Chef(idChef)
);
create table Booking
(
	idBooking int primary key auto_increment,
    nameBookingGuest nvarchar(50) not null,
    emailBookingGuest varchar(50) not null,
    dateTimeBooking datetime not null,
    totalQuantityFoodBooking int not null,
    totalPriceFoodBooking float not null
);
create table Booking_Detail
(
	idBookingDetail int primary key auto_increment,
	idBooking int not null,
    idFoodDetail int not null,
    idChef int not null,
    quantityBookingDetail int not null,
    priceBookingDetail float not null,
    foreign key (idBooking) references Booking(idBooking),
    foreign key (idFoodDetail) references Food_Detail(idFoodDetail),
    foreign key (idChef) references Chef(idChef)
);
create table Respondent
(
	idRespondent int primary key auto_increment,
    nameRespondent nvarchar(50) not null
);
create table FeedBack
(
	idFeedBack int primary key auto_increment,
    idRespondent int not null,
    titleFeedBack nvarchar(50) not null,
    decriptionFeedBack nvarchar(200) not null,
    foreign key (idRespondent) references Respondent(idRespondent)
)





