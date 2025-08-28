package data

import (
	"kratos-tutorial/internal/conf"

	"github.com/go-kratos/kratos/v2/log"
	"go.uber.org/fx"
)

// ProviderSet is data providers.
var (
	Providers = fx.Options(
		fx.Provide(NewData),
		fx.Provide(NewGreeterRepo),
	)
)

// Data .
type Data struct {
	// TODO wrapped database client
}

// NewData .
func NewData(lc fx.Lifecycle, c *conf.Data, logger log.Logger) (*Data, error) {
	lc.Append(fx.StopHook(func() {
		log.NewHelper(logger).Info("closing the data resources")
	}))
	return &Data{}, nil
}
