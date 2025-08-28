package biz

import (
	"kratos-tutorial/internal/biz/greeter"

	"go.uber.org/fx"
)

var Providers = fx.Options(fx.Provide(greeter.NewGreeterUsecase))
