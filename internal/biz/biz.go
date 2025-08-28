package biz

import (
	"go.uber.org/fx"
)

// ProviderSet is biz providers.
var (
	Providers = fx.Options(fx.Provide(NewGreeterUsecase))
)
