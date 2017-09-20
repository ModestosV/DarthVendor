echo "Create Admin Table"
python3 manage.py create_admin_table
echo "Populate Admin Table"
python3 manage.py populate_admin_table

echo "Create Token Table"
python3 manage.py create_token_table

echo "Done"