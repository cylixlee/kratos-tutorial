package server

import "go.uber.org/fx"

var Providers = fx.Options(fx.Provide(NewHTTPServer), fx.Provide(NewGRPCServer))
