# Database Systems
***
## Most basic terminology
  * Data: Known facts that can be recorded that have implicit meaning
  * Database: Logically coherent collection of related data
    * Built for a specific purpose
    * Represents some aspects of the real world (miniworld)
  * Examples of large databases
    * Amazon.com's product data
    * Data collection underlying Webreg
  * Database management systems (DBMS)
    * Collection of computer programs
    * Enables users to create and maintain a DB
    * Supports concurrent access to the DB by multiple users and programs
    * Protects the DB against unauthorized access and manipulation
    * Provides means to evolve the DB as requirements change
  * Examples of database management systems
    * IBM's DB2, Microsoft Access, Microsoft SQL Server, Oracle, SAP's SQL Anywhere, MySQL, PostgreSQL
  * Database System: A collection of Database and DBMS
***
## Main Characteristics of Database Systems
  * Self-describing
    * DBS contains a database catalog with meta-data that describes the structure and constraints of the database(s)
    * Database catalog used by DBMS, and by DB users who need information about DB structure
  * Programs isolated from data through abstraction
    * DBMS does not expose details of how (or where) data is stored or how operations are implemented
    * Programs refer to an abstract model of the data, rather than data storage details
    * Data structures and storage organization can be changed without having to change the application programs
  * Support of multiple views of the data
    * Different users may see different views of the database, which contain only the data of interest to these users
***
## Database System Design Process
  * Two main activities:
    * Database design focuses on defining the database
    * Application design focuses on the programs and interfaces that access the database (out of scope of this lecture)
***
## Conceptual Design
  * Entity Relationship (ER) Model
    * High-level conceptual data model
      * an overview of the database
      * Easy to translate to data model of DBMS
      * Easy to discuss with non-database experts
    * ER Diagram
      * Diagrammatic notation of associated with the ER model
***
## Logical Design
  *
