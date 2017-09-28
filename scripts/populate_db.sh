echo "Create Admin Table"
python3 manage.py create_admin_table

echo "Populate Admin Table"
python3 manage.py populate_admin_table

echo "Create Token Table"
python3 manage.py create_token_table

echo "Create Item Table"
python3 manage.py create_item_table

echo "Populate Item Table"
python3 manage.py populate_item_table

echo "Done"