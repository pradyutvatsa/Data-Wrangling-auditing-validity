# Data-Wrangling-auditing-validity

This piece of code takes a csv input that is information on autos. The objective is to check whether the field 'productionStartYear' values conform to a defined schema. 

What is the schema? Find the details below: 
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- Use csv.DictReader and csv.DictWriter to read and write files
