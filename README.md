# clip-search

Run Docker Desktop, then:

```bash
docker build -t clip-search -f docker/Dockerfile .
docker run -p 4000:5000 clip-search
curl -X POST -H "Content-Type: application/json" -d '{"text":"red hat"}' http://localhost:4000/lookup
```
