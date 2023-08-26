create database if not exists hackout;
use hackout;
create table if not exists retail(hsn_code varchar(7), medicine_name varchar(40), quantity int, stock int, rate int, amount int, discount int, taxable_value int, cgst int, sgst int, igst int, cess int, total int, demand varchar(4));
