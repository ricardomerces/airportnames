Fonte:
[https://github.com/GoogleCloudPlatform/endpoints-quickstart]

# Como executar:
```
$ docker run --name airportnames -p 8080:8080 rmerces/airportnames
```

# Consulta:

iataCode --> código iata dos aeroportos

```
http://localhost:8080/airportName?iataCode=SDU
```
