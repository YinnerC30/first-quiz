import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/
#
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is
# created in the file `pets_db.py`.
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

SELECT an.name AS animal_name,
       an.species AS animal_specie,
       an.age AS animal_age
FROM   animals AS an
       LEFT JOIN people_animals AS pea
              ON pea.pet_id = an.animal_id
WHERE  owner_id IS NULL;

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners.
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT count(*) AS total
FROM   animals AS an
       INNER JOIN people_animals AS pea
               ON pea.pet_id = an.animal_id
       INNER JOIN people AS pe
               ON pea.owner_id = pe.person_id
WHERE  an.age > pe.age;

"""

# Part 4.C: BONUS CHALLENGE!
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """

SELECT pe.name as name_person,
       an.name as name_animal,
       an.species as specie_animal
FROM animals AS an
         INNER JOIN people_animals AS pea
                    ON pea.pet_id = an.animal_id
         INNER JOIN people AS pe
                    ON pea.owner_id = pe.person_id
WHERE pea.owner_id = 2
  AND pea.pet_id <> (SELECT pea2.pet_id AS animal_id
                     FROM people_animals AS pea2
                     WHERE pea2.owner_id <> 2
                       AND pea2.pet_id IN (SELECT pea3.pet_id
                                         FROM people_animals AS pea3
                                         WHERE pea3.owner_id = 2));


"""
