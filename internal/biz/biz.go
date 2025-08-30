package biz

import (
	"go.uber.org/fx"
)

// ProviderSet is biz providers.
var Providers = fx.Provide(NewGreeterUsecase)
