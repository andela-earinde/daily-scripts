/*
Bookstore database
 */
--Connect to a different database
\connect gnerkus gnerkus

-- Drop the database if it exists
drop database bookstore;

-- Create the bookstore database
create database bookstore;

-- Connect to the database with the user gnerkus
\connect bookstore gnerkus;

-- Create the books table
create table if not exists books (
  "id" integer PRIMARY KEY,
  "title" text NOT NULL,
  "author_id" integer
);

-- Create the authors table
create table if not exists authors (
  "id" integer PRIMARY KEY CHECK(id > 100),
  "last_name" text,
  "first_name" text
);

-- Create the states table
create table if not exists states (
  "id" integer PRIMARY KEY,
  "name" text,
  "abbreviation" character(2)
);

-- Create personal list table
create table if not exists my_list (
  "todos" text
);

-- Create sequence for the book ids
create sequence book_ids start 100 increment 1 maxvalue 2147483647;

-- Create seqence for the author ids
create sequence author_ids start 100 increment 1 maxvalue 2147483647;

