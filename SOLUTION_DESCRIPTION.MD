# Deliverables



## Data Model 
The [Data Model](data_model/DataModel.pdf), generated via dbdiagram.io and saved as a .pdf, is located in the [data_model](data_model) folder. A text file that can be used to replicate the [schema](data_model/data_model_code.txt) is also present.

The Data Model is fairly well normalized, and takes advantage of two simplifications of note:
- The ISO Language code appears in both the spoken language JSON-like raw field `spoken_languages` as well as the `original_language` field.  Relationships to a single 'language' table for both of these should exist.
- A given member of the production team can be both cast and crew (e.g., Woody Allen often directs movies he acts in).  A 'company_member' table is created to store all memebers of the production team, and then 1-to-Many relationships for cast and crew can be realized.

---

## Implementation

The implementation code is written in **Python**.  The [src/ingest.py](src) file contains the code to extract and load the raw data, and the [src/api_queries.py](src) file contains the API queries for the pre-identified reports of interest.

**PostgreSQL** and psycopg2 are leveraged to extract the approriate fields for for the database.

The 'movies_metatdata.csv' raw data file has some data integrity issues - three records have incorrect (additional) line breaks.  Error handling should be considered to deal with this type of issue, but disucssing the root cause with the data provider should also be a part of the data integrity solution.

Both the ingestion and the API files could be structures as Classes, given more time to configure and test.

No unit testing was set up for these scripts; that is also something that could be added fairly easily given more time.

** Caveats and Notes:

- The "popularity" concept could be appraoched with different methods.  Three fields in the 'moveies_metadata' file could factor into this metric (`popularity`, `vote_average`, `vote_count`) and there is also a 'ratings' file.  For simplicity, the `popularity` field was used, but this is a good example of a situation where confirming customer requirements would be wise. 

- The `popularity` field itself is interesting, in that there is an apparantly complex calculation behind it.   Values can range from 0 to +Inf (read more [here](https://www.themoviedb.org/talk/5141d424760ee34da71431b0)).  Using the SQL `AVG` function is likely not an appropriate way to handle this data - again, a conversation with the end user here would be wise.

---

## Design

Storage via S3 is a simple and straightforward solution.  It's cost effective and scalable.

**Snowflake** could also be a part of this solution would would fit into the design well.  It uses S3 for storage and permits multi-cluster virtual warehouses for compute activities to allow autoscaling.  This might be excessive for the scope of this assignment, but a general model it could a a useful component of the overall solution.  Materialized Views (MVs) could be configured in Snowflake for the specified reporting needs using the SQL query provided in 

Data serving: Snowflake's MVs integrate with **Looker** which could allow end users to dovetail this data stream into their existing toolbox.  Snowflake also has access control privleges with MVs, if sensitive material were to be involved.
If Looker wasn't a desired solution, a Flask app could be written for simple web-based access.

A scheduled event tool to trigger the data ingestion code, like **AWS Lambda**, could be configured to run monthly after the expected new files are delivered.  Since the event would trigger infrequently, it should be possible to run it during off-peak times.

