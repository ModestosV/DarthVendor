echo "Create Admin Table"
python3 manage.py create_admin_table

echo "Populate Admin Table"
python3 manage.py populate_admin_table

echo "Create Token Table"
python3 manage.py create_token_table

echo "Create Item Table"
python3 manage.py create_item_table

echo "Create Desktop Table"
python3 manage.py create_desktop_table

echo "Populate Desktop Table"
python3 manage.py populate_desktop_table

echo "Create Laptop Table"
python3 manage.py create_laptop_table

echo "Create Monitor Display Table"
python3 manage.py create_monitor_display_table

echo "Populate Monitor Display Table"
python3 manage.py populate_monitor_display_table

echo "Create Tablet Table"
python3 manage.py create_tablet_table

echo "Populate Tablet Table"
python3 manage.py populate_tablet_table

echo "Create Television Table"
python3 manage.py create_television_table

echo "Done"
