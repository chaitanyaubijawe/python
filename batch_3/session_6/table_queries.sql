-- Structured query language....
-- DML
  -- Data Manipulation :: UPDATe/INSERT/SELECT
-- DDL
  -- ALter/CREATE

CREATE TABLE `bajaj_insurance`.`insurance_transaction` (
  `idinsurance_transaction` INT NOT NULL AUTO_INCREMENT,
  `transaction_id` VARCHAR(45) NULL,
  `csc_transaction_id` VARCHAR(45) NULL,
  PRIMARY KEY (`idinsurance_transaction`));



select * from insurance_transaction --

select * from insurance_transaction where transaction_id="third_transaction"
select * from insurance_transaction where transaction_id like "%transaction%"
select * from insurance_transaction where transaction_id like "f%"

insert into insurance_transaction (transaction_id, csc_transaction_id) values("third_transaction", "csc_transaction")
