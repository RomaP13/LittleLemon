build:
	docker-compose build

build_dev:
	docker-compose build --build-arg DEV=true

up:
	docker-compose up

make_migr:
	docker-compose run --rm web sh -c "python manage.py makemigrations restaurant"

migr:
	docker-compose run --rm web sh -c "python manage.py migrate"

super:
	docker-compose run --rm web sh -c "python manage.py createsuperuser"

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

