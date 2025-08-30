package service

import (
	"go.uber.org/fx"
)

// ProviderSet is service providers.
var Providers = fx.Provide(NewGreeterService)
