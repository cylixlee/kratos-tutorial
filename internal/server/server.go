package server

import (
	"go.uber.org/fx"
)

// ProviderSet is server providers.
var (
	Providers = fx.Options(
		fx.Provide(NewGRPCServer),
		fx.Provide(NewHTTPServer),
	)
)
