curl -X POST 'http://localhost:9000/admin/auth' \
-H 'Content-Type: application/json' \
--data-raw '{
  "email": "weijiang2009@gmail.com",
  "password": "Love2009"
}'

echo 'next'

curl -X POST 'http://backend.algmon.com/admin/auth' \
-H 'Content-Type: application/json' \
--data-raw '{
  "email": "weijiang2009@gmail.com",
  "password": "Love2009"
}'
