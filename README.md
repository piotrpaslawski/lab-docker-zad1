# Laboratorium "Programowanie Full-Stack w Chmurze Obliczeniowej"

Repozytorium powstało w ramach zadania 1.

Budowanie opracowanego obrazu kontenera:
```
docker build -t serwer -f DockerFile .
```

Uruchomienie kontenera:
```
docker run --name serwer -p 8000:8000 serwer
```

Uzyskanie logów, które wygenerował serwer w trakcie uruchamiana kontenera:
```
docker logs serwer
```

Sprawdzenie ile warstw posiada zbudowany obraz:
```
docker history serwer
```
