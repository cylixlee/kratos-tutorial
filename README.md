# Kratos Tutorial Template
This branch (`main`) is a template for creating a Kratos project. It has migrated to using `fx` as Dependency Injection framework since `wire` is no longer maintained.

Also, an alternative `make.py` is introduced for those who could not run Makefile (for example, Windows users).

### Install Kratos
```
go install github.com/go-kratos/kratos/cmd/kratos/v2@latest
```

### Create a service
```
# Create a template project
kratos new server

cd server
# Add a proto template
kratos proto add api/server/server.proto
# Generate the proto code
kratos proto client api/server/server.proto
# Generate the source code of service by proto file
kratos proto server api/server/server.proto -t internal/service

go generate ./...
go build -o ./bin/ ./...
./bin/server -conf ./configs
```

### Generate other auxiliary files by Makefile
```
# Download and update dependencies
make init
# Generate API files (include: pb.go, http, grpc, validate, swagger) by proto file
make api
# Generate all files
make all
```

### Generate other auxiliary files by `make.py`
A Python scripts is written to act as a cross-platform Makefile. Python 3 is required.
```
# Download and update dependencies
python make.py init
# Generate API files (include: pb.go, http, grpc, validate, swagger) by proto file
python make.py api
# Generate all files
python make.py all
```

### Docker
```bash
# build
docker build -t <your-docker-image-name> .

# run
docker run --rm -p 8000:8000 -p 9000:9000 -v </path/to/your/configs>:/data/conf <your-docker-image-name>
```

