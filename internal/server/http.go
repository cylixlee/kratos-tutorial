package server

import (
	greeterV1 "kratos-tutorial/api/greeter/v1"
	"kratos-tutorial/internal/conf"
	"kratos-tutorial/internal/service/greeter"

	"github.com/go-kratos/kratos/v2/middleware/recovery"
	"github.com/go-kratos/kratos/v2/transport/http"
	"go.uber.org/fx"
)

type HTTPServerParams struct {
	fx.In

	greeterService *greeter.GreeterService
}

// NewHTTPServer new an HTTP server.
func NewHTTPServer(params HTTPServerParams, c *conf.Server) *http.Server {
	var opts = []http.ServerOption{
		http.Middleware(
			recovery.Recovery(),
		),
	}
	if c.Http.Network != "" {
		opts = append(opts, http.Network(c.Http.Network))
	}
	if c.Http.Addr != "" {
		opts = append(opts, http.Address(c.Http.Addr))
	}
	if c.Http.Timeout != nil {
		opts = append(opts, http.Timeout(c.Http.Timeout.AsDuration()))
	}
	srv := http.NewServer(opts...)

	greeterV1.RegisterGreeterHTTPServer(srv, params.greeterService)
	return srv
}
