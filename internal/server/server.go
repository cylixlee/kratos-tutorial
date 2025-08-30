package server

import "go.uber.org/fx"

var Providers = fx.Provide(NewHTTPServer, NewGRPCServer)
