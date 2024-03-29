load_fixtures:
	docker-compose run --rm web sh -c "python manage.py loaddata restaurant/fixtures/bookings.json"
	docker-compose run --rm web sh -c "python manage.py loaddata restaurant/fixtures/categories.json"
	docker-compose run --rm web sh -c "python manage.py loaddata restaurant/fixtures/menus.json"
