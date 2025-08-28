package service

import (
	"kratos-tutorial/internal/service/greeter"

	"go.uber.org/fx"
)

var Providers = fx.Options(fx.Provide(greeter.NewGreeterService))
