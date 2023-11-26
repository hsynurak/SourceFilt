rm -rf log/*.log

source .env
export PATH=${PATH}:/usr/local/mysql/bin/

#mysql -h "localhost" --user="root" --password=${PASSWORD} "sourcefilt" < "sql/create_source.sql"

for f in scrapers/*.py; do source_env/bin/python3.11  "$f"; done

source_env/bin/python3.11 utils/remove_duplicates.py

mysql -h "localhost" --user="root" --password=${PASSWORD} "sourcefilt" < "sql/create_book.sql"

source_env/bin/python3.11 book.py

mysql -h "localhost" --user="root" --password=${PASSWORD} "sourcefilt" < "sql/finalize_source.sql"