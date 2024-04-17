load_fixtures:
	docker-compose run --rm web sh -c "python manage.py loaddata restaurant/fixtures/bookings.json"
	docker-compose run --rm web sh -c "python manage.py loaddata restaurant/fixtures/categories.json"
	docker-compose run --rm web sh -c "python manage.py loaddata restaurant/fixtures/menus.json"

test:
	docker-compose run --rm web sh -c "python manage.py test"

shell:
	docker-compose run --rm web sh -c "python manage.py shell"

ssh_w:
	docker-compose exec web sh

