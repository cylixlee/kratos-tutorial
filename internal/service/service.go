package service

import (
	"kratos-tutorial/internal/service/greeter"

	"go.uber.org/fx"
)

var Providers = fx.Provide(greeter.NewGreeterService)
