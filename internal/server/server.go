package server

import (
	"go.uber.org/fx"
)

// ProviderSet is server providers.
var Providers = fx.Provide(NewGRPCServer, NewHTTPServer)
